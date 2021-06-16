from selenium import webdriver


class GenericFactory:

    @staticmethod
    def max_window_size(driver: webdriver):
        driver.maximize_window()
