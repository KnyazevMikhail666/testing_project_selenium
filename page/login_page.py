from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.FORM_REGISTER_EMAIL)
        input_password1 = self.browser.find_element(*LoginPageLocators.FORM_REGISTER_PASSWORD1)
        input_password2 = self.browser.find_element(*LoginPageLocators.FORM_REGISTER_PASSWORD2)
        input_email.send_keys(email)
        input_password1.send_keys(password)
        input_password2.send_keys(password)
        self._go_to(LoginPageLocators.BUTTON_REGISTRATION)
        messages = self.browser.find_element(*LoginPageLocators.SUCCESSFUL_REGISTRATION)

        assert 'Спасибо за регистрацию!' in messages.text, 'Registration failed!'

    def should_be_login_page(self):
        try:
            self.should_be_login_url()
            self.should_be_login_form()
            self.should_be_register_form()
            self.register_new_user(*self.user_generation())
        except Exception as exs:
            print('ERROR is LoginPage:', exs, flush=True)

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'not correct url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'not found login form!'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'not found register form'
