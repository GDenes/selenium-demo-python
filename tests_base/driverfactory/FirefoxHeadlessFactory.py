from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from tests_base.driverfactory.DriverInterface import DriverInterface
from tests_base.driverfactory.GenericFactory import GenericFactory


class FirefoxHeadlessFactory(GenericFactory, DriverInterface):

    def get_driver(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        self.max_window_size(driver)
        return driver

    def get_remote_driver(self, remoteUrl):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument( '--headless')
        driver = webdriver.Remote( command_executor=remoteUrl,
                                   desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True},
                                   options=firefox_options)
        self.max_window_size( driver )
        return driver


