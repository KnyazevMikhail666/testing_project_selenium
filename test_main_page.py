from .page.basket_page import BasketPage
from .page.login_page import LoginPage
from .page.main_page import MainPage
from .page.locators import MainPageLocators



def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login()
    page.should_be_login_link()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MainPageLocators.MAIN_URL
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.no_products_in_the_card()
    page.message_basket_is_empty()



