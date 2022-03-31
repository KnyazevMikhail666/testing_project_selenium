from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BUTTON_BASKET = (By.CSS_SELECTOR, '.basket-mini a.btn-default')
    MESSAGE_YOUR_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
    MESSAGE_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '#content_inner  .basket-title h2')


class LoginPageLocators:
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    FORM_REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    FORM_REGISTER_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    FORM_REGISTER_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name="registration_submit"]')
    SUCCESSFUL_REGISTRATION = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner')

class ProductPageLocators:
    PRODUCT_URL = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, '#messages :nth-child(1) strong ')
    ALL_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.row .hidden-xs')

    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
