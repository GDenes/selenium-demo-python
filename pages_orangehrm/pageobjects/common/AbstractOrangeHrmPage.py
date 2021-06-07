from abc import ABC

from selenium import webdriver

from pages_base.pageobjects.AbstractPage import AbstractPage
from pages_orangehrm.enums.PageEnum import PageEnum
from pages_orangehrm.enums.UserEnum import UserEnum
from pages_orangehrm.pageobjects.navigation.AbstractNavigationLeftSideBar import AbstractNavigationLeftSideBar
from pages_orangehrm.pageobjects.navigation.AdminNavigationLeftSideBar import AdminNavigationLeftSideBar
from pages_orangehrm.pageobjects.navigation.HeaderInterface import HeaderInterface
from pages_orangehrm.pageobjects.navigation.UserNavigationLeftSideBar import UserNavigationLeftSideBar
from utils.enums.BrowserEnum import BrowserEnum


class AbstractOrangeHrmPage(AbstractPage, HeaderInterface, ABC):
    navigation: AbstractNavigationLeftSideBar

    def __init__(self, driver: webdriver, browser: BrowserEnum, userEnum: UserEnum):
        super().__init__(driver, browser)
        if userEnum == UserEnum.ESS_USER:
            self.navigation = UserNavigationLeftSideBar(driver, browser)
        elif userEnum == UserEnum.SYSTEM_ADMIN:
            self.navigation = AdminNavigationLeftSideBar(driver, browser)

    def navigate_to(self, pageEnum: PageEnum):
        return self.navigation.navigate_to(pageEnum)
