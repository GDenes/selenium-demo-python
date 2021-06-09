import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_base.pageobjects.AbstractPage import AbstractPage
from utils.enums.BrowserEnum import BrowserEnum


class ToolTipsPage(AbstractPage):
    IMPLICIT_WAIT = 5
    PAUSE = 0.5

    toolTipButtonLocator = '#toolTipButton'
    toolTipButton = None

    toolTipTextFieldLocator = '#toolTipTextField'
    toolTipTextField = None

    toolTipTextLocator = '.tooltip-inner'
    toolTipText = None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.toolTipButton = driver.find_element(By.CSS_SELECTOR, self.toolTipButtonLocator)
        self.toolTipTextField = driver.find_element(By.CSS_SELECTOR, self.toolTipTextFieldLocator)

    @allure.step("Move cursor to button and get text of popup")
    def hover_tool_tip_button_and_get_text(self):
        return self.hover_web_element_get_tool_tip_text(self.toolTipButton)

    @allure.step("Move cursor to text field and get text of popup")
    def hover_tool_tip_text_field_and_get_text(self):
        return self.hover_web_element_get_tool_tip_text(self.toolTipTextField)

    def hover_web_element_get_tool_tip_text(self, web_element: webelement):
        action = ActionChains(self.driver)
        action.pause(self.PAUSE).perform()
        action.move_to_element(web_element).perform()
        action.pause(self.PAUSE).perform()

        element = WebDriverWait(self.driver, self.IMPLICIT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.toolTipTextLocator)))
        return element.text


