import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from locators.login_locators import LoginLocators
from data import Urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Wait and find element by locator")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 15).until((EC.visibility_of_element_located(locator)))

        return self.driver.find_element(*locator)

    @allure.step("Find element and send text")
    def send_keys_to_locator(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    @allure.step("Get element text")
    def get_text_locator(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step("Wait until element is clickable and click on it")
    def click_to_element(self, locator):

        WebDriverWait(self.driver, 15).until((EC.element_to_be_clickable(locator)))
        element = self.driver.find_element(*locator)

        attempt_count = 1000000
        for i in range(attempt_count):
            try:
                element.click()
                break
            except ElementClickInterceptedException:
                pass

    @allure.step("Open url page")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Verify element is displayed")
    def check_element_is_displayed(self, locator):
        return self.wait_and_find_element(locator).is_displayed()

    @staticmethod
    @allure.step("Generate locator")
    def format_locator(locator, param):
        search_type, search_text = locator

        return search_type, search_text.format(param)

    @allure.step("Return current page url")
    def return_page_url(self):
        return self.driver.current_url

    @allure.step("drag and drop element")
    def drag_element_and_drop(self, locator_from, locator_to):
        element_from = self.wait_and_find_element(locator_from)
        element_to = self.wait_and_find_element(locator_to)
        actions_chain = ActionChains(self.driver)
        actions_chain.drag_and_drop(element_from, element_to).pause(5).perform()

    @allure.step("Execute script")
    def execute_script(self, script, arg):
        self.driver.execute_script(script, arg)

    @allure.step("User authorisation")
    def login_user(self, new_user):
        base_page = BasePage(self.driver)
        base_page.open_page(Urls.LOGIN)
        base_page.send_keys_to_locator(LoginLocators.EMAIL_FIELD, new_user[1]["email"])
        base_page.send_keys_to_locator(LoginLocators.PASSWORD_FIELD, new_user[1]["password"])

        element = base_page.wait_and_find_element(LoginLocators.LOGIN_BUTTON)
        base_page.execute_script("arguments[0].click();", element)

    @allure.step("Wait until page is loaded")
    def wait_window_to_load(self, link):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(link))

    @allure.step("Wait until locator is clickable")
    def wait_element_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))