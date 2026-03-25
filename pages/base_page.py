from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step('Подождать, пока элемент станет кликабельным')
    def wait_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step('Подождать, пока элемент исчезнет')
    def wait_element_invisible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step('Найти элемент на странице')
    def find_element_with_wait(self, locator, timeout=10):
        self.wait_visibility_of_element(locator, timeout)
        return self.driver.find_element(*locator)

    @allure.step('Найти несколько элементов на странице')
    def find_elements_with_wait(self, locator, timeout=10):
        self.wait_visibility_of_element(locator, timeout)
        return self.driver.find_elements(*locator)

    @allure.step('Кликнуть на элемент по локатору')
    def click_on_element(self, locator, timeout=10):
        target = self.wait_element_clickable(locator, timeout)
        ActionChains(self.driver).move_to_element(target).click().perform()

    @allure.step('Кликнуть по уже найденному элементу')
    def click_webelement(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.find_element_with_wait(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Перетащить элемент с учетом браузера')
    def drag_and_drop(self, source_element, target_element):
        browser_name = self.driver.capabilities.get('browserName', '').lower()
        if 'firefox' in browser_name:
            self.driver.execute_script(
                """
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
                """,
                source_element,
                target_element,
            )
        else:
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=10):
        element = self.find_element_with_wait(locator, timeout)
        return element.text

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator, timeout=10):
        try:
            element = self.find_element_with_wait(locator, timeout)
            return element.is_displayed()
        except Exception:
            return False

    @allure.step('Подождать смену текста на элементе')
    def wait_for_element_to_change_text(self, locator, value, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.text_to_be_present_in_element(locator, value)
        )

    @allure.step('Открыть страницу по URL')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Получить значение из localStorage')
    def get_local_storage_item(self, key):
        return self.driver.execute_script(
            f'return window.localStorage.getItem("{key}");'
        )
