from typing import cast

from pages_orangehrm.enums.PageEnum import PageEnum
from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.myinfo.MyInfoPage import MyInfoPage
from pages_orangehrm.pageobjects.navigation.HeaderInterface import HeaderInterface
from tests_orangehrm.testbase.OrangeHrmTestBase import OrangeHrmTestBase


class MyInfoTests(OrangeHrmTestBase):
    FIRST_NAME = 'Linda'
    MIDDLE_NAME = 'Jane'
    LAST_NAME = 'Anderson'
    EMPLOYEE_ID = '1000'
    DATE_OF_BIRTH = 'Wed, 05 Jun 1985'
    MARTIAL_STATUS = 'Married'
    GENDER = 'Female'
    NATIONALITY = 'Canadian'
    DRIVER_LICENSE_EXP_DATE = 'Fri, 06 Mar 2020'

    header_interface: HeaderInterface

    def test_my_info(self):
        login_page = self.navigate_to_login_page()
        dashboard_page = login_page.login(UserEnum.ESS_USER)

        self.header_interface = dashboard_page.navigate_to(PageEnum.MY_INFO_PAGE)

        self.compare_test_results()

    def compare_test_results(self):
        self.assertEqual(self.FIRST_NAME, cast(MyInfoPage, self.header_interface).get_first_name_field_value(),
                         'Incorrect first name value.')
        self.assertEqual(self.MIDDLE_NAME, cast(MyInfoPage, self.header_interface).get_middle_name_value(),
                         'Incorrect middle name value.')
        self.assertEqual(self.LAST_NAME, cast(MyInfoPage, self.header_interface).get_last_name_value(),
                         'Incorrect last name value.')
        self.assertEqual(self.EMPLOYEE_ID, cast(MyInfoPage, self.header_interface).get_employee_id_value(),
                         'Incorrect employee id value.')
        self.assertEqual(self.DATE_OF_BIRTH, cast(MyInfoPage, self.header_interface).get_employee_birthday_value(),
                         'Incorrect date of birth value.')
        self.assertEqual(self.MARTIAL_STATUS, cast(MyInfoPage, self.header_interface).get_marital_status_value(),
                         'Incorrect martial status value.')
        self.assertEqual(self.GENDER, cast(MyInfoPage, self.header_interface).get_employee_gender_value(),
                         'Incorrect gender value.')
        self.assertEqual(self.NATIONALITY, cast(MyInfoPage, self.header_interface).get_nationality_code_value(),
                         'Incorrect nationality value.')
        self.assertEqual(self.DRIVER_LICENSE_EXP_DATE, cast(MyInfoPage, self.header_interface)
                         .get_driver_license_exp_date_value(), 'Incorrect driver license exp date value.')
