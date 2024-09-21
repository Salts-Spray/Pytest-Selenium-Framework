# tests/test_forms.py
import pytest
from tests.test_base import TestBase
from pages.forms_page import FormsPage
import os


@pytest.mark.usefixtures("driver_init")
class TestForms(TestBase):
    """Test cases for the Forms page."""

    @pytest.mark.smoke
    @pytest.mark.forms
    def test_fill_practice_form(self):
        self.logger.info("Starting test: test_fill_practice_form")
        forms_page = FormsPage(self.driver)
        forms_page.navigate_to_forms()
        forms_page.navigate_to_practice_form()
        forms_page.fill_practice_form(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            gender="Male",
            mobile="1234567890",
            dob="17 Sep 1990",
            subjects=["Maths", "Physics"],
            hobbies=["Sports", "Music"],
            picture_path=os.path.abspath(r"resources/images/Picture1.jpg"),
            current_address="123 Main Street",
            state="NCR",
            city="Delhi"
        )
        assert forms_page.is_submission_successful(), "Form submission failed"
        self.logger.info("Completed test: test_fill_practice_form")
