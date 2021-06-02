from pages_orangehrm.enums.PageEnum import PageEnum
from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.navigation.HeaderInterface import HeaderInterface
from tests_orangehrm.testbase.OrangeHrmTestBase import OrangeHrmTestBase


class UserListTests(OrangeHrmTestBase):
    USERNAME_VALUE_FROM_TABLE = "span"
    ROW_PER_PAGE = 50

    headerInterface: HeaderInterface

    def test_row_per_page_test(self):
        login_page = self.navigate_to_login_page()
        self.headerInterface = login_page.login(UserEnum.SYSTEM_ADMIN)

        user_page = self.headerInterface.navigate_to(PageEnum.USER_PAGE)
