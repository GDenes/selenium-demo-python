import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.common.AbstractOrangeHrmPage import AbstractOrangeHrmPage
from utils.enums.BrowserEnum import BrowserEnum


class UserPage(AbstractOrangeHrmPage):
    GET_ATTRIBUTE_VALUE = 'value'

    usersTableLocator = '#systemUserDiv'
    usersTable: None

    userListSizeLocator = 'input.select-dropdown'
    userListSize: None

    pageTitleLocator = '.page-title'
    pageTitle: None

    userRowElementsLocator = '.highlight > tbody:nth-child(3) > tr'
    userRowElements: None

    firstRowInTableLocator = '.highlight > tbody:nth-child(3) > tr:nth-child(1)'
    firstRowInTable: None

    def __init__(self, driver: webdriver, browser: BrowserEnum, userEnum: UserEnum):
        super().__init__(driver, browser, userEnum)
        self.pageTitle = driver.find_element(By.CSS_SELECTOR, self.pageTitleLocator)

        self.userListSize = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.userListSizeLocator)))
        # self.userListSize = driver.find_element(By.CSS_SELECTOR, self.userListSizeLocator)

        self.userRowElements = driver.find_element(By.CSS_SELECTOR, self.userRowElementsLocator)
        self.firstRowInTable = driver.find_element(By.CSS_SELECTOR, self.firstRowInTableLocator)

    @allure.step("Get user list table size")
    def get_user_list_size(self):
        return self.userListSize.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get all username from data table")
    def get_all_username(self):
        return self.userRowElements


