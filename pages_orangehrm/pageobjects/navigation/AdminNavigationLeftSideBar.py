import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_orangehrm.enums.PageEnum import PageEnum
from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.navigation.AbstractNavigationLeftSideBar import AbstractNavigationLeftSideBar
from utils.enums.BrowserEnum import BrowserEnum


class AdminNavigationLeftSideBar(AbstractNavigationLeftSideBar):
    adminModuleButtonLocator = '#menu_admin_viewAdminModule'
    adminModuleButton: None

    userModuleButtonLocator = '#menu_admin_UserManagement'
    userModuleButton: None

    userButtonLocator = '#menu_admin_viewSystemUsers'
    userButton: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.userButton = self.driver.find_element(By.CSS_SELECTOR, self.userButtonLocator)
        # self.adminModuleButton = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
        #     expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.adminModuleButtonLocator)))
        # self.adminModuleButton = driver.find_element(By.CSS_SELECTOR, self.adminModuleButtonLocator)

        self.userButton = driver.find_element(By.CSS_SELECTOR, self.userButtonLocator)

    def navigate_to(self, pageEnum: PageEnum):
        if pageEnum == PageEnum.USER_PAGE:
            return self.navigate_to_user_page()
        # elif pageEnum == PageEnum.EXPENSE_CLAIMS_PAGE:
        #     return self.navigate_to_expense_claims_page()

    @allure.step("Navigate to `User page`")
    def navigate_to_user_page(self):
        self.click_to_admin_item()
        self.click_to_user_management_item()
        self.userButton = self.driver.find_element(By.CSS_SELECTOR, self.userButtonLocator)
        self.userButton.click()
        from pages_orangehrm.pageobjects.userpage.UserPage import UserPage
        return UserPage(self.driver, self.browser, UserEnum.SYSTEM_ADMIN)

    def click_to_admin_item(self):
        self.adminModuleButton = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.adminModuleButtonLocator)))
        self.adminModuleButton.click()

    def click_to_user_management_item(self):
        self.userModuleButton = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.userModuleButtonLocator)))
        self.userModuleButton.click()
