import random
import allure
from faker import Faker


class NewUserCredentials:
    @staticmethod
    @allure.step("Generate credentials for user registration")
    def generate_credentials_set():
        """Generate fake credentials for a new user using Faker."""
        fake = Faker("en_US")
        email = fake.email()
        password = fake.password()
        name = fake.user_name()

        creds = {
            "email": email,
            "password": password,
            "name": name
        }
        return creds
