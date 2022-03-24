import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose languages:")



@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language:
        print(f"\nstarting browser in {language} languages for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--languages should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()