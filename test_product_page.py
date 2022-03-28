import pytest
from .page.product_page import ProductPage
from .page.locators import ProductPageLocators

link = [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}' for n in range(10)]
bugged_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7'
ind = link.index(bugged_link)
link[ind] = pytest.param(bugged_link, marks=pytest.mark.xfail(reason='some bug'))

@pytest.mark.parametrize('link', link)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to(ProductPageLocators.BUTTON_ADD_BASKET)
    page.solve_quiz_and_get_code()
    page.run_tests_case()
