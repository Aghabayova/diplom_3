from selenium.webdriver.common.by import By


class LoginLocators:

    RETRIEVE_PASSWORD = By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"
    EMAIL_FIELD = By.XPATH, "//label[contains(text(), 'Email')]/parent::div/input"
    PASSWORD_FIELD = By.XPATH, "//label[contains(text(), 'Пароль')]/parent::div/input"
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]"