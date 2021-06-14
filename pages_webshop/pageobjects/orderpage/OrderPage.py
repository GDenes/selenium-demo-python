import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_webshop.pageobjects.common.GeneralWebShopPage import GeneralWebShopPage
from pages_webshop.pageobjects.signinpage.SignInPage import SignInPage
from utils.enums.BrowserEnum import BrowserEnum


class OrderPage(GeneralWebShopPage):
    totalProductLocator = '#total_product'
    totalProduct: None

    totalShippingLocator = "#total_shipping"
    totalShipping: None

    totalTaxLocator = "#total_tax"
    totalTax: None

    totalPriceLocator = "#total_price"
    totalPrice: None

    proceedToCheckoutButtonLocator = 'a.standard-checkout > span'
    proceedToCheckoutButton: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.totalProduct = driver.find_element(By.CSS_SELECTOR, self.totalProductLocator)
        self.totalShipping = driver.find_element(By.CSS_SELECTOR, self.totalShippingLocator)
        self.totalTax = driver.find_element(By.CSS_SELECTOR, self.totalTaxLocator)
        self.totalPrice = driver.find_element(By.CSS_SELECTOR, self.totalPriceLocator)
        self.proceedToCheckoutButton = driver.find_element(By.CSS_SELECTOR, self.proceedToCheckoutButtonLocator)

    @allure.step("Click to `Proceed to checkout` button")
    def click_proceed_checkout_button(self):
        logging.info("Clicking to `Proceed to checkout` button")
        self.proceedToCheckoutButton.click()
        return SignInPage(self.driver, self.browser)

    @allure.step("Get `Total product` text value")
    def get_total_product_text(self):
        logging.info("Get `Total product` text value")
        return self.totalProduct.text

    @allure.step("Get value of `Total shipping`")
    def get_total_shipping_text(self):
        logging.info("Get value of `Total shipping`")
        return self.totalShipping.text

    @allure.step("Get value of `Total tax`")
    def get_total_tax_text(self):
        logging.info("Get value of `Total tax`")
        return self.totalTax.text

    @allure.step("Get value of `Total price`")
    def get_total_price_text(self):
        logging.info("Get value of `Total price`")
        return self.totalPrice.text
