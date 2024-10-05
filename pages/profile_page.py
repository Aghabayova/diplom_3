import allure

from locators.profile_page_locators import ProfileLocators
from pages.base_page import BasePage
from data import Urls


class ProfilePage(BasePage):

    @allure.step("Order History click in Profile page")
    def click_on_order_history(self):
        self.click_to_element(ProfileLocators.PROFILE_BUTTON)
        self.click_to_element(ProfileLocators.ORDER_HISTORY)

        return self.return_page_url()

    @allure.step("Constructor btn click")
    def click_on_constructor_button(self):
        self.click_to_element(ProfileLocators.PROFILE_BUTTON)
        self.click_to_element(ProfileLocators.CONSTRUCTOR_BUTTON)

        return self.return_page_url()

    @allure.step("Click on logout in profile page")
    def click_on_logout_button(self):
        self.click_to_element(ProfileLocators.PROFILE_BUTTON)
        self.click_to_element(ProfileLocators.LOGOUT_BUTTON)
        self.wait_window_to_load(Urls.LOGIN)

        return self.return_page_url()
