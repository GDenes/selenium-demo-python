from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_base.pageobjects.AbstractPage import AbstractPage
from utils.enums.BrowserEnum import BrowserEnum


class WidgetPage(AbstractPage):
    IMPLICIT_WAIT = 2

    uploadFileLocator = '#uploadFile'
    uploadFile = None

    filePathLocator = '#uploadedFilePath'
    filePath: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.uploadFile = driver.find_element(By.CSS_SELECTOR, self.uploadFileLocator)