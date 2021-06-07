from typing import cast

from pages_orangehrm.enums.PageEnum import PageEnum
from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.expenseclaimspage.ExpenseClaimsPage import ExpenseClaimsPage
from tests_orangehrm.testbase.OrangeHrmTestBase import OrangeHrmTestBase


class EmployeeClaimsTests(OrangeHrmTestBase):
    EXPENSE_CLAIMS_ID_TAG_NAME = 'a'

    def test_expense_claims(self):
        login_page = self.navigate_to_login_page()
        dashboard_page = login_page.login(UserEnum.SYSTEM_ADMIN)
        header_interface = cast(ExpenseClaimsPage, dashboard_page.navigate_to(PageEnum.EXPENSE_CLAIMS_PAGE))
        size = header_interface.get_total_list_element_in_current_page()

        self.print_all_username_to_terminal(header_interface.get_table_result_rows(), self.EXPENSE_CLAIMS_ID_TAG_NAME)

        self.assertEquals(size, len(header_interface.get_table_result_rows()), 'Incorrect row number in table')

    def test_failure(self):
        login_page = self.navigate_to_login_page()
        dashboard_page = login_page.login(UserEnum.SYSTEM_ADMIN)
        header_interface = cast(ExpenseClaimsPage, dashboard_page.navigate_to(PageEnum.EXPENSE_CLAIMS_PAGE))
        header_interface.navigate_to(PageEnum.USER_PAGE)
        self.assertEqual(1, 0, 'This is one failure example test')
