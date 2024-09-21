import time

from .base_page import BasePage
from selenium.webdriver.common.by import By


class ElementsPage(BasePage):
    """Page class for the Elements page."""

    ELEMENTS_MENU = (By.XPATH, "(//div[@class='card mt-4 top-card'])[1]")
    TEXT_BOX_MENU = (By.ID, "item-0")
    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")

    def navigate_to_elements(self):
        self.logger.info("Navigating to Elements section.")
        self.go_to()
        # time.sleep(5)
        self.close_fixed_banner()
        self.click(self.ELEMENTS_MENU)

    def navigate_to_text_box(self):
        self.logger.info("Navigating to Text Box page.")
        self.click(self.TEXT_BOX_MENU)

    def fill_text_box_form(self, name, email):
        self.logger.info(f"Filling Text Box form with name: {name}, email: {email}")
        self.send_keys(self.FULL_NAME_INPUT, name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)

    def get_output_name(self):
        output = self.find_element(self.OUTPUT_NAME).text
        self.logger.info(f"Output name: {output}")
        return output

    def get_output_email(self):
        output = self.find_element(self.OUTPUT_EMAIL).text
        self.logger.info(f"Output email: {output}")
        return output
