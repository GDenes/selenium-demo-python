import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_base.pageobjects.AbstractPage import AbstractPage
from utils.enums.BrowserEnum import BrowserEnum


class QuickViewDialogBox(AbstractPage):
    IMPLICIT_WAIT = 15

    descriptionLocator = '#short_description_content'
    description: None

    iframeLocator = '.fancybox-iframe'
    iframe: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.iframe = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
             expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.iframeLocator)))

    @allure.step("Get short description of product")
    def get_description_text(self):
        logging.info("Get short description of product")
        self.driver.switch_to.frame(self.iframe)

        return WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.descriptionLocator))).text
