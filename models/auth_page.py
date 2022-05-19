from .base_page import BasePage
from .locators import AuthPageLocators


class AuthPage(BasePage):
    def auth_admin(self):
        if self.page.inner_text(AuthPageLocators.TITLE_NAME) == "Вход":
            self.insert_login()
            self.insert_password()
            self.auth_button_click()
        elif self.page.inner_text(AuthPageLocators.TITLE_NAME) == "Проекты":
            print("Вы уже авторизованы!")

    def insert_login(self):
        self.page.fill(AuthPageLocators.LOGIN_INPUT, "cutqxx@gmail.com")

    def insert_password(self):
        self.page.fill(AuthPageLocators.PASSWORD_INPUT, "cutqxx998")

    def auth_button_click(self):
        self.page.locator(AuthPageLocators.BUTTON_AUTH).click()