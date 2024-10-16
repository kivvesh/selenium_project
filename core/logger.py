import logging
import os

from datetime import datetime

from root import ROOT_DIR
from configs.settings import settings


class Logger:
    def __init__(self, level):
        file_path = os.path.join(ROOT_DIR, 'logs', f'{datetime.now().date()}.log')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        log_level = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'ERROR': logging.ERROR,
            'WARNING': logging.WARNING,
        }.get(level.upper(), logging.DEBUG)

        # Настройка логирования
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)

        # Проверка наличия обработчиков
        if not self.logger.handlers:
            # Обработчик для записи в файл
            file_handler = logging.FileHandler(file_path)
            file_handler.setLevel(log_level)

            # Форматирование логов
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)

            # Добавление обработчика к логгеру
            self.logger.addHandler(file_handler)

            #вывод в консоль
            # console_handler = logging.StreamHandler()
            # console_handler.setLevel(log_level)
            # console_handler.setFormatter(formatter)
            # self.logger.addHandler(console_handler)


    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_debug(self, message):
        self.logger.debug(message)

my_logger = Logger(settings.get('log_level'))
