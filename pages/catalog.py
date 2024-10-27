import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CatalogPage(BasePage):
    """Страница каталога"""
    def add_product_to_cart(self, timeout: int=1):
        name_product = self.get_element((By.XPATH, '//div[@class="product-thumb"]//h4/a'),timeout).text
        self.scroll_to_element((By.XPATH, '//div[@class="button-group"]/button[1]'))
        self.click_element((By.XPATH, '//div[@class="button-group"]/button[1]'),timeout)
        self.scroll_to_y(0)
        self.click_after_detect_element((By.XPATH, '//div[@class="dropdown d-grid"]/button'), timeout)
        name_product_in_cart = self.get_element((By.XPATH,'//td[@class="text-start"]/a'),timeout).text
        assert name_product == name_product_in_cart
        self.logger.info('Товар добавлен в корзину')

    def delete_product_from_cart(self, timeout: int=1):
        self.scroll_to_y(0)
        self.click_after_detect_element((By.XPATH,"//button[@class='btn btn-danger']"),timeout)
        self.scroll_to_y(0)
        self.click_after_detect_element((By.XPATH, '//div[@class="dropdown d-grid"]/button'), timeout)
        text_cart = self.get_element((By.XPATH, '//li[@class="text-center p-4"]'),timeout).text
        assert text_cart == 'Your shopping cart is empty!'
