import allure

from locators.order_page_locators import OrderLocators
from pages.base_page import BasePage
from data import Urls
from api_requests import Order
import time


class OrderFeed(BasePage):
    @allure.step("Verify order info")
    @allure.description("1. Open order feed page"
                        "2. Click on last order"
                        "3. Verify order info is displayed")
    def open_order_info(self):
        self.open_page(Urls.ORDER_FEED)
        self.click_to_element(OrderLocators.ORDER_NUMBER_IN_FEED)

        return self.check_element_is_displayed(OrderLocators.ORDER_INFO_TEXT)

    @allure.step("Verify own order in order feed")
    @allure.description("1. Create order via API and get its ID"
                        "2. Open order feed page"
                        "3. Find order by ID")
    def check_private_orders_in_feed(self, new_user):
        token = new_user[0].json()["accessToken"]
        ingredients = Order().create_burger()
        order_id = Order().create_order(ingredients, token).json()['order']['_id']

        self.open_page(Urls.ORDER_FEED)
        order_locator = self.format_locator(OrderLocators.ORDER_BY_ID, order_id)

        return self.wait_and_find_element(order_locator)

    @allure.step("Verify order counter")
    @allure.description("1. Create Order from API"
                        "2. Get current counters for today and all times"
                        "3. Assert counters")
    def check_order_counter(self, new_user):
        self.open_page(Urls.ORDER_FEED)
        all_time_counter_before = self.get_text_locator(OrderLocators.CREATED_ALL_TIME_ORDERS)
        today_counter_before = self.get_text_locator(OrderLocators.CREATED_TODAY_ORDERS)

        token = new_user[0].json()["accessToken"]
        ingredients = Order().create_burger()
        Order().create_order(ingredients, token)

        all_time_counter_after = self.get_text_locator(OrderLocators.CREATED_ALL_TIME_ORDERS)
        today_counter_after = self.get_text_locator(OrderLocators.CREATED_TODAY_ORDERS)

        return all_time_counter_before < all_time_counter_after and today_counter_before < today_counter_after

    @allure.step("Verify created order is displayed in In Process section")
    @allure.description("1. Create order and get its number"
                        "2. Switch to order feed"
                        "3. Wait for the order to appear in In Process section"
                        "4. Assert order numbers")
    def check_order_in_progress(self, new_user):
        # Open the order feed page
        self.open_page(Urls.ORDER_FEED)
        token = new_user[0].json()["accessToken"]

        ingredients = Order().create_burger()
        order_number = Order().create_order(ingredients, token).json()['order']['number']

        time.sleep(2)

        order_number_from_locator = self.get_text_locator(OrderLocators.ORDER_IN_PROGRESS)

        normalized_order_number = str(order_number).lstrip('0')
        normalized_order_number_from_locator = order_number_from_locator.lstrip('#').lstrip(
            '0')
        return normalized_order_number == normalized_order_number_from_locator
