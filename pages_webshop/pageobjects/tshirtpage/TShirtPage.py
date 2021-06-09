import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_webshop.pageobjects.common.GeneralWebShopPage import GeneralWebShopPage
from pages_webshop.pageobjects.fadedshortpage.FadedShortPage import FadedShortPage
from utils.enums.BrowserEnum import BrowserEnum


class TShirtPage(GeneralWebShopPage):
    fadedShortItemLocator = '.product-name[title="Faded Short Sleeve T-shirts"]'
    fadedShortItem: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.fadedShortItem = driver.find_element(By.CSS_SELECTOR, self.fadedShortItemLocator)

    @allure.step("Click to `Faded short item`")
    def click_faded_short_item(self):
        logging.info("`Clicking to `Faded short item`")
        self.fadedShortItem.click()

        return FadedShortPage(self.driver, self.browser)
