import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose languages: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser, options = None, Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language if language else None})
    if language == "es" or language == 'fr':
        print("\nstarting browser in es languages for test.." if language == 'es'
              else "\nstarting browser in fr languages for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--languages should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()