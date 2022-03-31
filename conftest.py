import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .page.locators import LoginPageLocators
from .page.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose languages:")


def site_language(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language:
        print(f"\nstarting browser in {language} languages for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--languages should be en or ru")
    return browser


@pytest.fixture(scope='function')
def setup(request):
    print('\nstart setup!!!')
    browser = site_language(request)
    link = LoginPageLocators.LOGIN_URL
    login = LoginPage(browser, link)
    login.open()
    login.should_be_login_page()
    login.should_be_authorized_user()

    yield browser

    browser.quit()
    print('\nexit setup!!!')


@pytest.fixture(scope="function")
def browser(request):
    print('\nstart browser!!!')
    browser = site_language(request)

    yield browser

    print("\nquit browser..")
    browser.quit()
