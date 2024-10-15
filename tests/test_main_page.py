import allure
import pytest

from pages.login_page import LoginPage
from data import Urls
import api_requests
from pages.main_page import MainPage


class TestMainPage:
    @allure.title("Verify Click on Profile btn")
    def test_click_on_profile(self, get_main_page, get_logged_driver):
        assert get_main_page.click_on_profile() == Urls.PROFILE

    @allure.title("Verify click on Order Feed")
    def test_click_on_orders_feed(self, get_main_page, get_logged_driver):
        assert get_main_page.click_on_order_feed() == Urls.ORDER_FEED

    @allure.title("Verify Click on ingredient opens popup")
    @pytest.mark.parametrize("ingredient", api_requests.Order.get_ingredients()[1])
    def test_click_on_ingredient(self, get_main_page, ingredient):
        assert get_main_page.click_on_ingredient(ingredient) == "Детали ингредиента"

    @allure.title("Verify click on X btn in ingredient form")
    def test_close_ingredient_info(self, get_main_page):
        assert get_main_page.click_on_ingredient_and_close()

    @allure.title("Verify increase of counter when ingredient is dragged and dropped to build burger")
    def test_add_ingredient_check_counter(self, get_main_page):
        assert get_main_page.check_counter_of_ingredient()

    @allure.title("Verify authorised user creates order")
    def test_user_create_order(self, get_driver):
        login_page = LoginPage(get_driver)
        login_page.login()
        main_page = MainPage(get_driver)

        assert main_page.create_order()
