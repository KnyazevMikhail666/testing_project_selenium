from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    PRODUCT_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, '#messages :nth-child(1) strong ')
    ALL_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.row .hidden-xs')

    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
