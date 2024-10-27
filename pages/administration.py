from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdministrationPage(BasePage):
    """Страница Админки /administration"""
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


