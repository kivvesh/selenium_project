import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ui(browser, url):
    browser.get(url)

    coockies = browser.get_cookie('_ym_d')
    print(coockies)
    time.sleep(10)


@pytest.mark.find_element
@pytest.mark.parametrize(
    'locator,selector,time_wait',
    [
        (By.XPATH, '//input[@name="search"]',3),
        (By.XPATH, '//div[@id="header-cart"]//button',3),
        (By.ID, "narbar-menu",3),
        (By.CLASS_NAME,'list-inline',3),
        (By.CSS_SELECTOR,'div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4',3)
    ]
)
def test_main_page(browser, url, locator, selector, time_wait):
    """Тесты для поиска элементов главной странице"""
    browser.get(url)
    try:
        element = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located((locator, selector))
        )
        assert element
    except Exception as error:
        print(error)


@pytest.mark.find_element
@pytest.mark.parametrize(
    'endpoint,locator,selector,time_wait',
    [
        ('', By.XPATH,'//div[@class="list-group mb-3"]//a',3),
        ('desktops', By.ID,'product-list',3),
        ('desktops', By.ID,'compare-total',3),
        ('desktops/pc', By.TAG_NAME,'h2',3),
        ('desktops/mac', By.XPATH,'//a[@class="btn btn-primary d-block"]',3),
    ]
)
def test_catalog(browser, url, locator, selector, endpoint,time_wait):
    """Тесты для поиска элементов в каталоге"""
    browser.get(f'{url}/en-gb/catalog/{endpoint}')
    try:
        elements = WebDriverWait(browser, time_wait).until(
            EC.presence_of_all_elements_located((locator, selector)))
        assert elements
    except Exception as error:
        print(error)



@pytest.mark.find_element
@pytest.mark.parametrize(
    'endpoint,locator,selector,time_wait',
    [
        ('desktops/apple-cinema', By.TAG_NAME,'h1',3),
        ('desktops/canon-eos-5d', By.XPATH,'//span[@class="price-new"]',3),
        ('desktops/htc-touch-hd', By.XPATH,'//div[@id="tab-description"]//p[1]',3),
        ('cameras/canon-eos-5d', By.XPATH,'//button[@class="btn btn-light"]',3),
        ('cameras/nikon-d300', By.XPATH,'//button[@id="button-cart"]',3),
    ],
    ids=['Title','Price','Description','In like', 'Add to cart']
)
def test_cart(browser, url, locator, selector, endpoint, time_wait):
    """Тесты для поиска элементов в карточке товара"""
    browser.get(f'{url}/en-gb/product/{endpoint}')
    try:
        element = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located((locator, selector))
        )
        assert element
    except Exception as error:
        print(error)


@pytest.mark.find_element
@pytest.mark.parametrize(
    'locator,selector,time_wait',
    [
        (By.XPATH,'//div[@class="card-header"]',3),
        (By.NAME,'username',3),
        (By.NAME,'password',3),
        (By.XPATH,'//button[@class="btn btn-primary"]',3),
        (By.XPATH,'//footer[@id="footer"]/a',3),
    ]
)
def test_administration(browser, url, locator, selector, time_wait):
    """Тесты для поиска элементов /administration"""
    browser.get(f'{url}/administration/')
    try:
        element = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located((locator, selector))
        )
        assert element
    except Exception as error:
        print(error)


@pytest.mark.find_element
@pytest.mark.parametrize(
    'locator,selector,time_wait',
    [
        (By.NAME,'firstname',3),
        (By.NAME,'lastname',3),
        (By.NAME,'email',3),
        (By.ID,'column-right',3),
        (By.XPATH,'//button[@class="btn btn-primary"]',3),
    ],
    ids=['firstname','lastname','email','column-right','button']
)
def test_register_user(browser, url, locator, selector, time_wait):
    """Тесты для поиска элементов /administration"""
    browser.get(f'{url}index.php?route=account/register')
    try:
        element = WebDriverWait(browser, time_wait).until(
            EC.presence_of_element_located((locator, selector))
        )
        assert element
    except Exception as error:
        print(error)