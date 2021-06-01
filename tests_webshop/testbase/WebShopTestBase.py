from pages_webshop.pageobjects.homepage.HomePage import HomePage
from pages_webshop.pageobjects.navigationbar.NavigationBar import NavigationBar
from tests_base.testbase.TestBase import TestBase


class WebShopTestBase(TestBase):
    
    BASE_URL = "http://automationpractice.com/index.php"

    def navigate_to_web_shop_page(self):
        super().get_driver().get(self.BASE_URL)
        return HomePage(self.get_driver(), self.get_browser())

    def get_navigation_bar(self):
        return NavigationBar(self.driver, self.browser)