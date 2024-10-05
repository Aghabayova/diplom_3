from selenium.webdriver.common.by import By


class ProfileLocators:

    ORDER_HISTORY = By.XPATH, "//a[@href='/account/order-history']"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(text(), 'Выход')]"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]"
    PROFILE_BUTTON = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"
