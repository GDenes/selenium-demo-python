from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_base.pageobjects.AbstractPage import AbstractPage
from utils.enums.BrowserEnum import BrowserEnum


class DroppablePage(AbstractPage):
    droppableComponentLocator = '#droppable'
    droppableComponent = None

    draggableComponentLocator = '#draggable'
    draggableComponent: None

    def __init__(self, driver: webdriver, browser: BrowserEnum):
        super().__init__(driver, browser)
        self.droppableComponent = driver.find_element(By.CSS_SELECTOR, self.droppableComponentLocator)
        self.draggableComponent = driver.find_element(By.CSS_SELECTOR, self.draggableComponentLocator)

    def get_draggable_square_component(self):
        return self.draggableComponent

    def get_droppable_square_component(self):
        return self.droppableComponent

    def get_droppable_square_component_text(self):
        return self.droppableComponent.text

    def get_droppable_square_component_background_color(self):
        return self.droppableComponent.value_of_css_property("background-color")


