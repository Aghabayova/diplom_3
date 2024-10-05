from selenium.webdriver.common.by import By


class OrderLocators:

    ORDER_NUMBER_IN_FEED = By.XPATH, "//p[contains(@class, 'text_type_digits-default')]"
    CREATED_ALL_TIME_ORDERS = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    CREATED_TODAY_ORDERS = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    ORDER_IN_PROGRESS = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")
    ORDER_INFO_TEXT = By.XPATH, "//p[contains(text(), 'Cостав')]"
    ORDER_BY_ID = By.XPATH, "//a[@href='/feed/{}']"
