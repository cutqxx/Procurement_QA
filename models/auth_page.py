from .base_page import BasePage
from .locators import AuthPageLocators


class AuthPage(BasePage):
    def auth_admin(self):
        self.insert_login()
        self.insert_password()
        self.auth_button_click()

    def insert_login(self):
        self.page.fill(AuthPageLocators.LOGIN_INPUT, "cutqxx@gmail.com")

    def insert_password(self):
        self.page.fill(AuthPageLocators.PASSWORD_INPUT, "cutqxx998")

    def auth_button_click(self):
        self.page.locator(AuthPageLocators.BUTTON_AUTH).click()