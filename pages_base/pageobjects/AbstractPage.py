import logging
from abc import ABC

from selenium import webdriver

from utils.enums.BrowserEnum import BrowserEnum

formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s~module:%(module)s')

file_handler = logging.FileHandler("logfile.log")
file_handler.setLevel(logging.WARN)
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)


class AbstractPage(ABC):
    IMPLICIT_WAIT = 30

    driver: webdriver
    browser: BrowserEnum

    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        self.driver = driver
        self.browser = browser
