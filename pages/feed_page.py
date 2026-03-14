from pages.base_page import BasePage
from locators import OrderFeedLocators
import allure


class FeedPage(BasePage):
    
    @allure.step('Получить заголовок ленты заказов')
    def get_feed_title(self):
        return self.get_text_on_element(OrderFeedLocators.FEED_TITLE)

    @allure.step('Клик по карточке заказа')
    def click_on_order_card(self):
        self.wait_visibility_of_element(OrderFeedLocators.ORDER_CARD)
        self.click_on_element(OrderFeedLocators.ORDER_CARD)
        return self

    @allure.step('Получить заголовок модального окна заказа')
    def get_order_modal_title(self):
        return self.get_text_on_element(OrderFeedLocators.ORDER_MODAL_TITLE)

    @allure.step('Получить счетчик "Выполнено за всё время"')
    def get_total_orders_count(self):
        return int(self.get_text_on_element(OrderFeedLocators.TOTAL_ORDERS_COUNTER))

    @allure.step('Получить счетчик "Выполнено за сегодня"')
    def get_today_orders_count(self):
        return int(self.get_text_on_element(OrderFeedLocators.TODAY_ORDERS_COUNTER))

    @allure.step('Получить список заказов в работе')
    def get_orders_in_progress(self):
        try:
            self.wait_visibility_of_element(OrderFeedLocators.ORDERS_IN_PROGRESS)
            orders = self.driver.find_elements(*OrderFeedLocators.ORDERS_IN_PROGRESS)
            return [order.text for order in orders]
        except:
            return []