from selenium import webdriver


class GenericFactory:
    def max_window_size(self: webdriver):
        webdriver.maximize_window()