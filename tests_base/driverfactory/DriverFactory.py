from tests_base.driverfactory.ChromeFactory import ChromeFactory
from tests_base.driverfactory.ChromeHeadlessFactory import ChromeHeadlessFactory
from tests_base.driverfactory.FirefoxFactory import FirefoxFactory
from tests_base.driverfactory.FirefoxHeadlessFactory import FirefoxHeadlessFactory
from utils.enums.BrowserEnum import BrowserEnum


class DriverFactory:

    def create_driver(self, browser: BrowserEnum):
        driver: None
        if browser == BrowserEnum.CHROME:
            driver = ChromeFactory().get_driver()
        if browser == BrowserEnum.CHROME_HEADLESS:
            driver = ChromeHeadlessFactory().get_driver()
        if browser == BrowserEnum.FIREFOX:
            driver = FirefoxFactory().get_driver()
        if browser == BrowserEnum.FIREFOX_HEADLESS:
            driver = FirefoxHeadlessFactory().get_driver()
        return driver

    def create_remote_driver(self, browser: BrowserEnum, remoteUrl):
        driver: None
        if browser == BrowserEnum.CHROME:
            driver = ChromeFactory().get_remote_driver(remoteUrl)
        if browser == BrowserEnum.CHROME_HEADLESS:
            driver = ChromeHeadlessFactory().get_remote_driver(remoteUrl)
        if browser == BrowserEnum.FIREFOX:
            driver = FirefoxFactory().get_remote_driver(remoteUrl)
        if browser == BrowserEnum.FIREFOX_HEADLESS:
            driver = FirefoxHeadlessFactory().get_remote_driver(remoteUrl)
        return driver

