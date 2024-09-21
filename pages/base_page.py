from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from utils.logger import Logger


class BasePage:
    """Base class for all pages."""

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demoqa.com/"
        self.logger = Logger.get_logger(self.__class__.__name__)

    def go_to(self, url=""):
        """Navigate to a page."""
        full_url = self.base_url + url
        self.logger.info(f"Navigating to URL: {full_url}")
        self.driver.get(full_url)

    def find_element(self, locator, timeout=10):
        """Find a single element."""
        self.logger.info(f"Finding element: {locator}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def find_elements(self, locator, timeout=10):
        """Find multiple elements."""
        self.logger.info(f"Finding elements: {locator}")
        elements = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
        return elements

    def click(self, locator, timeout=10):
        """Click an element after scrolling it into view."""
        self.logger.info(f"Clicking element: {locator}")
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def send_keys(self, locator, text, timeout=10):
        """Send keys to an element."""
        self.logger.info(f"Sending keys to element: {locator}, text: {text}")
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(text)

    def close_fixed_banner(self):
        """Close the fixed banner if it appears."""
        try:
            # Adjust the locator to match the close button of the banner
            close_button = self.find_element((By.ID, "close-fixedban"), timeout=5)
            close_button.click()
            self.logger.info("Closed the fixed banner.")
        except (NoSuchElementException, TimeoutException):
            self.logger.info("No fixed banner to close.")

    def scroll_to_element(self, locator, timeout=10):
        """Scroll to the element specified by the locator."""
        self.logger.info(f"Scrolling to element: {locator}")
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
