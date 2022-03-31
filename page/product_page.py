from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_basket(self):
        self._go_to(ProductPageLocators.BUTTON_ADD_BASKET)

    def run_tests_case(self):
        self.compare_the_message_name_product()
        self.compare_the_price_in_basket()

    def compare_the_message_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        message_name_product = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_PRODUCT)
        assert name_product.text == message_name_product.text, 'The title in the message does ' \
                                                               'not match the title of the product'

    def compare_the_price_in_basket(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_in_basket = self.browser.find_element(*ProductPageLocators.ALL_PRICE_IN_BASKET)
        assert price_product.text in price_in_basket.text, 'The price in the cart must ' \
                                                           'match the price of the product'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_NAME_PRODUCT), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_NAME_PRODUCT), \
            "Success message is presented, but should not be"
