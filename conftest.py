from tracemalloc import Trace

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from configs.settings import settings
from core.logger import Logger


BROWSERS = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox,
}

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Браузер для запуска тестов")
    parser.addoption("--url", action="store", default="http://10.0.2.15:8081/",
                     help=" Url  сервиса")
    parser.addoption("--log_level", action="store", default="info",
                     help="Уровень логирования")


@pytest.fixture(scope='session', autouse=True)
def my_logger(request):
    level = request.config.getoption('--log_level', default='INFO').upper()
    loger = Logger('TestLogger',level) # Инициализация логгера с указанным уровнем
    return loger.get_logger()

@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption("--url", default="http://10.0.2.15:8081/")


@pytest.fixture(scope='session')
def browser(url, request):
    browser_name = request.config.getoption("--browser", default="chrome")

    driver = BROWSERS.get(browser_name)()
    driver.implicitly_wait(1)
    driver.get(url)
    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def config():
    return settings

@pytest.fixture(scope="function")
def get_page_administration():
    return {
        'username': (By.XPATH,'//input[@name="username"]'),
        'password': (By.XPATH,'//input[@name="password"]'),
        'button_login': (By.XPATH,'//button[@class="btn btn-primary"]'),
        'button_logout': (By.XPATH,'//li[@id="nav-logout"]/a'),
    }