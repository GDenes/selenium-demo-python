from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_base.pageobjects.AbstractPage import AbstractPage
from pages_demoqa.pageobjects.dynamicpropertiespage.DynamicPropertiesPage import DynamicPropertiesPage
from pages_demoqa.pageobjects.uploadanddownloadpage.UploadAndDownloadPage import UploadAndDownloadPage
from utils.enums.BrowserEnum import BrowserEnum


class ElementsPage(AbstractPage):
    dynamicPropertiesLocator = '//span[text()="Dynamic Properties"]'
    dynamicProperties = None

    uploadAndDownloadLocator = '//span[text()="Upload and Download"]'
    uploadAndDownload: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.dynamicProperties = driver.find_element(By.XPATH, self.dynamicPropertiesLocator)
        self.uploadAndDownload = driver.find_element(By.XPATH, self.uploadAndDownloadLocator)

    def navigate_to_dynamic_properties_page(self):
        self.dynamicProperties.click()
        return DynamicPropertiesPage(self.driver, self.browser)

    def navigate_to_upload_and_download_page(self):
        self.uploadAndDownload.click()
        return UploadAndDownloadPage(self.driver, self.browser)
