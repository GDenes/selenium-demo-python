import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_base.pageobjects.AbstractPage import AbstractPage
from pages_demoqa.pageobjects.droppablepage.DroppablePage import DroppablePage
from utils.enums.BrowserEnum import BrowserEnum


class InteractionPage(AbstractPage):

    droppableMenuItemLocator = '//span[text()="Droppable"]'
    droppableMenuItem = None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.droppableMenuItem = driver.find_element(By.XPATH, self.droppableMenuItemLocator)

    @allure.step("Go to `Droppable page`")
    def get_droppable_page(self):
        logging.info("Navigating to `Droppable` page")
        self.droppableMenuItem.click()
        return DroppablePage(self.driver, self.browser)