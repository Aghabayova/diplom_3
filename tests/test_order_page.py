import allure


class TestOrderFeed:

    @allure.title("Verify order info opening from the Order Feed")
    def test_open_order_info(self, get_order_feed_instance):
        assert get_order_feed_instance.open_order_info()

    @allure.title("Check own orders in Order Feed")
    def test_check_own_orders_in_feed(self, get_order_feed_instance, get_new_user):
        assert get_order_feed_instance.check_private_orders_in_feed(get_new_user)

    @allure.title("Verify quantity of orders made today and for all time increase")
    def test_check_order_counter(self, get_order_feed_instance, get_new_user):
        assert get_order_feed_instance.check_order_counter(get_new_user)

    @allure.title("Verify created order is displayed in 'In Process' section")
    def test_check_order_in_progress(self, get_order_feed_instance, get_new_user):
        assert get_order_feed_instance.check_order_in_progress(get_new_user)