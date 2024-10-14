import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.scenario
@pytest.mark.parametrize(
    'time_wait',
    [
        (3)
    ]
)
def test_login_administration(browser,url, time_wait, my_loger, config, get_page_administration):
    """Тест для login/logout на админку"""

    my_loger.log_info(test_login_administration.__doc__)
    browser.get(f'{url}administration/')
    try:
        username = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located(get_page_administration.get('username'))
        )
        username.send_keys(config.get('admin_username'))

        password = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located(get_page_administration.get('password'))
        )
        password.send_keys(config.get('admin_password'))

        button_login = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located(get_page_administration.get('button_login'))
        )
        button_login.click()
        time.sleep(1)

        button_logout = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located(get_page_administration.get('button_logout'))
        )
        assert 'user_token' in browser.current_url

        button_logout.click()
    except Exception as error:
        my_loger.log_error(error)