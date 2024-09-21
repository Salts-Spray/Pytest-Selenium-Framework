# utils/driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    """Factory class to create WebDriver instances."""

    @staticmethod
    def get_driver(browser_name='chrome'):
        if browser_name.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            # Add any desired options
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
        elif browser_name.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
            # Add any desired options
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
            driver.install_addon(r"resources/extensions/firefox/uBlock0@raymondhill.net.xpi")
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported.")
        driver.maximize_window()
        return driver
