import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.common.AbstractOrangeHrmPage import AbstractOrangeHrmPage
from utils.enums.BrowserEnum import BrowserEnum


class ExpenseClaimsPage(AbstractOrangeHrmPage):
    resultsTableLocator = '#claimRequestList'
    resultsTable: None

    tableResultRowsLocator = 'tr.dataRaw'
    tableResultRows: None

    iframeContentLocator = '#noncoreIframe'
    iframeContent: None

    totalListElementInCurrentPageLocator = '#frmList_ohrmListComponenttotal'
    totalListElementInCurrentPage: None

    def __init__(self, driver: webdriver, browser: BrowserEnum, userEnum: UserEnum):
        super().__init__(driver, browser, userEnum)
        self.resultsTable = driver.find_element(By.CSS_SELECTOR, self.resultsTableLocator)
        self.tableResultRows = driver.find_elements(By.CSS_SELECTOR, self.tableResultRowsLocator)
        self.iframeContent = driver.find_element(By.CSS_SELECTOR, self.iframeContentLocator)
        self.totalListElementInCurrentPage = driver.find_element(By.CSS_SELECTOR,
                                                                 self.totalListElementInCurrentPageLocator)

    @allure.step("Get all row from table")
    def get_table_result_rows(self):
        logging.info("Get all of rows from table")
        return self.tableResultRows

    @allure.step("Get total list element from table")
    def get_total_list_element_in_current_page(self):
        logging.info("Get total number of elements from table")
        return self.totalListElementInCurrentPage.text
