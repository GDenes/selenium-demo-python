from abc import ABC

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_base.pageobjects.AbstractPage import AbstractPage
from pages_orangehrm.pageobjects.navigation.HeaderInterface import HeaderInterface
from utils.enums.BrowserEnum import BrowserEnum


class AbstractNavigationLeftSideBar(AbstractPage, ABC, HeaderInterface):
    menuItemListLocator = 'menu-content'
    menuItemList: None

    expenseMenuItemLocator = 'menu_expense_viewExpenseModule'
    expenseMenuItem: None

    claimsSubMenuItemLocator = 'menu_expense_Claims'
    claimsSubMenuItem: None

    underClaimsEmployeeSubMenuItemLocator = 'menu_expense_viewExpenseClaims'
    underClaimsEmployeeSubMenuItem: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.menuItemList = driver.find_element(By.ID, self.menuItemListLocator)
        self.expenseMenuItem = driver.find_element(By.ID, self.expenseMenuItemLocator)
        self.underClaimsEmployeeSubMenuItem = driver.find_element(By.ID, self.underClaimsEmployeeSubMenuItemLocator)