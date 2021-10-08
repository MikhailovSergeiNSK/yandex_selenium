#!/usr/bin/python3
# -*- encoding=utf8 -*-

from pages.yandex import MainPage
import time
#python -m pytest -v --driver Chrome --driver-path ~/chrome tests/test_smoke_yandex.py


def test_check_yandex_search(web_browser):
    """ search in yandex. """

    #1)	Зайти на yandex.ru
    page = MainPage(web_browser)

    #2)	Проверить наличия поля поиска
    assert page.search.is_visible(), 'search field not found'

    #3)	Ввести в поиск Тензор
    page.search = 'Тензор'

    #4)	Проверить, что появилась таблица с подсказками (suggest)
    time.sleep(2)
    assert page.suggest.is_visible(), 'suggest not found'

    #5)	При нажатии Enter появляется таблица результатов поиска
    page.search.send_keys(u'\ue007', clear=False)
    page.wait_page_loaded()
    time.sleep(2)
    assert page.table_results.is_visible(), 'table results not found'

    #6) В первых 5 результатах есть ссылка на tensor.ru
    assert page.results_links.get_text().index('tensor.ru') <= 5, 'tensor.ru not found in first 5 results'


def test_check_yandex_images(web_browser):
    """ yandex images. """

    #1)	Зайти на yandex.ru
    page = MainPage(web_browser)

    #2) Ссылка «Картинки» присутствует на странице
    assert page.images_link.get_attribute('href').split('?')[0] == 'https://yandex.ru/images/', 'images link not found'

    #3) Кликаем на ссылку
    page.images_link.click()

    #4) Проверить, что перешли на url https://yandex.ru/images/
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://yandex.ru/images/?utm_source=main_stripe_big', 'invalid current page'

    #5) Открыть 1 категорию, проверить что открылась, в поиске верный текст
    page.category_images.click()
    assert page.category_images.get_text() == page.category_search.get_attribute("value"), 'category does not match'

    # 6) Открыть 1 картинку , проверить что открылась
    src1 = page.firs_image_link.get_attribute("src").split('//')[1]
    page.firs_image.click()
    src2 = page.firs_image_link2.get_attribute("style").split('//')[1][:-3]
    assert src1 == src2, 'first picture not open'


    # 7) При нажатии кнопки вперед  картинка изменяется
    page.full_image.mov_to()
    page.wait_page_loaded()
    before_img = page.full_image.screenshot()
    time.sleep(1)
    page.button_next.click()
    page.wait_page_loaded()
    after_img = page.full_image.screenshot()
    assert before_img != after_img, 'image not changed'

    # 8) При нажатии кнопки назад картинка изменяется на изображение из шага 6. \
    # Необходимо проверить, что это то же изображение.
    time.sleep(1)
    page.button_prev.click()
    page.full_image.mov_to()
    page.wait_page_loaded()
    after_img = page.full_image.screenshot()
    assert before_img == after_img, 'image not match original'

