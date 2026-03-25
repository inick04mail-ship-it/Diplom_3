from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage
from locators import MainPageLocators
import allure
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_personal_account_button(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        return self

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)
        return self

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self

    @allure.step('Получить заголовок конструктора')
    def get_constructor_title(self):
        return self.get_text_on_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_login_button(self):
        self.click_on_element(MainPageLocators.LOGIN_BUTTON)
        return self

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)
        return self

    @allure.step('Проверить отображение модального окна ингредиента')
    def check_ingredient_modal_displayed(self):
        return self.check_displaying_of_element(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Проверить, что модальное окно не отображается')
    def check_ingredient_modal_not_displayed(self):
        try:
            self.wait_element_invisible(MainPageLocators.INGREDIENT_MODAL_TITLE, timeout=5)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step('Закрыть модальное окно ингредиента')
    def close_modal(self):
        try:
            close_buttons = self.find_elements_with_wait(MainPageLocators.MODAL_CLOSE_BUTTON)
            if close_buttons:
                self.click_webelement(close_buttons[0])
                self.wait_element_invisible(MainPageLocators.INGREDIENT_MODAL_TITLE, timeout=5)
        except (TimeoutException, NoSuchElementException):
            pass
        return self

    @allure.step('Перетащить ингредиент в заказ')
    def drag_and_drop_ingredient(self):
        source = self.find_element_with_wait(MainPageLocators.BURGER_INGREDIENT)
        target = self.find_element_with_wait((By.CSS_SELECTOR, '.constructor-element__text'))
        self.drag_and_drop(source, target)
        return self

    @allure.step('Получить счётчик ингредиента')
    def get_ingredient_counter(self):
        try:
            counter_element = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER)
            return int(counter_element.text)
        except (TimeoutException, NoSuchElementException, ValueError):
            return 0

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_place_order_button(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)
        return self

    @allure.step('Проверить отображение окна подтверждения заказа')
    def check_order_confirmation_displayed(self):
        return self.check_displaying_of_element(MainPageLocators.ORDER_CONFIRMATION_MODAL)

    @allure.step('Получить номер заказа в окне подтверждения')
    def get_order_number(self):
        try:
            return self.get_text_on_element(MainPageLocators.ORDER_NUMBER_MODAL)
        except (TimeoutException, NoSuchElementException, ValueError):
            return None

    @allure.step('Закрыть окно подтверждения заказа')
    def close_order_confirmation(self):
        try:
            close_button = self.find_element_with_wait(MainPageLocators.CONFIRMATION_CLOSE_BUTTON)
            self.click_webelement(close_button)
            self.wait_element_invisible(MainPageLocators.ORDER_CONFIRMATION_MODAL, timeout=5)
        except (TimeoutException, NoSuchElementException):
            pass
        return self
