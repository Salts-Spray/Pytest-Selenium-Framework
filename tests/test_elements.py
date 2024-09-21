# tests/test_elements.py
import time

import pytest
from tests.test_base import TestBase
from pages.elements_page import ElementsPage


@pytest.mark.usefixtures("driver_init")
class TestElements(TestBase):
    """Test cases for the Elements page."""

    @pytest.mark.smoke
    @pytest.mark.elements
    def test_fill_text_box(self):
        self.logger.info("Starting test: test_fill_text_box")
        elements_page = ElementsPage(self.driver)
        elements_page.navigate_to_elements()
        elements_page.navigate_to_text_box()
        elements_page.fill_text_box_form(name="John Doe", email="john@example.com")

        output_name = elements_page.get_output_name()
        output_email = elements_page.get_output_email()
        assert "John Doe" in output_name
        assert "john@example.com" in output_email
        self.logger.info("Completed test: test_fill_text_box")
