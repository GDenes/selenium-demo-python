from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tests_base.driverconfig.ChromeConfig import ChromeConfig
from tests_base.driverfactory.GenericFactory import GenericFactory


def get_driver():
    # driver = webdriver.Chrome(ChromeDriverManager().install(), ChromeConfig().get_options())
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # super().max_window_size(driver)
    return driver


class ChromeFactory(GenericFactory):
    pass
