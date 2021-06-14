import logging
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_base.pageobjects.AbstractPage import AbstractPage
from pages_demoqa.pageobjects.tooltipspage.ToolTipsPage import ToolTipsPage
from utils.enums.BrowserEnum import BrowserEnum


class WidgetPage(AbstractPage):
    IMPLICIT_WAIT = 10

    toolTipsMenuItemLocator = '//span[text()="Tool Tips"]'
    toolTipsMenuItem = None

    bodyLocator = 'body'
    body = None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.body = driver.find_element(By.CSS_SELECTOR, self.bodyLocator)

    @allure.step("Go to `Tool Tips page`")
    def navigate_to_tool_tips_page(self):
        logging.info("Navigating to `Tool Tips` page")
        self.body.send_keys(Keys.PAGE_DOWN)
        WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.toolTipsMenuItemLocator))).click()
        return ToolTipsPage(self.driver, self.browser)
