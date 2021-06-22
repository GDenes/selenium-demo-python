import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_webshop.pageobjects.common.GeneralWebShopPage import GeneralWebShopPage
from utils.enums.BrowserEnum import BrowserEnum


class SignInPage(GeneralWebShopPage):
    pageHeadLocator = '.page-heading'
    pageHead: None

    createAccountButtonLocator = 'button#SubmitCreate > span'
    createAccountButton: None

    signInButtonLocator = 'button#SubmitLogin > span'
    signInButton: None

    currentStepLocator = 'li.step_current > span'
    currentStep: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.pageHead = WebDriverWait( self.driver, self.IMPLICIT_WAIT ).until(
            expected_conditions.visibility_of_element_located( (By.CSS_SELECTOR, self.pageHeadLocator)))
        self.createAccountButton = driver.find_element(By.CSS_SELECTOR, self.createAccountButtonLocator)
        self.signInButton = driver.find_element(By.CSS_SELECTOR, self.signInButtonLocator)
        self.currentStep = driver.find_element(By.CSS_SELECTOR, self.currentStepLocator)

    @allure.step("Get head text of page")
    def get_head_text(self):
        logging.info("Get head text of page")
        return self.pageHead.text

    @allure.step("Get current text of current step")
    def get_current_step_text(self):
        logging.info("Get current text of current step")
        return self.currentStep.text
