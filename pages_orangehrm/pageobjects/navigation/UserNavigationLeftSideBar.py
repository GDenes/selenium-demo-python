from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_orangehrm.enums.PageEnum import PageEnum
from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.navigation.AbstractNavigationLeftSideBar import AbstractNavigationLeftSideBar
from utils.enums.BrowserEnum import BrowserEnum


class UserNavigationLeftSideBar(AbstractNavigationLeftSideBar):
    myInfoMenuItemLocator = '#menu_pim_viewMyDetails'

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.myInfoMenuItem = driver.find_element(By.CSS_SELECTOR, self.myInfoMenuItemLocator)

    def navigate_to(self, pageEnum: PageEnum):
        if pageEnum == PageEnum.MY_INFO_PAGE:
            return self.navigate_to_my_info_page()
        elif pageEnum == PageEnum.EXPENSE_CLAIMS_PAGE:
            return self.navigate_to_expense_claims_page()

    def navigate_to_my_info_page(self):
        self.myInfoMenuItem.click()
        from pages_orangehrm.pageobjects.myinfo.MyInfoPage import MyInfoPage
        return MyInfoPage.MyInfoPage(self.driver, self.browser, UserEnum.ESS_USER)

    def navigate_to_expense_claims_page(self): # TODO implement method
        return self
