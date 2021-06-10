import string

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from pages_orangehrm.pageobjects.loginpage.LoginPage import LoginPage
from tests_base.testbase.TestBase import TestBase


class OrangeHrmTestBase(TestBase):
    BASE_URL = 'https://orangehrm-demo-6x.orangehrmlive.com'

    @allure.step("Navigate to Orange HRM login page")
    def navigate_to_login_page(self):
        super().get_driver().get(self.BASE_URL)
        return LoginPage(self.get_driver(), self.get_browser())

    @allure.step("Print users from table")
    def print_all_username_to_terminal(self, rows, filterTagName: string):
        row: webelement
        for row in rows:
            print(row.find_element(By.TAG_NAME, filterTagName).text)
