from tests_base.driverfactory.ChromeFactory import get_driver
from utils.enums.BrowserEnum import BrowserEnum


class DriverFactory:
    def create_driver(self, browser: BrowserEnum):
        if browser == BrowserEnum.CHROME:
            chrome = get_driver()
            return chrome
