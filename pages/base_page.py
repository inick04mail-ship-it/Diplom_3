from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Найти элемент на странице')
    def find_element_with_wait(self, locator, timeout=10):
        self.wait_visibility_of_element(locator, timeout)
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout=10):
        target = self.check_element_is_clickable(locator, timeout)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).pause(1).perform()

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator, timeout=10):
        self.wait_visibility_of_element(locator, timeout)
        return self.driver.find_element(*locator).text

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except:
            return False

    @allure.step('Подождать, пока элемент закроется')
    def wait_for_closing_of_element(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until_not(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Подождать смену текста на элементе')
    def wait_for_element_to_change_text(self, locator, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.text_to_be_present_in_element(locator, value))