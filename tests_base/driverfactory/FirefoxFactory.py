from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from tests_base.driverfactory.DriverInterface import DriverInterface
from tests_base.driverfactory.GenericFactory import GenericFactory


class FirefoxFactory(GenericFactory, DriverInterface):

    def get_driver(self):
        driver = webdriver.Firefox(GeckoDriverManager().install())
        self.max_window_size(driver)
        return driver

    def get_remote_driver(self, remoteUrl):
        GeckoDriverManager().install()
        driver = webdriver.Remote( command_executor=remoteUrl,
                                   desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})
        self.max_window_size(driver)
        return driver