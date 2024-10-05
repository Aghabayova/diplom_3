import allure

from pages.base_page import BasePage
from locators.retrieve_password_locators import ForgotPasswordLocators, ResetPasswordLocators
from data import Urls


class PasswordPage(BasePage):
    @allure.step("Retrieve password. Email input")
    def input_email_address(self, email):
        self.open_page(Urls.FORGOT_PASS)

        self.click_to_element(ForgotPasswordLocators.FORGOT_PASS_LABEL)
        self.send_keys_to_locator(ForgotPasswordLocators.FORGOT_PASS_FIELD, email)
        self.click_to_element(ForgotPasswordLocators.RETRIEVE_BUTTON)
        self.wait_window_to_load(Urls.RESET_PASS)

        return self.return_page_url()

    @allure.step("Get element class name for password input field")
    def check_password_field(self):
        self.click_to_element(ResetPasswordLocators.SHOW_PASSWORD)

        return self.wait_and_find_element(ResetPasswordLocators.PASSWORD_IN_FOCUS).get_attribute("class")