from pages.base_page import BasePage
from locators import MainPageLocators
import allure
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    
    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_personal_account_button(self):
        self.wait_visibility_of_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        return self

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_order_feed_button(self):
        self.wait_visibility_of_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)
        return self

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.wait_visibility_of_element(MainPageLocators.CONSTRUCTOR_BUTTON)
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
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT)
        self.click_on_element(MainPageLocators.INGREDIENT)
        time.sleep(1)
        return self

    @allure.step('Проверить отображение модального окна ингредиента')
    def check_ingredient_modal_displayed(self):
        try:
            self.wait_visibility_of_element(MainPageLocators.INGREDIENT_MODAL_TITLE)
            return True
        except:
            return False

    @allure.step('Проверить, что модальное окно не отображается')
    def check_ingredient_modal_not_displayed(self):
        try:
            self.wait_for_closing_of_element(MainPageLocators.INGREDIENT_MODAL_TITLE, timeout=5)
            return True
        except:
            return False

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        try:
            close_buttons = self.driver.find_elements(*MainPageLocators.MODAL_CLOSE_BUTTON)
            if close_buttons:
                close_buttons[0].click()
                time.sleep(1)
        except:
            pass
        return self

    @allure.step('Перетащить ингредиент в заказ')
    def drag_and_drop_ingredient(self):
        source = self.find_element_with_wait(MainPageLocators.BURGER_INGREDIENT)
        target = self.find_element_with_wait((By.CSS_SELECTOR, '.constructor-element__text'))
        
        # Пришлось прибегнуть к помощи ИИ так как имелась проблема с Firefox и счетчиком
        
        if 'firefox' in self.driver.capabilities['browserName'].lower():
            self.driver.execute_script("""
                var source = arguments[0];
                var target = arguments[1];
                
                var dragStartEvent = new MouseEvent('dragstart', {
                    bubbles: true,
                    cancelable: true
                });
                source.dispatchEvent(dragStartEvent);
                
                var dropEvent = new MouseEvent('drop', {
                    bubbles: true,
                    cancelable: true
                });
                target.dispatchEvent(dropEvent);
                
                var dragEndEvent = new MouseEvent('dragend', {
                    bubbles: true,
                    cancelable: true
                });
                source.dispatchEvent(dragEndEvent);
            """, source, target)
        else:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source, target).perform()
        
        time.sleep(2)
        return self

    @allure.step('Получить счетчик ингредиента')
    def get_ingredient_counter(self):
        try:
            counter_element = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER)
            return int(counter_element.text)
        except:
            return 0

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_place_order_button(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)
        return self

    @allure.step('Проверить отображение окна подтверждения заказа')
    def check_order_confirmation_displayed(self):
        try:
            self.wait_visibility_of_element(MainPageLocators.ORDER_CONFIRMATION_MODAL)
            return True
        except:
            return False

    @allure.step('Получить номер заказа в окне подтверждения')
    def get_order_number(self):
        try:
            return self.get_text_on_element(MainPageLocators.ORDER_NUMBER_MODAL)
        except:
            return "0"

    @allure.step('Закрыть окно подтверждения заказа')
    def close_order_confirmation(self):
        try:
            close_button = self.find_element_with_wait(MainPageLocators.CONFIRMATION_CLOSE_BUTTON)
            close_button.click()
            time.sleep(1)
        except:
            pass
        return self