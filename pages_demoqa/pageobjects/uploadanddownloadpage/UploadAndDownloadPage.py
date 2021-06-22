import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_base.pageobjects.AbstractPage import AbstractPage
from utils.enums.BrowserEnum import BrowserEnum


class UploadAndDownloadPage(AbstractPage):
    IMPLICIT_WAIT = 2

    downloadButtonLocator = '#downloadButton'

    uploadFileLocator = '#uploadFile'

    filePathLocator = '#uploadedFilePath'
    filePath: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        WebDriverWait( self.driver, self.IMPLICIT_WAIT ).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.downloadButtonLocator)))
        self.uploadFile = driver.find_element(By.CSS_SELECTOR, self.uploadFileLocator)

    @allure.step("Upload file")
    def upload_sample_file(self, path):
        logging.info("Uploading file")
        self.uploadFile.send_keys(path)

    @allure.step("Get uploaded file path")
    def get_file_path_text(self):
        logging.info("Checking uploaded file path")
        return WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.filePathLocator))).text

