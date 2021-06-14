import logging

import allure
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

    @allure.step("Move cursor to `draggable component` and catch it")
    def get_draggable_square_component(self):
        logging.info("Moving cursor to draggable component and catch is")
        return self.draggableComponent

    @allure.step("Drop component")
    def get_droppable_square_component(self):
        logging.info("Dropping the caught component")
        return self.droppableComponent

    @allure.step("Get text of droppable component")
    def get_droppable_square_component_text(self):
        logging.info("Getting text of droppable component")
        return self.droppableComponent.text

    @allure.step("Get color of droppable component")
    def get_droppable_square_component_background_color(self):
        logging.info("Getting background color of droppable component")
        return self.droppableComponent.value_of_css_property("background-color")


