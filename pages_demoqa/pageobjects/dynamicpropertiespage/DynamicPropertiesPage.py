from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages_base.pageobjects.AbstractPage import AbstractPage
from utils.enums.BrowserEnum import BrowserEnum


class DynamicPropertiesPage(AbstractPage):
    IMPLICIT_WAIT: int = 10
    DANGER_CLASS_NAME = 'text-danger'

    enableAfterSelector = '#enableAfter'
    enableAfter: WebElement = None

    colorChangeSelector = '#colorChange'
    colorChange = None

    visibleAfterSelector = '#visibleAfter'
    visibleAfter = None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.enableAfter = driver.find_element(By.CSS_SELECTOR, self.enableAfterSelector)
        self.colorChange = driver.find_element(By.CSS_SELECTOR, self.colorChangeSelector)
        self.visibleAfter = driver.find_element(By.CSS_SELECTOR, self.visibleAfterSelector)

    def will_enabled_button(self):
        return WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.enableAfterSelector))).is_enabled()

    # In return, if no result find method return -1, if have return start index of
    def color_changed_button(self):
        class_name = self.colorChange.get_attribute('class')
        return class_name.find(self.DANGER_CLASS_NAME) != -1

    def visible_button(self):
        element = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.visibleAfterSelector)))
        return element.is_displayed()
