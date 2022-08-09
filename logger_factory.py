from enum import Enum
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class LoggerFactory(object):

    _log = None

    @staticmethod
    def __init_logger(log_file, log_level, backup_count):
        LoggerFactory._log = logging.getLogger(log_file)
        log_format = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.7s]  %(message)s")
        LoggerFactory._log.setLevel(log_level.value)
        Path(log_file).parents[0].mkdir(parents=True, exist_ok=True)
        need_roll = Path(log_file).is_file()

        file_handler = RotatingFileHandler(log_file, backupCount=backup_count)
        file_handler.setFormatter(log_format)
        LoggerFactory._log.addHandler(file_handler)
        # Roll over on application start
        if need_roll:
            file_handler.doRollover()

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        LoggerFactory._log.addHandler(console_handler)
        return LoggerFactory._log

    @staticmethod
    def get_logger(log_file: str, log_level: LogLevel, backup_count=2) -> logging.Logger:
        logger = LoggerFactory.__init_logger(log_file, log_level, backup_count)

        return logger