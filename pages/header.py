from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderPage(BasePage):
    def get_now_currency(self, timeout):
        return self.get_element((By.XPATH,'//strong'), timeout).text

    def switch_currency(self, now_currency, timeout):
        self.get_element((By.XPATH, '//ul[@class="list-inline"]'),timeout).click()

        list_currency = self.get_elements((By.XPATH, '//ul[@class="dropdown-menu show"]/li/a'),timeout)
        for cur in list_currency:

            if now_currency not in cur.text:
                cur.click()
                break