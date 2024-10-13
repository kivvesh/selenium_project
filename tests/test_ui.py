import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_ui(browser, url):
    browser.get(url)

    coockies = browser.get_cookie('_ym_d')
    print(coockies)
    time.sleep(10)


@pytest.mark.find_element
@pytest.mark.parametrize(
    'locator,selector',
    [
        (By.XPATH, '//input[@name="search"]'),
        (By.XPATH, '//div[@id="header-cart"]//button'),
        (By.ID, "narbar-menu"),
        (By.CLASS_NAME,'list-inline'),
        (By.CSS_SELECTOR,'div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4')
    ]
)
def test_main_page(browser, url, locator, selector):
    """Тесты для поиска элементов главной странице"""
    browser.get(url)
    element = browser.find_element(locator, selector)
    assert element


@pytest.mark.find_element
@pytest.mark.parametrize(
    'endpoint,locator,selector',
    [
        ('', By.XPATH,'//div[@class="list-group mb-3"]//a'),
        ('desktops', By.ID,'product-list'),
        ('desktops', By.ID,'compare-total'),
        ('desktops/pc', By.TAG_NAME,'h2'),
        ('desktops/mac', By.XPATH,'//a[@class="btn btn-primary d-block"]'),
    ]
)
def test_catalog(browser, url, locator, selector, endpoint):
    """Тесты для поиска элементов в каталоге"""
    browser.get(f'{url}/en-gb/catalog/{endpoint}')
    elements = browser.find_elements(locator, selector)
    assert elements


@pytest.mark.smoke
@pytest.mark.parametrize(
    'endpoint,locator,selector',
    [
        ('desktops/apple-cinema', By.TAG_NAME,'h1'),
        ('desktops/canon-eos-5d', By.XPATH,'//span[@class="price-new"]'),
        ('desktops/htc-touch-hd', By.XPATH,'//div[@id="tab-description"]//p[1]'),
        ('cameras/canon-eos-5d', By.XPATH,'//div[@id="tab-description"]//p[1]'),
    ],
    ids=['Название товара','Цена товара','Описание товара','Добавить в избранное']
)
def test_cart(browser, url, locator, selector, endpoint):
    """Тесты для поиска элементов в карточке товара"""
    browser.get(f'{url}/en-gb/product/{endpoint}')
    elements = browser.find_element(locator, selector)
    assert elements