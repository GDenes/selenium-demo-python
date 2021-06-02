from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.common.AbstractOrangeHrmPage import AbstractOrangeHrmPage
from utils.enums.BrowserEnum import BrowserEnum


class DashboardPage(AbstractOrangeHrmPage):
    pageTitleLocator = 'page-title'
    pageTitle: None

    pageContentLocator = '#content'
    pageContent: None

    def __init__(self, driver: webdriver, browser: BrowserEnum, userEnum: UserEnum):
        super().__init__(driver, browser)
        self.pageTitle = driver.find_element(By.CSS_SELECTOR, self.pageTitleLocator)
        self.pageContent = driver.find_element(By.CSS_SELECTOR, self.pageContentLocator)
