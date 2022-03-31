from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_YOUR_BASKET_IS_EMPTY)

    def no_products_in_the_card(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_PRODUCTS_IN_BASKET)
