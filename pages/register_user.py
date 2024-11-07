import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterUserPage(BasePage):
    """Страница регистрации пользователя"""
    def register_new_user(self, user: dict):
        self.get_element((By.XPATH, '//div[@class="nav float-end"]//i[@class="fa-solid fa-caret-down"]')).click()
        self.click_after_detect_element((By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]/li[1]'))

        self.scroll_to_element((By.XPATH, '//input[@name="firstname"]'))
        self.get_element((By.XPATH, '//input[@name="firstname"]')).send_keys(user.get('first_name'))

        self.scroll_to_element((By.XPATH, '//input[@name="lastname"]'))
        self.get_element((By.XPATH, '//input[@name="lastname"]')).send_keys(user.get('last_name'))

        self.scroll_to_element((By.XPATH, '//input[@name="email"]'))
        self.get_element((By.XPATH, '//input[@name="email"]')).send_keys(user.get('email'))

        self.scroll_to_element((By.XPATH, '//input[@name="password"]'))
        self.get_element((By.XPATH, '//input[@name="password"]')).send_keys(user.get('password'))

        self.scroll_to_element((By.XPATH, '//button[@class="btn btn-primary"]'))
        self.get_element((By.XPATH, '//button[@class="btn btn-primary"]')).click()

        assert self.get_element((By.XPATH, '//dirv')).text == 'Warning: You must agree to the Privacy Policy!'

        self.scroll_to_element((By.XPATH, '//input[@name="agree"]'))
        self.get_element((By.XPATH, '//input[@name="agree"]')).click()

        self.scroll_to_element((By.XPATH, '//button[@class="btn btn-primary"]'))
        self.get_element((By.XPATH, '//button[@class="btn btn-primary"]')).click()
        time.sleep(1)
        text_success = self.get_element((By.XPATH, '//h1'), 3).text
        assert text_success == 'Your Account Has Been Created!'

        self.logger.info(f'Пользователь с  данными {user} зарегистрирован')
