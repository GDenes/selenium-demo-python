from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_base.pageobjects.AbstractPage import AbstractPage
from utils.enums.BrowserEnum import BrowserEnum


class QuickViewDialogBox(AbstractPage):
    IMPLICIT_WAIT = 15

    descriptionLocator = '#short_description_content'
    description: None

    iframeLocator = '.fancybox-iframe'
    iframe: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.iframe = driver.find_element(By.CSS_SELECTOR, self.iframeLocator)

    def get_description_text(self):
        self.driver.switch_to.frame(self.iframe)

        return WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.descriptionLocator))).text
