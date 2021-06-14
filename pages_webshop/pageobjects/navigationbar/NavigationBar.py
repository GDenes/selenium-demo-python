import logging

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_base.pageobjects.AbstractPage import AbstractPage
from pages_webshop.pageobjects.searchpage.SearchPage import SearchPage
from pages_webshop.pageobjects.tshirtpage.TShirtPage import TShirtPage
from utils.enums.BrowserEnum import BrowserEnum


class NavigationBar(AbstractPage):
    womenButtonLocator = '.sf-with-ul[title="Women"]'
    womenButton: None

    dressButtonLocator = 'ul.sf-menu > li > [title="Dresses"]'
    dressButton: None

    tShirtButtonLocator = 'ul.sf-menu .submenu-container [title="T-shirts"]'
    tShirtButton: None

    searchFieldLocator = '#search_query_top'
    searchField: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.womenButton = driver.find_element(By.CSS_SELECTOR, self.womenButtonLocator)
        self.dressButton = driver.find_element(By.CSS_SELECTOR, self.dressButtonLocator)
        self.searchField = driver.find_element(By.CSS_SELECTOR, self.searchFieldLocator)

    @allure.step("Fill input field with {searchText}")
    def fill_input_field_and_search(self, searchText):
        logging.info("Searching for `{}`", searchText)
        self.searchField.send_keys(searchText)
        self.searchField.send_keys(Keys.ENTER)

        return SearchPage(self.driver, self.browser)

    @allure.step("Move cursor to `Women button` and click to popup")
    def hover_and_click_t_shirt_button(self):
        logging.info("Navigating to `T-shirts` page")
        action = ActionChains(self.driver)
        action.move_to_element(self.womenButton).perform()
        WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.tShirtButtonLocator)))
        return TShirtPage(self.driver, self.browser)