import pytest

from selenium import webdriver


BROWSERS = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox,
}

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Браузер для запуска тестов")
    parser.addoption("--url", action="store", default="http://10.0.2.15:8081/",
                     help=" Url  сервиса")

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

