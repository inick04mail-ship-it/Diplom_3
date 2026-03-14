from pages.base_page import BasePage
from locators import OrderHistoryPageLocators
import allure


class OrderHistoryPage(BasePage):
    
    @allure.step('Подождать прогрузки карточки заказа')
    def wait_for_order_card(self):
        self.wait_visibility_of_element(OrderHistoryPageLocators.ORDER_CARD)
        return self

    @allure.step('Получить текст заголовка карточки заказа')
    def get_order_card_title(self):
        return self.get_text_on_element(OrderHistoryPageLocators.ORDER_CARD_TITLE)

    @allure.step('Получить номер заказа в карточке')
    def get_order_card_id(self):
        return self.get_text_on_element(OrderHistoryPageLocators.ORDER_CARD_ID)