class Urls:
    MAIN = 'https://stellarburgers.nomoreparties.site/'

    REGISTER = MAIN + 'register'
    LOGIN = MAIN + 'login'
    FORGOT_PASS = MAIN + 'forgot-password'
    RESET_PASS = MAIN + 'reset-password'
    PROFILE = MAIN + 'account/profile'
    ORDER_HISTORY = MAIN + 'account/order-history'
    ORDER_FEED = MAIN + 'feed'


class EndPoints:
    test_url = 'https://stellarburgers.nomoreparties.site'
    ingredients = test_url + '/api/ingredients'
    create_order = test_url + '/api/orders'
    create_user = test_url + '/api/auth/register'
    login_user = test_url + '/api/auth/login'
    get_user_info = test_url + '/api/auth/user'
    update_user = test_url + '/api/auth/user'
    delete_user = test_url + '/api/auth/user'
    get_all_orders = test_url + '/api/orders/all'
    get_orders = test_url + '/api/orders'
