import unittest

import allure
from selenium import webdriver
from tests_base.driverfactory.DriverFactory import DriverFactory
from utils.enums.BrowserEnum import BrowserEnum


class TestBase(unittest.TestCase):
    driver: webdriver
    browser = BrowserEnum.CHROME

    remoteRun: bool = False

    remoteUrl = "http://localhost:4444/wd/hub"

    @allure.step("Create WebDriver")
    def setUp(self):
        if self.remoteRun:
            self.driver = DriverFactory().create_remote_driver(self.browser, self.remoteUrl)
        else:
            self.driver = DriverFactory().create_driver(self.browser)

        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver

    def get_browser(self):
        return self.browser
