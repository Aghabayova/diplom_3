import allure

from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from data import Urls


class LoginPage(BasePage):
    @allure.step("Click on retrieve password btn")
    def click_to_retrieve_password(self):
        self.open_page(Urls.LOGIN)
        self.click_to_element(LoginLocators.RETRIEVE_PASSWORD)

        return self.return_page_url()