import allure

from data import Urls


class TestProfilePage:
    @allure.title("Verify click on Order History btn")
    def test_click_on_order_history(self, get_profile_page):
        assert get_profile_page.click_on_order_history() == Urls.ORDER_HISTORY

    @allure.title("Verify click on Constructor btn")
    def test_click_on_constructor(self, get_profile_page):
        assert get_profile_page.click_on_constructor_button() == Urls.MAIN

    @allure.title("Verify click on Logout btn")
    def test_click_on_logout(self, get_profile_page):
        assert get_profile_page.click_on_logout_button() == Urls.LOGIN
