from pages.base_page import BasePage
from locators import AccountPageLocators
import allure


class AccountPage(BasePage):
    
    @allure.step('Клик по кнопке "История заказов"')
    def click_order_history_button(self):
        self.click_on_element(AccountPageLocators.ORDER_HISTORY)
        return self

    @allure.step('Клик по кнопке "Выйти"')
    def click_logout_button(self):
        self.click_on_element(AccountPageLocators.LOGOUT_BUTTON)
        return self

    @allure.step('Подождать прогрузки описания раздела')
    def wait_for_description(self):
        self.wait_visibility_of_element(AccountPageLocators.DESCRIPTION)
        return self

    @allure.step('Проверить отображение описания раздела')
    def is_description_displayed(self):
        return self.check_displaying_of_element(AccountPageLocators.DESCRIPTION)

    @allure.step('Подождать прогрузки кнопки "Зарегистрироваться"')
    def wait_for_register_button(self):
        self.wait_visibility_of_element(AccountPageLocators.REGISTER_BUTTON)
        return self

    @allure.step('Проверить отображение кнопки "Зарегистрироваться"')
    def is_register_button_displayed(self):
        return self.check_displaying_of_element(AccountPageLocators.REGISTER_BUTTON)