from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

from logging import Logger

class BasePage:
    def __init__(self, browser: WebDriver, logger: Logger):
        self.browser = browser
        self.logger = logger

    def get_element(self, locator: tuple[str,str], timeout: int=1):
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            self.logger.debug(f'Элемент с локатором {locator} найден')
            return element
        except Exception as error:
            self.logger.error(f'Элемент с локатором {locator} не найден\n{error}')

    def get_elements(self, locator: tuple[str,str], timeout: int=1):

        elements = WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))
        if len(elements) > 0:
            self.logger.debug(f'Элементы с локатором {locator} найдены')
        else:
            self.logger.error(f'Элементы с локатором {locator} не найдены')

    def click_element(self, locator: tuple[str,str]):
        actions = ActionChains(self.browser)
        try:
            actions.move_to_element_with_offset(
                self.get_element(locator),
                randint(1,10),
                randint(1,10)
            ).pause(randint(1,2)).click().perform()
            self.logger.debug(f'Клик на элемент с локатором {locator} состоялся')
        except Exception as error:
            self.logger.debug(f'Клик на элемент с локатором {locator} не состоялся\n{error}')
