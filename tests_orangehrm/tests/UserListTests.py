from typing import cast

import allure

from pages_orangehrm.enums.PageEnum import PageEnum
from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.navigation.HeaderInterface import HeaderInterface
from tests_orangehrm.testbase.OrangeHrmTestBase import OrangeHrmTestBase


class UserListTests(OrangeHrmTestBase):
    USERNAME_VALUE_FROM_TABLE = 'span'
    ROW_PER_PAGE = 50

    headerInterface: HeaderInterface

    @allure.story("Testing table row number")
    @allure.description("In this case, test user list")
    def test_row_per_page(self):
        login_page = self.navigate_to_login_page()
        dashboard_page = login_page.login(UserEnum.SYSTEM_ADMIN)

        from pages_orangehrm.pageobjects.userpage.UserPage import UserPage
        user_page = cast(UserPage, self.headerInterface.navigate_to(PageEnum.USER_PAGE))
        # self.header_interface = dashboard_page.navigate_to(PageEnum.MY_INFO_PAGE)

        self.print_all_username_to_terminal(self.header_interface.get_all_username(), self.USERNAME_VALUE_FROM_TABLE)

        self.assertEqual(self.ROW_PER_PAGE, user_page.get_user_list_size(), 'User per page number not valid')
        self.assertEqual(self.ROW_PER_PAGE, user_page.get_all_username().size, 'User per page not valid')
