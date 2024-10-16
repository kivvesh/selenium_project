import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
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

@pytest.mark.parametrize(
    'path,time_wait',
    [
        ('en-gb/catalog/desktops/mac',3),
        ('en-gb/catalog/tablet',3)
    ]
)
@pytest.mark.scenario
def test_add_product_to_cart(browser,time_wait, url, my_loger, config, path):
    """Тест для добавление\удаления товара в\из корзину\ы"""

    my_loger.log_info(test_add_product_to_cart.__doc__)
    browser.get(f'{url}{path}/')
    browser.delete_all_cookies()
    time.sleep(1)
    try:
        #получаем название товара и добавляем в корзину
        name_product = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located((By.XPATH,'//div[@class="description"]/h4/a'))
        ).text
        while True:
            buttons = WebDriverWait(browser, time_wait).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="button-group"]/button[1]'))
            )
            if len(buttons) == 0:
                browser.execute_script("window.scrollBy(0, 300);")
            else:
                break
        #кликаем с помощью метода js
        browser.execute_script("arguments[0].click();", buttons[0])

        # 2 способ
        # browser.execute_script("arguments[0].scrollIntoView(true);", buttons[0])
        # while True:
        #     try:
        #         buttons[0].click()
        #         break
        #     except Exception:
        #         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # ожидаем пока корзина будет достпуна для клика
        while True:
            try:
                cart_button = WebDriverWait(browser, time_wait).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@class="dropdown d-grid"]/button'))
                )
                cart_button.click()
                break
            except:
                time.sleep(time_wait)
        # получаем название товара в корзине
        cart_table = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located((By.XPATH,'//td[@class="text-start"]/a'))
        )

        assert cart_table.text == name_product

        # удаляем товар из корзины
        remove_product = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located((By.XPATH,"//button[@class='btn btn-danger']"))
        )
        remove_product.click()

        #кликаем по корзине
        while True:
            try:
                cart_button = WebDriverWait(browser, time_wait).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@class="dropdown d-grid"]/button'))
                )
                cart_button.click()
                break
            except:
                time.sleep(time_wait)

        #получаем мэсседж из корзины
        text_cart = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located((By.XPATH, '//li[@class="text-center p-4"]'))
        ).text
        assert text_cart == 'Your shopping cart is empty!'
        time.sleep(5)


    except Exception as error:
        my_loger.log_error(error)

