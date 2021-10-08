#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time
from selenium.webdriver import ActionChains
from pages.elements import WebElement


class AdvancedWebElement(WebElement):

    def send_keys(self, keys, wait=2, clear=True):
        """ Send keys to the element. """

        keys = keys.replace('\n', '\ue007')

        element = self.find()

        if element:
            element.click()
            if clear:
                element.clear()
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def screenshot(self):
        element = self.find(timeout=0.1)
        return element.screenshot_as_png

    def mov_to(self):
        """ Moving the mouse to the middle of an element. """

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element(element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))
