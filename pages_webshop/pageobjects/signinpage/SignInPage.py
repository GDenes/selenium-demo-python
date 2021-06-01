from selenium import webdriver
from selenium.webdriver.common.by import By

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
        self.pageHead = driver.find_element(By.CSS_SELECTOR, self.pageHeadLocator)
        self.createAccountButton = driver.find_element(By.CSS_SELECTOR, self.createAccountButtonLocator)
        self.signInButton = driver.find_element(By.CSS_SELECTOR, self.signInButtonLocator)
        self.currentStep = driver.find_element(By.CSS_SELECTOR, self.currentStepLocator)

    def get_head_text(self):
        return self.pageHead.text

    def get_current_step_text(self):
        return self.currentStep.text
