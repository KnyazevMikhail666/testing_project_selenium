import time

from .page.product_page import ProductPage
from .page.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_URL
    page = ProductPage(browser, link)
    page.open()
    page.go_to(ProductPageLocators.BUTTON_ADD_BASKET)
    page.solve_quiz_and_get_code()
    page.run_tests_case()