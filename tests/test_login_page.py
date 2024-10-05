import allure

from data import Urls


class TestLoginPage:
    @allure.title("Verify click on retrieve password btn")
    def test_click_to_retrieve_password_success(self, get_login_page):
        assert get_login_page.click_to_retrieve_password() == Urls.FORGOT_PASS
