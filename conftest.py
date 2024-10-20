import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from configs.settings import settings
from core.logger import my_logger


BROWSERS = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox,
}

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Браузер для запуска тестов")
    parser.addoption("--url", action="store", default="http://10.0.2.15:8081/",
                     help=" Url  сервиса")
    parser.addoption("--log_level", action="store", default="debug",
                     help="Уровень логирования")


@pytest.fixture(scope='session')
def my_loger(request):
    level = request.config.getoption('--log_level', default='DEBUG').upper()
    loger = my_logger # Инициализация логгера с указанным уровнем
    my_logger.logger.setLevel(level)
    return loger


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption("--browser", default="chrome")

    driver = BROWSERS.get(browser_name)()
    driver.implicitly_wait(1)
    yield driver

    driver.quit()

@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption("--url", default="http://10.0.2.15:8081/")

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