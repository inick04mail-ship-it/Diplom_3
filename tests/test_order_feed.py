import allure
import requests

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from urls import Urls


class TestOrderFeed:

    @allure.title('Проверка увеличения числа на счетчике общего количества выполненных заказов')
    def test_total_orders_counter_increases(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        
        main_page.click_order_feed_button()
        initial_count = feed_page.get_total_orders_count()

        
        access_token = driver.execute_script('return window.localStorage.getItem("accessToken");')
        headers = {"Authorization": access_token}
        payload = {"ingredients": Urls.VALID_INGREDIENTS}
        requests.post(Urls.CREATE_ORDER, headers=headers, json=payload)

        
        driver.get(Urls.BASE_URL)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_order_feed_button()
        new_count = feed_page.get_total_orders_count()

        assert new_count > initial_count

    @allure.title('Проверка увеличения числа на счетчике ежедневного количества выполненных заказов')
    def test_today_orders_counter_increases(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_order_feed_button()
        initial_count = feed_page.get_today_orders_count()

        access_token = driver.execute_script('return window.localStorage.getItem("accessToken");')
        headers = {"Authorization": access_token}
        payload = {"ingredients": Urls.VALID_INGREDIENTS}
        requests.post(Urls.CREATE_ORDER, headers=headers, json=payload)

        driver.get(Urls.BASE_URL)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_order_feed_button()
        new_count = feed_page.get_today_orders_count()

        assert new_count > initial_count

    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    def test_order_number_appears_in_progress(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.click_order_feed_button()
        orders_in_progress = feed_page.get_orders_in_progress()
        assert isinstance(orders_in_progress, list)
