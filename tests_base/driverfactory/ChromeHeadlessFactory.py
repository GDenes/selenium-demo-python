from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tests_base.driverfactory.DriverInterface import DriverInterface
from tests_base.driverfactory.GenericFactory import GenericFactory


class ChromeHeadlessFactory(GenericFactory, DriverInterface):

    def get_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.max_window_size(driver)
        return driver

    def get_remote_driver(self, remoteUrl):
        ChromeDriverManager().install()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument( '--headless' )
        driver = webdriver.Remote( command_executor=remoteUrl,
                                   desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True},
                                   options=chrome_options)
        self.max_window_size(driver)
        return driver



