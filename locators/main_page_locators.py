from selenium.webdriver.common.by import By


class MainPageLocators:

    PROFILE_BUTTON = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"
    ORDERS_FEED_BUTTON = By.XPATH, "//p[contains(text(), 'Лента Заказов')]"
    INGREDIENT = By.XPATH, "//a[@href='/ingredient/{}']"
    INGREDIENT_COUNTER = By.XPATH, "//a[@href='/ingredient/{}']/div/p"

    INGREDIENT_DETAILS_TEXT = By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]"
    CLOSE_INGREDIENT_DETAILS_BUTTON = By.XPATH, "//button[contains(@class, '_close')]"
    BUN_INGREDIENT = By.XPATH, "//p[contains(text(), 'Флюоресцентная булка R2-D3')]"

    ORDER_CART = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    ORDER_ID_TEXT = By.XPATH, "//p[contains(text(), 'идентификатор заказа')]"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"