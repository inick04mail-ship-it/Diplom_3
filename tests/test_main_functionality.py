import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestMainFunctionality:

    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_constructor_button_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        main_page.click_constructor_button()
        assert 'Соберите бургер' in main_page.get_constructor_title()

    @allure.title('Проверка перехода по клику на "Ленту заказов"')
    def test_order_feed_button_click(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_order_feed_button()
        assert feed_page.get_feed_title() == 'Лента заказов'

    @allure.title('Проверка отображения окна "Детали ингредиента" при клике на ингредиент')
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.check_ingredient_modal_displayed()

    @allure.title('Проверка закрытия окна "Детали ингредиента" кликом по крестику')
    def test_ingredient_modal_closes_by_x(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.check_ingredient_modal_not_displayed()

    @allure.title('Проверка увеличения счетчика при добавлении ингредиента в заказ')
    def test_ingredient_counter_increases(self, driver, set_user_tokens):
        main_page = MainPage(driver)
        initial_count = main_page.get_ingredient_counter()
        main_page.drag_and_drop_ingredient()
        new_count = main_page.get_ingredient_counter()
        assert new_count > initial_count