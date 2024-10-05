from selenium.webdriver.common.by import By


class ForgotPasswordLocators:

    FORGOT_PASS_LABEL = By.XPATH, "//label[contains(text(), 'Email')]"
    FORGOT_PASS_FIELD = By.XPATH, "//label[contains(text(), 'Email')]/parent::div/input"
    RETRIEVE_BUTTON = By.XPATH, "//button[contains(text(), 'Восстановить')]"


class ResetPasswordLocators:

    SHOW_PASSWORD = By.XPATH, "//input[@name='Введите новый пароль']/parent::div"
    PASSWORD_IN_FOCUS = By.XPATH, "//input[@name='Введите новый пароль']/parent::div/label"