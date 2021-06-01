from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_webshop.pageobjects.common.GeneralWebShopPage import GeneralWebShopPage
from utils.enums.BrowserEnum import BrowserEnum


class HomePage(GeneralWebShopPage):
    girlInTheRedDressLocator = 'ul#homefeatured [alt="Faded Short Sleeve T-shirts"]'
    girlInTheRedDress: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.girlInTheRedDress = driver.find_element(By.CSS_SELECTOR, self.girlInTheRedDressLocator)

    def get_girl_in_the_red_dress(self):
        return self.girlInTheRedDress
