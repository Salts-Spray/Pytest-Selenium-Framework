# tests/test_base.py
import pytest
from utils.logger import Logger


class TestBase:
    """Base class for all test classes."""
    logger = None  # Define logger as a class attribute

    @pytest.fixture(autouse=True)
    def init_driver(self, request, driver_init):
        self.driver = driver_init
        type(self).logger = Logger.get_logger(self.__class__.__name__)
        yield
        self.driver.quit()
