from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_webshop.pageobjects.common.GeneralWebShopPage import GeneralWebShopPage
from pages_webshop.pageobjects.quickview.QuickViewDialogBox import QuickViewDialogBox
from utils.enums.BrowserEnum import BrowserEnum


class SearchPage(GeneralWebShopPage):
    firstElementLocator = 'div.left-block > .product-image-container'
    firstElement = None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.firstElement = WebDriverWait( self.driver, self.IMPLICIT_WAIT ).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.firstElementLocator)))

    def clickFirstElement(self):
        self.firstElement.click()
        return QuickViewDialogBox(self.driver, self.browser)