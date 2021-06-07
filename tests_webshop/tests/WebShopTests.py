from tests_webshop.testbase.WebShopTestBase import WebShopTestBase


class WebShopTests(WebShopTestBase):
    SCREENSHOT_NAME = '../screenshots/testScreenshot.png'
    
    SEARCH_VALUE = 'blouse'
    BLOUSE_DESCRIPTION = 'Short sleeved blouse with feminine draped sleeve detail.'

    def test_create_screenshot(self):
        home_page = self.navigate_to_web_shop_page()
        home_page.get_girl_in_the_red_dress().screenshot(self.SCREENSHOT_NAME)

    def test_search(self):
        self.navigate_to_web_shop_page()
        search_page = self.get_navigation_bar().fill_input_field_and_search(self.SEARCH_VALUE)
        quick_view_dialog_box = search_page.clickFirstElement()

        self.assertEqual(self.BLOUSE_DESCRIPTION, quick_view_dialog_box.get_description_text(),
                         'Incorrect blouse description')
