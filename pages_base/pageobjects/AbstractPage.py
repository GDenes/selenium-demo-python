from selenium import webdriver

from utils.enums.BrowserEnum import BrowserEnum


class AbstractPage:
    driver: webdriver
    browser: BrowserEnum

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        self.driver = driver
        self.browser = browser
