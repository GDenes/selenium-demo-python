import logging

import allure

from pages_demoqa.pageobjects.NavigationPage import NavigationPage
from tests_base.testbase.TestBase import TestBase


class DemoQaTestBase(TestBase):
    BASE_URL = "https://demoqa.com/"

    @allure.step("Navigating to: " + BASE_URL)
    def navigate_to_tools_qa_page(self):
        super().get_driver().get(self.BASE_URL)
        return NavigationPage(self.get_driver(), self.get_browser())

