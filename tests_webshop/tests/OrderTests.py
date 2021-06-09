import allure
from parameterized import parameterized_class

from pages_webshop.enums.ColorEnum import ColorEnum
from pages_webshop.enums.SizeEnum import SizeEnum
from tests_webshop.testbase.WebShopTestBase import WebShopTestBase

ADD_CART_COLOR_AND_SIZE_01 = 'Blue, M'
ADD_CART_COLOR_AND_SIZE_02 = 'Orange, S'


@parameterized_class(('size', 'color', 'expectedResult'), [
    (SizeEnum.M, ColorEnum.BLUE, ADD_CART_COLOR_AND_SIZE_01),
    (SizeEnum.S, ColorEnum.ORANGE, ADD_CART_COLOR_AND_SIZE_02),
])
class OrderTests(WebShopTestBase):
    ADD_CART_PRODUCT_TITLE_TEXT = 'Faded Short Sleeve T-shirts'
    TOTAL_PRODUCT = '$33.02'
    TOTAL_SHIPPING = '$2.00'
    TOTAL_TAX = '$0.00'
    TOTAL_PRICE = '$35.02'
    HEADER = 'AUTHENTICATION'
    CURRENT_STEP = '02. Sign in'

    @allure.description('Parameterized order tests')
    def test_order(self):
        self.navigate_to_web_shop_page()
        self.get_driver().delete_all_cookies()

        t_shirt_page = self.get_navigation_bar().hover_and_click_t_shirt_button()
        faded_short_page = t_shirt_page.click_faded_short_item()
        faded_short_page.increase_quantity_number()
        faded_short_page.select_size(self.size)
        faded_short_page.select_color(self.color)
        add_chart_dialog_box = faded_short_page.click_add_cart_button()

        self.assertEqual(self.ADD_CART_PRODUCT_TITLE_TEXT, add_chart_dialog_box.get_product_title_text(),
                         'The title of dialogbox does not match.')
        self.assertEqual(self.expectedResult, add_chart_dialog_box.get_color_and_size_text(),
                         'The color or size does not match')

        order_page = add_chart_dialog_box.click_proceed_to_checkout_button()

        self.assertEqual(self.TOTAL_PRODUCT, order_page.get_total_product_text(),
                         'Price of total product does not match')
        self.assertEqual(self.TOTAL_SHIPPING, order_page.get_total_shipping_text(),
                         'Price of total shipping does not match')
        self.assertEqual(self.TOTAL_TAX, order_page.get_total_tax_text(),
                         'Price of total tax does not match')
        self.assertEqual(self.TOTAL_PRICE, order_page.get_total_price_text(),
                         'Total price does not match')

        sign_in_page = order_page.click_proceed_checkout_button()

        self.assertEqual(self.HEADER, sign_in_page.get_head_text(),
                         'Head text does not match')
        self.assertEqual(self.CURRENT_STEP, sign_in_page.get_current_step_text(),
                         'Current Step text does not match')
