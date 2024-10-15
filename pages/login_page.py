import allure

from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from data import Urls, UserCredentials


class LoginPage(BasePage):
    @allure.step("Click on retrieve password btn")
    def click_to_retrieve_password(self):
        self.open_page(Urls.LOGIN)
        self.click_to_element(LoginLocators.RETRIEVE_PASSWORD)

        return self.return_page_url()

    @allure.step("Log in with username and password")
    def login(self):
        self.open_page(Urls.LOGIN)
        self.send_keys_to_locator(LoginLocators.EMAIL_FIELD, UserCredentials.EMAIL)
        self.send_keys_to_locator(LoginLocators.PASSWORD_FIELD, UserCredentials.PASSWORD)
        self.click_to_element(LoginLocators.LOGIN_BUTTON)

        return self.return_page_url()

