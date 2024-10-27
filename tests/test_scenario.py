import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.administration import AdministrationPage
from pages.catalog import CatalogPage


@pytest.mark.parametrize(
    'time_wait',
    [
        (3)
    ]
)
@pytest.mark.scenario
@pytest.mark.smoke
def test_login_administration(browser, url, time_wait, my_logger, config):
    """Тест для login/logout на админку"""

    my_logger.info(test_login_administration.__doc__)
    browser.get(f'{url}administration/')

    page = AdministrationPage(browser, my_logger)
    page.login(config.get('admin_username'), config.get('admin_password'),time_wait)
    page.logout(time_wait)


@pytest.mark.parametrize(
    'path,time_wait',
    [
        ('en-gb/catalog/desktops/mac',3),
        ('en-gb/catalog/tablet',3)
    ]
)
@pytest.mark.scenario1
@pytest.mark.smoke
def test_add_delete_product_to_cart(browser, time_wait, url, my_logger, config, path):
    """Тест для добавление\удаления товара в\из корзину\ы"""

    my_logger.info(test_add_delete_product_to_cart.__doc__)
    browser.get(f'{url}{path}/')

    page = CatalogPage(browser, my_logger)
    page.add_product_to_cart(3)
    page.delete_product_from_cart(3)



@pytest.mark.parametrize(
    'path,time_wait',
    [
        ('',3),
        ('en-gb/catalog/desktops',3),
    ],
    ids=['home', 'catalog']
)
@pytest.mark.scenario
@pytest.mark.smoke
def test_switch_currency (browser,time_wait, url, my_loger, config, path):
    """Тесты на проверку переключение валюты"""
    my_loger.log_info(test_switch_currency.__doc__)
    browser.get(f'{url}{path}')

    #узнаем текущую валюту, например $
    now_currency = WebDriverWait(browser, time_wait).until(
        EC.presence_of_element_located((By.XPATH,'//strong'))
    ).text

    #узнаем цену товара
    price_product = WebDriverWait(browser, time_wait).until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="price-new"]'))
    ).text

    assert now_currency in price_product

    #кликаем на выплывающий список с валютами
    list_inline = WebDriverWait(browser, time_wait).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="list-inline"]'))
    )
    list_inline.click()

    #получаем список валют и выбираем другую валюту
    list_currency = WebDriverWait(browser, time_wait).until(
        EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="dropdown-menu show"]/li/a'))
    )

    for cur in list_currency:

        if now_currency not in cur.text:
            next_currency = cur.text
            cur.click()
            break

    # узнаем текущую валюту, цену товара и сравниваем с выбранной
    now_currency = WebDriverWait(browser, time_wait).until(
        EC.presence_of_element_located((By.XPATH, '//strong'))
    ).text

    price_product = WebDriverWait(browser, time_wait).until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="price-new"]'))
    ).text

    assert now_currency in next_currency
    assert now_currency in price_product
