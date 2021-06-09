import logging
from abc import ABC

from selenium import webdriver

from utils.enums.BrowserEnum import BrowserEnum


class AbstractPage(ABC):
    IMPLICIT_WAIT = 30

    logger = logging.getLogger()

    driver: webdriver
    browser: BrowserEnum

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        self.driver = driver
        self.browser = browser
