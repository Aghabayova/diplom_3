import random
import allure
import requests
from data import EndPoints


class User:
    @staticmethod
    @allure.step("New user registration")
    def create_user(user_data):
        """Create a new user via API."""
        return requests.post(EndPoints.create_user, data=user_data)

    @staticmethod
    @allure.step("Delete user")
    def delete_user(user_token):
        """Delete a user via API."""
        headers = {"Authorization": user_token}
        response = requests.delete(EndPoints.login_user, headers=headers)
        return response


class Order:
    @staticmethod
    @allure.step("Create new order")
    def create_order(ingredients, token=""):
        """Create a new order via API."""
        headers = {"Authorization": token}
        data = {"ingredients": ingredients}
        response = requests.post(EndPoints.create_order, data=data, headers=headers)
        return response

    @allure.step("Create ingredient hashes for burger")
    def create_burger(self):
        """Create a list of random ingredient hashes for a burger."""
        ingredients = self.get_ingredients()[0]
        burger_ingredients = []
        for value in ingredients.values():
            ingredient_hash = random.choice(value)
            burger_ingredients.append(ingredient_hash)
        return burger_ingredients

    @staticmethod
    @allure.step("Get ingredient list and dict by type of ingredient")
    def get_ingredients():
        """Get ingredients from API and classify them by type."""
        ingredients_dict = {
            "bun": [],
            "main": [],
            "sauce": []
        }
        ingredient_list = []
        response = requests.get(EndPoints.ingredients)
        for ingredient in response.json()["data"]:
            current_hashs = ingredients_dict.pop(ingredient["type"])
            current_hashs.append(ingredient["_id"])
            ingredients_dict[ingredient["type"]] = current_hashs
            ingredient_list.append(ingredient["_id"])

        return ingredients_dict, ingredient_list
