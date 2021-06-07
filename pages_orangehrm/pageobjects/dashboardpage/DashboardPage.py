from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.common.AbstractOrangeHrmPage import AbstractOrangeHrmPage
from utils.enums.BrowserEnum import BrowserEnum


class DashboardPage(AbstractOrangeHrmPage):
    pageTitleLocator = '.page-title'
    pageTitle: None

    pageContentLocator = '#content'
    pageContent: None

    def __init__(self, driver: webdriver, browser: BrowserEnum, userEnum: UserEnum):
        super().__init__(driver, browser, userEnum)
        self.pageTitle = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.pageTitleLocator)))
        # self.pageTitle = driver.find_element(By.CSS_SELECTOR, self.pageTitleLocator)

        self.pageContent = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.pageContentLocator)))
        # self.pageContent = driver.find_element(By.CSS_SELECTOR, self.pageContentLocator)
