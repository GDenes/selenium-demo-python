from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class WaitForElementToAppear:
    driver: webdriver
    BASIC_WAIT: int = 30

    def __init__(self, driver: webdriver):
        self.driver = driver

    def apply(self, element: WebElement):
        wait = WebDriverWait(self.driver, self.BASIC_WAIT)
        return wait.until(expected_conditions.visibility_of_element_located(element))

