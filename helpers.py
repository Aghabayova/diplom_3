import random
import allure
import requests
from faker import Faker

from data import EndPoints


class NewUserCredentials:

    @staticmethod
    @allure.step("Generate credentials for user registration")
    def generate_credentials_set():
        fake = Faker("en_US")

        email = fake.email()
        password = fake.password()
        name = fake.user_name()

        creds = {"email": email,
                 "password": password,
                 "name": name,
                 }
        return creds


class User:
    @staticmethod
    @allure.step("New user registration")
    def create_user(user_data):
        return requests.post(EndPoints.create_user, data=user_data)

    @staticmethod
    @allure.step("Delete user")
    def delete_user(user_token):
        headers = {"Authorization": user_token}
        response = requests.delete(EndPoints.login_user, headers=headers)

        return response


class Order:
    @staticmethod
    @allure.step("Create new order")
    def create_order(ingredients, token=""):
        headers = {"Authorization": token}
        data = {"ingredients": ingredients}
        response = requests.post(EndPoints.create_order, data=data, headers=headers)

        return response

    @allure.step("Create ingredient hashes for burger")
    def create_burger(self):
        ingredients = self.get_ingredients()[0]
        burger_ingredients = []
        for value in ingredients.values():
            ingredient_hash = random.choice(value)
            burger_ingredients.append(ingredient_hash)

        return burger_ingredients

    @staticmethod
    @allure.step("Get ingredient list and dict by type of ingredient")
    def get_ingredients():
        ingredients_dict = {"bun": [],
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
