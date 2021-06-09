import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.common.AbstractOrangeHrmPage import AbstractOrangeHrmPage
from utils.enums.BrowserEnum import BrowserEnum


class MyInfoPage(AbstractOrangeHrmPage):
    GET_ATTRIBUTE_VALUE = 'value'

    firstNameFieldLocator = '#firstName'
    middleNameFieldLocator = '#middleName'
    lastNameFieldLocator = '#lastName'
    employeeIdFieldLocator = '#employeeId'
    otherIdLocator = '#otherId'
    empBirthdayFieldLocator = '#emp_birthday'
    empMaritalStatusFieldLocator = '#emp_marital_status_inputfileddiv > div > input.select-dropdown'
    empGenderFieldLocator = '#emp_gender_inputfileddiv > div > input.select-dropdown'
    nationalityCodeInputLocator = '#nation_code_inputfileddiv > div > input.select-dropdown'
    driverLicenseNoFieldLocator = '#licenseNo'
    driverLicenseExpDateFieldLocator = '#emp_dri_lice_exp_date'

    def __init__(self, driver: webdriver, browser: BrowserEnum, userEnum: UserEnum):
        super().__init__(driver, browser, userEnum)
        self.firstNameField = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.firstNameFieldLocator)))

        self.firstNameField = driver.find_element(By.CSS_SELECTOR, self.firstNameFieldLocator)
        self.middleNameField = driver.find_element(By.CSS_SELECTOR, self.middleNameFieldLocator)
        self.lastNameField = driver.find_element(By.CSS_SELECTOR, self.lastNameFieldLocator)
        self.employeeIdField = driver.find_element(By.CSS_SELECTOR, self.employeeIdFieldLocator)
        self.otherId = driver.find_element(By.CSS_SELECTOR, self.otherIdLocator)
        self.empBirthdayField = driver.find_element(By.CSS_SELECTOR, self.empBirthdayFieldLocator)
        self.empMaritalStatusField = driver.find_element(By.CSS_SELECTOR, self.empMaritalStatusFieldLocator)
        self.empGenderField = driver.find_element(By.CSS_SELECTOR, self.empGenderFieldLocator)
        self.nationalityCodeInput = driver.find_element(By.CSS_SELECTOR, self.nationalityCodeInputLocator)
        self.driverLicenseNoField = driver.find_element(By.CSS_SELECTOR, self.driverLicenseNoFieldLocator)
        self.driverLicenseExpDateField = driver.find_element(By.CSS_SELECTOR, self.driverLicenseExpDateFieldLocator)

    @allure.step("Get fistname value")
    def get_first_name_field_value(self):
        return self.firstNameField.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get middlename value")
    def get_middle_name_value(self):
        return self.middleNameField.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get lastname value")
    def get_last_name_value(self):
        return self.lastNameField.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get employee id value")
    def get_employee_id_value(self):
        return self.employeeIdField.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get employee id value")
    def get_other_id_value(self):
        return self.otherId.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get birthday value")
    def get_employee_birthday_value(self):
        return self.empBirthdayField.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get marital status value")
    def get_marital_status_value(self):
        return self.empMaritalStatusField.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get employee gender value")
    def get_employee_gender_value(self):
        return self.empGenderField.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get nationality value")
    def get_nationality_code_value(self):
        return self.nationalityCodeInput.get_attribute(self.GET_ATTRIBUTE_VALUE)

    @allure.step("Get driver license value")
    def get_driver_license_exp_date_value(self):
        return self.driverLicenseExpDateField.get_attribute(self.GET_ATTRIBUTE_VALUE)
