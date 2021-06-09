import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_base.pageobjects.AbstractPage import AbstractPage
from pages_demoqa.pageobjects.elementspage.ElementsPage import ElementsPage
from pages_demoqa.pageobjects.interactionpage.InteractionPage import InteractionPage
from pages_demoqa.pageobjects.widgetpage.WidgetPage import WidgetPage
from utils.enums.BrowserEnum import BrowserEnum


class NavigationPage(AbstractPage):
    elementsButtonLocator = '//h5[text()="Elements"]'
    elementsButton = None

    interactionsButtonLocator = '//h5[text()="Interactions"]'
    interactionsButton = None

    widgetsButtonLocator = '//h5[text()="Widgets"]'
    widgetsButton = None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.elementsButton = driver.find_element(By.XPATH, self.elementsButtonLocator)
        self.interactionsButton = driver.find_element(By.XPATH, self.interactionsButtonLocator)
        self.widgetsButton = driver.find_element(By.XPATH, self.widgetsButtonLocator)

    @allure.step("Go to `Elements page`")
    def navigate_to_elements_page(self):
        self.elementsButton.click()
        return ElementsPage(self.driver, self.browser)

    @allure.step("Go to `Interactive page`")
    def navigate_to_interactions_page(self):
        self.interactionsButton.click()
        return InteractionPage(self.driver, self.browser)

    @allure.step("Go to `Widget page`")
    def navigate_to_widget_page(self):
        self.widgetsButton.click()
        return WidgetPage(self.driver, self.browser)
