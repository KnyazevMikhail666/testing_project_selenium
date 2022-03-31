import pytest
from .page.product_page import ProductPage
from .page.login_page import LoginPage
from .page.locators import ProductPageLocators, MainPageLocators, LoginPageLocators

# для удобства:
# pytest -v --tb=no --language=en -m need_review

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    def add_product_to_basket(self, fixture):
        page = ProductPage(fixture, ProductPageLocators.PRODUCT_URL)
        page.open()
        page.click_add_basket()
        page.run_tests_case()

    def test_user_can_add_product_to_basket(self, setup):
        self.add_product_to_basket(setup)

    def test_guest_can_add_product_to_basket(self, browser):
        self.add_product_to_basket(browser)

    #  я так и не понял откуда брать два последних теста и оставил эти помоему они те же что и там просто
    #  называются по другому
    # setup в  conftest.py  не работал когда использовал его в классе , может что то не так делал ...
    # p.s.  прошу понять и простить

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_URL)
        page.open()
        page.click_add_basket()
        page.should_not_be_success_message()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_URL)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_URL)
        page.open()
        page.click_add_basket()
        page.should_not_be_success_message_is_disappeared()
