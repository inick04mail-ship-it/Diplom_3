import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import requests
from urls import Urls
import allure
from helpers import create_random_email, create_random_password, create_random_name


@pytest.fixture(params=[webdriver.Firefox, webdriver.Chrome], ids=['firefox', 'chrome'], scope="function")
def driver(request):
    driver_class = request.param
    
    if driver_class == webdriver.Chrome:
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        
    elif driver_class == webdriver.Firefox:
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        firefox_options.accept_insecure_certs = True
        firefox_options.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.set_preference("browser.tabs.remote.autostart", False)
        firefox_options.set_preference("browser.tabs.remote.autostaskbar", False)
        driver = webdriver.Firefox(options=firefox_options)
    
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_random_user():
    payload = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    response = requests.post(Urls.CREATE_USER, data=payload)
    response_body = response.json()
    yield payload, response_body
    access_token = response_body.get('accessToken')
    if access_token:
        requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})


@pytest.fixture
def set_user_tokens(driver, create_random_user):
    driver.get(Urls.BASE_URL)
    user_data = create_random_user[1]
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')
    return create_random_user[0]