import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Urls
import helpers


class MainPage(BasePage):

    @allure.step("Click on the Profile button")
    def click_on_profile(self):
        self.click_to_element(MainPageLocators.PROFILE_BUTTON)
        self.wait_window_to_load(Urls.PROFILE)

        return self.return_page_url()

    @allure.step("Click on the Orders Feed button")
    def click_on_order_feed(self):
        self.click_to_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.wait_window_to_load(Urls.ORDER_FEED)

        return self.return_page_url()

    @allure.step("Click on an ingredient")
    def click_on_ingredient(self, ingredient_id):
        self.open_page(Urls.MAIN)
        self.click_to_element(self.format_locator(MainPageLocators.INGREDIENT, ingredient_id))

        return self.get_text_locator(MainPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step("Click on an ingredient and close the info popup")
    def click_on_ingredient_and_close(self):
        self.open_page(Urls.MAIN)
        self.click_to_element(MainPageLocators.BUN_INGREDIENT)

        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)
        self.wait_element_clickable(MainPageLocators.INGREDIENT_DETAILS_TEXT)

        return self.check_element_is_displayed(MainPageLocators.ORDERS_FEED_BUTTON)

    @allure.step("Add the ingredient 'Флюоресцентная булка R2-D3' to the order")
    def add_bun_to_order(self):
        self.open_page(Urls.MAIN)
        ingredient_id = helpers.Order.get_ingredients()[1][0]
        ingredient_locator = self.format_locator(MainPageLocators.INGREDIENT, ingredient_id)
        self.drag_element_and_drop(ingredient_locator, MainPageLocators.ORDER_CART)

    @allure.step("Verify that the ingredient counter increases when added to the order")
    def check_counter_of_ingredient(self):
        self.open_page(Urls.MAIN)
        ingredient_id = helpers.Order.get_ingredients()[1][0]

        ingredient_locator = self.format_locator(MainPageLocators.INGREDIENT, ingredient_id)
        ingredient_count_locator = self.format_locator(MainPageLocators.INGREDIENT_COUNTER, ingredient_id)
        ingredient_count_before = self.get_text_locator(ingredient_count_locator)

        self.drag_element_and_drop(ingredient_locator, MainPageLocators.ORDER_CART)

        ingredient_count_after = self.get_text_locator(ingredient_count_locator)

        return ingredient_count_before < ingredient_count_after

    @allure.step("Click on the 'Place Order' button")
    def create_order(self):
        self.click_to_element(MainPageLocators.CREATE_ORDER_BUTTON)

        return self.check_element_is_displayed(MainPageLocators.ORDER_ID_TEXT)
