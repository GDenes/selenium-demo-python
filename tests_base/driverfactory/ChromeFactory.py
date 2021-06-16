from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tests_base.driverfactory.DriverInterface import DriverInterface
from tests_base.driverfactory.GenericFactory import GenericFactory


class ChromeFactory(GenericFactory, DriverInterface):

    def get_driver(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        super().max_window_size(driver)
        return driver

    def get_remote_driver(self, remoteUrl):
        driver = webdriver.Remote(command_executor=remoteUrl,
                                   desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        self.max_window_size( driver )
        return driver
