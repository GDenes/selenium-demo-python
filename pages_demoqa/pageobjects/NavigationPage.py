from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages_base.pageobjects.AbstractPage import AbstractPage
from pages_demoqa.pageobjects.elementspage.ElementsPage import ElementsPage
from utils.enums.BrowserEnum import BrowserEnum
from pages_base.waits.WaitForElementToAppear import WaitForElementToAppear


class NavigationPage(AbstractPage):
    elementsButtonLocator = '//h5[text()="Elements"]'
    elementsButton = None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.elementsButton = driver.find_element(By.XPATH, self.elementsButtonLocator)

    def navigate_to_elements_page(self):
        self.elementsButton.click()
        return ElementsPage(self.driver, self.browser)
