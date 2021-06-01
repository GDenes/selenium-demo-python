from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages_webshop.enums.ColorEnum import ColorEnum
from pages_webshop.enums.SizeEnum import SizeEnum
from pages_webshop.pageobjects.common.GeneralWebShopPage import GeneralWebShopPage
from pages_webshop.pageobjects.fadedshortpage.AddCartDialogBox import AddCartDialogBox
from utils.enums.BrowserEnum import BrowserEnum


class FadedShortPage(GeneralWebShopPage):
    increaseQuantityButtonLocator = '.icon-plus'
    increaseQuantityButton: None

    sizeInputFieldLocator = '.attribute_select'
    sizeInputField: None

    blueColorLocator = '[name="Blue"]'
    blueColor: None

    orangeColorLocator = '[name="Orange"]'
    orangeColor: None

    addToCartButtonLocator = 'button[name="Submit"] > span'
    addToCartButton: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.increaseQuantityButton = driver.find_element(By.CSS_SELECTOR, self.increaseQuantityButtonLocator)
        self.sizeInputField = driver.find_element(By.CSS_SELECTOR, self.sizeInputFieldLocator)
        self.addToCartButton = driver.find_element(By.CSS_SELECTOR, self.addToCartButtonLocator)
        self.blueColor = driver.find_element(By.CSS_SELECTOR, self.blueColorLocator)
        self.orangeColor = driver.find_element(By.CSS_SELECTOR, self.orangeColorLocator)

    def increase_quantity_number(self):
        self.increaseQuantityButton.click()

    def select_size(self, size: SizeEnum):
        select = Select(self.sizeInputField)
        select.select_by_visible_text(size.value)

    def click_add_cart_button(self):
        self.addToCartButton.click()
        return AddCartDialogBox(self.driver, self.browser)

    def select_color(self, color: ColorEnum):
        if color.value == ColorEnum.BLUE.value:
            self.blueColor.click()
        elif color.value == ColorEnum.ORANGE.value:
            self.orangeColor.click()
