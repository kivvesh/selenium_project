import tempfile
from tracemalloc import Trace

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
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
    parser.addoption("--headless", action="store", default=True,
                     help="Запуск в фоновом режиме")
    parser.addoption("--selenoid", action="store", default=False,
                     help="Запуск на selenoid")
    parser.addoption("--executer", action="store", default='http://localhost:4444/',
                     help="URL selenoid")
    parser.addoption("--browser_version", action="store", default='128',
                     help="URL selenoid")



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
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    executer = request.config.getoption("--executer")
    browser_version = request.config.getoption("--browser_version")
    executer_url = f'{executer}wd/hub'
    if browser_name == 'chrome':
        options = ChromeOptions()
        user_data_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={user_data_dir}")

    elif browser_name == 'firefox':
        options = FirefoxOptions()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    if request.config.getoption('--selenoid'):
        caps = {
            "browserName": browser_name,
            "browserVersion": f"{browser_version}.0",
            "selenoid:options": {
                "enableLog": False,
                "name":request.node.name,
                "enableVideo": True
            }
        }
        for key, value in caps.items():
            options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor=executer_url,
            options=options
        )
    else:
        driver = BROWSERS.get(browser_name)(options=options)

    driver.implicitly_wait(1)

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