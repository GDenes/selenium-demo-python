import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_base.pageobjects.AbstractPage import AbstractPage
from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.dashboardpage.DashboardPage import DashboardPage
from utils.enums.BrowserEnum import BrowserEnum


class LoginPage(AbstractPage):
    usernameInputFieldLocator = 'txtUsername'
    usernameInputField: None

    passwordInputFieldLocator = 'txtPassword'
    passwordInputField: None

    loginButtonLocator = 'btnLogin'
    loginButton: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.usernameInputField = driver.find_element(By.ID, self.usernameInputFieldLocator)
        self.passwordInputField = driver.find_element(By.ID, self.passwordInputFieldLocator)
        self.loginButton = driver.find_element(By.ID, self.loginButtonLocator)

    @allure.step("Login to page {userEnum}")
    def login(self, userEnum: UserEnum):
        logging.info("Entering login credentials")
        self.clear_input_field()
        self.usernameInputField.send_keys(userEnum.user_name)
        self.passwordInputField.send_keys(userEnum.password)

        logging.info("Clicking to login button")
        self.loginButton.click()
        
        return DashboardPage(self.driver, self.browser, userEnum)

    def clear_input_field(self):
        logging.info("Clearing credentials input fields")
        self.usernameInputField.clear()
        self.passwordInputField.clear()
