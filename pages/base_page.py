import time

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
            self.logger.debug(f'{self.__class__.__doc__} Элемент с локатором {locator} найден')
            return element
        except Exception as error:
            self.logger.error(f'{self.__class__.__doc__} Элемент с локатором {locator} не найден\n{error}')

    def get_elements(self, locator: tuple[str,str], timeout: int=1):

        elements = WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))
        if len(elements) > 0:
            self.logger.debug(f'{self.__class__.__doc__} Элементы с локатором {locator} найдены')
        else:
            self.logger.error(f'{self.__class__.__doc__} Элементы с локатором {locator} не найдены')

    def click_element(self, locator: tuple[str,str],timeout: int=1):
        actions = ActionChains(self.browser)
        try:
            actions.move_to_element_with_offset(
                self.get_element(locator, timeout),
                randint(1,10),
                randint(1,10)
            ).pause(randint(1,2)).click().perform()
            self.logger.debug(f'{self.__class__.__doc__} Клик на элемент с локатором {locator} состоялся')
        except Exception as error:
            self.logger.debug(f'{self.__class__.__doc__} Клик на элемент с локатором {locator} не состоялся\n{error}')

    def scroll_to_element(self, locator: tuple[str,str]):
        try:
            self.browser.execute_script("arguments[0].scrollIntoView(true);", self.get_element(locator))
            self.logger.debug(f'{self.__class__.__doc__} Прокрутка до элемента с локатором {locator} состоялась')
        except Exception as error:
            self.logger.debug(f'{self.__class__.__doc__} Прокрутка до элемента с локатором {locator} не состоялась\n{error}')

    def scroll_to_y(self, y:int):
        try:
            self.browser.execute_script(f"window.scrollTo(0, {y});")
            self.logger.debug(f'{self.__class__.__doc__} Прокрутка на {y} пиксель состоялась')
        except Exception as error:
            self.logger.debug(f'{self.__class__.__doc__} Прокрутка на {y} пиксель не состоялась\n{error}')

    def click_after_detect_element(self, locator: tuple[str,str], timeout: int=1, finish: int= 10):
        point=0
        while finish>point:
            try:
                element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                self.logger.debug(f'{self.__class__.__doc__} клик на элемент с локатором {locator} состоялся через {point}  сек.')
                break
            except Exception as error:
                point+=timeout
                time.sleep(timeout)
                if point >= finish:
                    self.logger.error(f'{self.__class__.__doc__} клик на элемент с локатором {locator} состоялся\n{error}')