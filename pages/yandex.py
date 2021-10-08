#!/usr/bin/python3
# -*- encoding=utf8 -*-

from pages.advanced_element import AdvancedWebElement
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://yandex.ru/'

        super().__init__(web_driver, url)

    search = AdvancedWebElement(id='text')

    suggest = WebElement(class_name='mini-suggest__popup_visible')

    table_results = WebElement(xpath='//*[@aria-label="Результаты поиска"]')

    results_links = ManyWebElements(xpath='//*[@aria-label="Результаты поиска"]/li//div/div[1]/div[1]/a/b')

    images_link = WebElement(xpath='/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a')

    category_images = WebElement(xpath='/html/body/div[3]/div[2]/div[1]/div/div/div[1]/a/div[2]')
    category_search = WebElement(xpath='/html/body/header/div/div[1]/div[2]/form/div[1]/span/span/input')

    firs_image = WebElement(class_name='serp-item__link')
    firs_image_link = WebElement(xpath='/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a/img')

    firs_image_link2 = WebElement(class_name='MMThumbImage-Image')

    button_next = AdvancedWebElement(class_name='CircleButton_type_next')
    button_prev = WebElement(class_name='CircleButton_type_prev')

    full_image = AdvancedWebElement(class_name='MMImage-Preview')

#python -m pytest -v --driver Chrome --driver-path ~/chrome tests/test_smoke_yandex.py
