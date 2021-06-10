import unittest

import allure
from selenium import webdriver
from tests_base.driverfactory.DriverFactory import DriverFactory
from utils.enums.BrowserEnum import BrowserEnum


class TestBase(unittest.TestCase):
    driver: webdriver
    browser = BrowserEnum.CHROME

    @allure.step("Create WebDriver")
    def setUp(self):
        self.driver = DriverFactory().create_driver(self.browser)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def get_driver(self):
        return self.driver

    def get_browser(self):
        return self.browser
