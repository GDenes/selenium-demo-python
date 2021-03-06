import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_webshop.pageobjects.common.GeneralWebShopPage import GeneralWebShopPage
from pages_webshop.pageobjects.orderpage.OrderPage import OrderPage
from utils.enums.BrowserEnum import BrowserEnum


class AddCartDialogBox(GeneralWebShopPage):
    productTitleLocator = '#layer_cart_product_title'
    productTitle: None

    colorAndSizeLocator = '#layer_cart_product_attributes'
    colorAndSize: None

    proceedToCheckoutButtonLocator = 'a.button-medium > span'
    proceedToCheckoutButton: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.productTitle = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.productTitleLocator)))

        # = driver.find_element(By.CSS_SELECTOR, self.productTitleLocator)
        self.proceedToCheckoutButton = driver.find_element(By.CSS_SELECTOR, self.proceedToCheckoutButtonLocator)
        self.colorAndSize = driver.find_element(By.CSS_SELECTOR, self.colorAndSizeLocator)

    @allure.step("Get title of product")
    def get_product_title_text(self):
        logging.info("Getting title of product")
        return self.productTitle.text

    @allure.step("Get color and size of product")
    def get_color_and_size_text(self):
        logging.info("Getting color and size of product")
        return self.colorAndSize.text

    @allure.step("Click to `Proceed to checkout` button")
    def click_proceed_to_checkout_button(self):
        logging.info("Clicking to `Proceed to checkout` button")
        self.proceedToCheckoutButton.click()
        return OrderPage(self.driver, self.browser)
