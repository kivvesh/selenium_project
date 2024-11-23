import logging
import os

from datetime import datetime

from root import ROOT_DIR
from configs.settings import settings


class Logger:
    def __init__(self,name, level):
        file_path = os.path.join(ROOT_DIR, 'logs', f'{datetime.now().date()}.log')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        log_level = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'ERROR': logging.ERROR,
            'WARNING': logging.WARNING,
        }.get(level.upper(), logging.DEBUG)

        # Настройка логирования
        self.logger = logging.getLogger(name)
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

    def get_logger(self):
        """Возвращает настроенный логгер."""
        return self.logger
