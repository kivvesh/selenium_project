import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.administration import AdministrationPage
from pages.catalog import CatalogPage
from pages.header import HeaderPage
from pages.register_user import RegisterUserPage
from tests.test_find_elements import test_register_user


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
@pytest.mark.scenario
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
def test_switch_currency(browser,time_wait, url, my_logger, config, path):
    """Тесты на проверку переключение валюты"""
    my_logger.info(test_switch_currency.__doc__)
    browser.get(f'{url}{path}')

    page_header = HeaderPage(browser, my_logger)
    now_currency = page_header.get_now_currency(time_wait)
    page_catalog = CatalogPage(browser, my_logger)
    price_product = page_catalog.get_price_product((By.XPATH, '//span[@class="price-new"]'), time_wait)
    assert now_currency in price_product

    page_header.switch_currency(now_currency, time_wait)
    after_currency = page_header.get_now_currency(time_wait)
    price_product = page_catalog.get_price_product((By.XPATH, '//span[@class="price-new"]'), time_wait)
    assert after_currency in price_product
    assert after_currency != now_currency


@pytest.mark.scenario
@pytest.mark.smoke
def test_add_product_in_administration(browser, url, my_logger, config):
    """Тест на проверку добавления товара в админке"""
    my_logger.info(test_add_product_in_administration.__doc__)
    browser.get(f'{url}{AdministrationPage.PATH}')
    page = AdministrationPage(browser, my_logger)
    page.login(config.get('admin_username'), config.get('admin_password'), 1)
    page.add_product(product=config.get('product'))


@pytest.mark.scenario
@pytest.mark.smoke
def test_delete_product_in_administration(browser, url, my_logger, config):
    """Тест на проверку удаления товара из админки"""
    my_logger.info(test_add_product_in_administration.__doc__)
    browser.get(f'{url}{AdministrationPage.PATH}')
    page = AdministrationPage(browser, my_logger)
    page.login(config.get('admin_username'), config.get('admin_password'), 1)
    page.delete_product()


@pytest.mark.scenario
@pytest.mark.smoke
def test_register_new_user(browser, url, my_logger, config):
    """Тест на проверку регистрации нового пользователя"""
    my_logger.info(test_register_new_user.__doc__)
    browser.get(url)
    page = RegisterUserPage(browser, my_logger)
    page.register_new_user(config.get('new_user'))
