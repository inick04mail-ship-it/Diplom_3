from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')
    CONSTRUCTOR_TITLE = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')
    INGREDIENT = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')
    BURGER_INGREDIENT = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')
    INGREDIENT_COUNTER = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]'
                                    '//p[@class="counter_counter__num__3nue1"][1]')
    INGREDIENT_MODAL_TITLE = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')
    MODAL_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                    '//button[contains(@class, "close")]')
    MODAL_OVERLAY = (By.XPATH, '//div[contains(@class, "Modal_modal_overlay")]')
    ORDER_CONFIRMATION_MODAL = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                          '/div[contains(@class, "Modal_modal__container")]')
    ORDER_NUMBER_MODAL = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')
    CONFIRMATION_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                           '//button[contains(@class, "close")]')
    BURGER_CONSTRUCTOR = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    PLACE_ORDER_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0')


class OrderFeedLocators:
    FEED_TITLE = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')
    ORDER_CARD = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')
    ORDER_MODAL_TITLE = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                   '//div[contains(@class, "Modal_orderBox")]//h2')
    TOTAL_ORDERS_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TODAY_ORDERS_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    ORDERS_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    ORDER_IN_FEED_TEMPLATE = (By.XPATH, './/*[text()="{order_id}"]')
    NUMBER_OF_ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]'
                                             '/li[contains(@class, "text_type_digits-default")]')


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, '//a[text() = "Зарегистрироваться"]')


class AccountPageLocators:
    PROFILE = (By.XPATH, '//a[@href = "/account/profile"]')
    ORDER_HISTORY = (By.XPATH, '//a[@href = "/account/order-history"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[@type = "button"]')
    REGISTER_BUTTON = (By.XPATH, '//a[text() = "Зарегистрироваться"]')
    DESCRIPTION = (By.XPATH, '//p[contains(@class, "Account_text")]')


class OrderHistoryPageLocators:
    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    ORDER_CARD_TITLE = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    ORDER_CARD_ID = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')


class PasswordRecoveryLocators:
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[text() = "Восстановить пароль"]')
    EMAIL_INPUT = (By.CLASS_NAME, 'input__textfield')
    RECOVER_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.input_type_password .input__textfield')
    EYE_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    PASSWORD_VISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]')
    PASSWORD_INVISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_type_password")]')
