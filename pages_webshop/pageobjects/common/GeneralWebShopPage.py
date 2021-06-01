from selenium import webdriver

from pages_base.pageobjects.AbstractPage import AbstractPage
from utils.enums.BrowserEnum import BrowserEnum


class GeneralWebShopPage(AbstractPage):

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
