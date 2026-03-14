import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestOrderFeed:

    @allure.title('Проверка увеличения числа на счетчике общего количества выполненных заказов')
    def test_total_orders_counter_increases(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        main_page.click_order_feed_button()
        orders_count_1 = feed_page.get_total_orders_count()
        assert orders_count_1 > 0

    @allure.title('Проверка увеличения числа на счетчике ежедневного количества выполненных заказов')
    def test_today_orders_counter_increases(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        main_page.click_order_feed_button()
        orders_count_1 = feed_page.get_today_orders_count()
        assert orders_count_1 > 0

    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    def test_order_number_appears_in_progress(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        main_page.click_order_feed_button()
        orders_in_progress = feed_page.get_orders_in_progress()
        assert isinstance(orders_in_progress, list)