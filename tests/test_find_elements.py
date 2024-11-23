import pytest
import allure

from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.catalog import CatalogPage
from pages.cart import CartPage
from pages.administration import AdministrationPage
from pages.register_user import RegisterUserPage


@pytest.mark.find_element
@pytest.mark.smoke
@pytest.mark.parametrize(
    'locator,time_wait',
    [
        ((By.XPATH, '//input[@name="search"]'),3),
        ((By.XPATH, '//div[@id="header-cart"]//button'),3),
        ((By.CLASS_NAME,'list-inline'),3),
        ((By.CSS_SELECTOR,'div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4'),3)
    ]
)
@allure.epic('Тестирование opencart')
@allure.feature('Поиск элемента')
@allure.story('Главная страница')
@allure.title('локатор {locator}')
def test_main_page(browser, url, locator, time_wait, my_logger):
    """Тесты для поиска элементов главной странице"""
    my_logger.info(f'{test_main_page.__doc__} с локатором {locator}')

    page = MainPage(browser, my_logger)
    page.get_element(locator, time_wait)


@pytest.mark.find_element
@pytest.mark.smoke
@pytest.mark.parametrize(
    'endpoint,locator,time_wait',
    [
        ('', (By.XPATH,'//div[@class="list-group mb-3"]//a'),3),
        ('desktops', (By.ID,'product-list'),3),
        ('desktops', (By.ID,'compare-total'),3),
        ('desktops/pc', (By.TAG_NAME,'h2'),3),
        ('desktops/mac', (By.XPATH,'//a[@class="btn btn-primary d-block"]'),3),
    ]
)
@allure.epic('Тестирование opencart')
@allure.feature('Поиск элемента')
@allure.story('Каталог')
@allure.title('локатор {locator}')
def test_catalog(browser, url, locator, endpoint,time_wait, my_logger):
    """Тесты для поиска элементов в каталоге"""
    my_logger.info(f'{test_catalog.__doc__} с локатором {locator}')

    browser.get(f'{url}/en-gb/catalog/{endpoint}')
    page = CatalogPage(browser, my_logger)
    page.get_element(locator, time_wait)



@pytest.mark.find_element
@pytest.mark.smoke
@pytest.mark.parametrize(
    'endpoint,locator,time_wait',
    [
        ('desktops/apple-cinema', (By.TAG_NAME,'h1'),3),
        ('desktops/canon-eos-5d', (By.XPATH,'//span[@class="price-new"]'),3),
        ('desktops/htc-touch-hd', (By.XPATH,'//div[@id="tab-description"]//p[1]'),3),
        ('cameras/canon-eos-5d', (By.XPATH,'//button[@class="btn btn-light"]'),3),
        ('cameras/nikon-d300', (By.XPATH,'//button[@id="button-cart"]'),3),
    ],
    ids=['Title','Price','Description','In like', 'Add to cart']
)
@allure.epic('Тестирование opencart')
@allure.feature('Поиск элемента')
@allure.story('Карточка товара')
@allure.title('локатор {locator}')
def test_cart(browser, url, locator, endpoint, time_wait, my_logger):
    """Тесты для поиска элементов в карточке товара"""
    my_logger.info(f'{test_cart.__doc__} с локатором {locator}')
    browser.get(f'{url}/en-gb/product/{endpoint}')
    page = CartPage(browser, my_logger)
    page.get_element(locator, time_wait)


@pytest.mark.find_element
@pytest.mark.smoke
@pytest.mark.parametrize(
    'locator,time_wait',
    [
        ((By.XPATH,'//div[@class="card-header"]'),3),
        ((By.NAME,'username'),3),
        ((By.NAME,'password'),3),
        ((By.XPATH,'//button[@class="btn btn-primary"]'),3),
        ((By.XPATH,'//footer[@id="footer"]/a'),3),
    ]
)
@allure.epic('Тестирование opencart')
@allure.feature('Поиск элемента')
@allure.story('Админка')
@allure.title('локатор {locator}')
def test_administration(browser, url, locator, time_wait, my_logger):
    """Тесты для поиска элементов /administration"""
    my_logger.info(test_administration.__doc__)
    browser.get(f'{url}/administration/')
    page = AdministrationPage(browser, my_logger)
    page.get_element(locator, time_wait)



@pytest.mark.find_element
@pytest.mark.smoke
@pytest.mark.parametrize(
    'locator,time_wait',
    [
        ((By.NAME,'firstname'),3),
        ((By.NAME,'lastname'),3),
        ((By.NAME,'email'),3),
        ((By.ID,'column-right'),3),
        ((By.XPATH,'//button[@class="btn btn-primary"]'),3),
    ],
    ids=['firstname','lastname','email','column-right','button']
)
@allure.epic('Тестирование opencart')
@allure.feature('Поиск элемента')
@allure.story('Страница регистрации')
@allure.title('локатор {locator}')
def test_register_user(browser, url, locator, time_wait, my_logger):
    """Тесты для поиска элементов на index.php?route=account/register"""
    my_logger.info(test_register_user.__doc__)
    browser.get(f'{url}index.php?route=account/register')
    page = RegisterUserPage(browser, my_logger)
    page.get_element(locator, time_wait)

