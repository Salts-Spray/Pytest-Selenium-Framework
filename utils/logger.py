# utils/logger.py
import logging
import os


class Logger:
    """Utility class for logging."""

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        if not logger.hasHandlers():
            logger.setLevel(logging.INFO)
            # Create handlers
            console_handler = logging.StreamHandler()
            file_handler = logging.FileHandler('logs/test_log.log')
            # Create formatters and add them to handlers
            formatter = logging.Formatter(
                fmt='%(asctime)s [%(levelname)s] %(name)s: %(message)s (%(filename)s:%(lineno)d)',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            console_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)
            # Add handlers to the logger
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
        return logger
