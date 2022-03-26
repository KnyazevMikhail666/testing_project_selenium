from .page.login_page import LoginPage
from .page.main_page import MainPage
from .page.locators import MainPageLocators
def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to(MainPageLocators.LOGIN_LINK)
    page.should_be_login_link()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()