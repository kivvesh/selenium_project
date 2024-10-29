import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdministrationPage(BasePage):
    """Страница Админки /administration"""
    PATH = "administration"
    def login(self, username, password, time_wait):
        try:
            self.get_element((By.XPATH,'//input[@name="username"]'),time_wait).send_keys(username)
            self.get_element((By.XPATH,'//input[@name="password"]'),time_wait).send_keys(password)
            self.click_element((By.XPATH,'//button[@class="btn btn-primary"]'),time_wait)
            self.logger.info(f'{self.__class__.__doc__} Login with username = {username} and password = {password}')
        except Exception as error:
            self.logger.error(f'{self.__class__.__doc__} Login with username = {username} and password = {password}\n{error}')

    def logout(self, time_wait):
        try:
            self.click_element((By.XPATH,'//li[@id="nav-logout"]/a'),time_wait)
            self.logger.info(f'{self.__class__.__doc__} Logout')
        except Exception as error:
            self.logger.error(f'{self.__class__.__doc__} Logout\n{error}')

    def add_product(self, product):
        try:
            self.get_element((By.XPATH, '//i[@class="fa-solid fa-bars"]'), 3).click()
            self.get_element((By.XPATH, '//li[@id="menu-catalog"]/a'), 3).click()
            self.get_element((By.XPATH, '//ul[@id="collapse-1"]/li[2]'), 3).click()
            self.get_element((By.XPATH, '//div[@class="float-end"]/a[1]'), 3).click()

            self.scroll_to_element((By.XPATH,'//input[@name="product_description[1][name]"]'))
            self.get_element((By.XPATH,'//input[@name="product_description[1][name]"]'))\
                .send_keys(product.get('product_name'))

            self.scroll_to_element((By.XPATH, '//input[@name="product_description[1][meta_title]"]'))
            self.get_element((By.XPATH, '//input[@name="product_description[1][meta_title]"]'))\
                .send_keys(product.get('tag'))

            self.scroll_to_element((By.XPATH,'//a[@href="#tab-data"]'))
            self.get_element((By.XPATH,'//a[@href="#tab-data"]')).click()

            self.scroll_to_element((By.XPATH, '//input[@name="model"]'))
            self.get_element((By.XPATH, '//input[@name="model"]'))\
                .send_keys(product.get('model'))

            self.scroll_to_element((By.XPATH, '//a[@href="#tab-data"]'))
            self.get_element((By.XPATH, '//a[@href="#tab-seo"]')).click()

            self.scroll_to_element((By.XPATH, '//input[@name="product_seo_url[0][1]"]'))
            self.get_element((By.XPATH, '//input[@name="product_seo_url[0][1]"]'))\
                .send_keys(product.get('seo'))

            self.scroll_to_y(0)
            self.get_element((By.XPATH, '//div[@class="float-end"]/button'), 3).click()

            self.logger.info(f'Товар добавлен в админке')
        except Exception as error:
            self.logger.error(f'Товар не добавлен в админке {error}')

    def delete_product(self):
        try:
            self.get_element((By.XPATH, '//i[@class="fa-solid fa-bars"]'), 3).click()
            self.get_element((By.XPATH, '//li[@id="menu-catalog"]/a'), 3).click()
            self.get_element((By.XPATH, '//ul[@id="collapse-1"]/li[2]'), 3).click()

            self.get_element((By.XPATH, '//input[@name="selected[]"]')).click()
            self.get_element((By.XPATH, '//div[@class="float-end"]/button[3]'), 3).click()
            self.browser.switch_to.alert.accept()

            self.logger.info(f'Товар удален в админке')

        except Exception as error:
            self.logger.error(f'Товар не удален в админке{error}')
