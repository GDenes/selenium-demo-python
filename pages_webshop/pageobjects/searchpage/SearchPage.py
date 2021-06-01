from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_webshop.pageobjects.common.GeneralWebShopPage import GeneralWebShopPage
from pages_webshop.pageobjects.quickview.QuickViewDialogBox import QuickViewDialogBox
from utils.enums.BrowserEnum import BrowserEnum


class SearchPage(GeneralWebShopPage):
    firstElementLocator = 'div.left-block > .product-image-container'
    firstElement = None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.firstElement = driver.find_element(By.CSS_SELECTOR, self.firstElementLocator)

    def clickFirstElement(self):
        self.firstElement.click()
        return QuickViewDialogBox(self.driver, self.browser)