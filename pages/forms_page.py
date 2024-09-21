# pages/forms_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FormsPage(BasePage):
    """Page class for the Forms page."""

    # Main menu locators
    FORMS_MENU = (By.XPATH, "(//div[@class='card mt-4 top-card'])[2]")
    PRACTICE_FORM_MENU = (By.XPATH, "//span[text()='Practice Form']")

    # Form field locators
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")

    # Gender radio buttons
    GENDER_RADIO_MALE = (By.XPATH, "//label[@for='gender-radio-1']")
    GENDER_RADIO_FEMALE = (By.XPATH, "//label[@for='gender-radio-2']")
    GENDER_RADIO_OTHER = (By.XPATH, "//label[@for='gender-radio-3']")

    MOBILE_INPUT = (By.ID, "userNumber")
    DATE_OF_BIRTH_INPUT = (By.ID, "dateOfBirthInput")

    # Subjects input
    SUBJECTS_INPUT = (By.ID, "subjectsInput")

    # Hobbies checkboxes
    HOBBIES_CHECKBOX_SPORTS = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    HOBBIES_CHECKBOX_READING = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    HOBBIES_CHECKBOX_MUSIC = (By.XPATH, "//label[@for='hobbies-checkbox-3']")

    # Picture upload
    PICTURE_UPLOAD = (By.ID, "uploadPicture")

    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")

    # State and City dropdowns
    STATE_DROPDOWN = (By.ID, "state")
    STATE_INPUT = (By.XPATH, "//div[@id='state']//input")
    CITY_DROPDOWN = (By.ID, "city")
    CITY_INPUT = (By.XPATH, "//div[@id='city']//input")

    SUBMIT_BUTTON = (By.ID, "submit")
    SUBMISSION_MESSAGE = (By.ID, "example-modal-sizes-title-lg")

    def navigate_to_forms(self):
        self.logger.info("Navigating to Forms section.")
        self.go_to()
        self.close_fixed_banner()
        self.scroll_to_element(self.FORMS_MENU)
        self.click(self.FORMS_MENU)

    def navigate_to_practice_form(self):
        self.logger.info("Navigating to Practice Form page.")
        self.click(self.PRACTICE_FORM_MENU)

    def fill_practice_form(self, first_name, last_name, email, gender, mobile, dob, subjects, hobbies, picture_path, current_address, state, city):
        self.logger.info(
            f"Filling Practice Form with first name: {first_name}, last name: {last_name}, email: {email}, mobile: {mobile}"
        )
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.EMAIL_INPUT, email)

        # Select gender
        if gender.lower() == 'male':
            self.click(self.GENDER_RADIO_MALE)
        elif gender.lower() == 'female':
            self.click(self.GENDER_RADIO_FEMALE)
        elif gender.lower() == 'other':
            self.click(self.GENDER_RADIO_OTHER)
        else:
            self.logger.warning(f"Invalid gender: {gender}")

        self.send_keys(self.MOBILE_INPUT, mobile)

        # Set date of birth
        self.set_date_of_birth(dob)

        # Select subjects
        for subject in subjects:
            self.select_subject(subject)

        # Select hobbies
        for hobby in hobbies:
            self.select_hobby(hobby)

        # Upload picture
        if picture_path:
            self.upload_picture(picture_path)

        self.send_keys(self.CURRENT_ADDRESS_INPUT, current_address)

        # Select state and city
        self.select_state(state)
        self.select_city(city)

        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)

    def set_date_of_birth(self, dob):
        """Set the date of birth. dob should be in 'dd mmm yyyy' format, e.g., '17 Sep 1990'"""
        self.logger.info(f"Setting date of birth to: {dob}")
        date_input = self.find_element(self.DATE_OF_BIRTH_INPUT)
        self.driver.execute_script("arguments[0].click();", date_input)
        date_input.send_keys(Keys.CONTROL + "a")
        date_input.send_keys(dob)
        date_input.send_keys(Keys.ENTER)

    def select_subject(self, subject):
        """Select a subject from the autocomplete"""
        self.logger.info(f"Selecting subject: {subject}")
        subject_input = self.find_element(self.SUBJECTS_INPUT)
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.TAB)

    def select_hobby(self, hobby):
        """Select a hobby checkbox"""
        self.logger.info(f"Selecting hobby: {hobby}")
        if hobby.lower() == 'sports':
            self.click(self.HOBBIES_CHECKBOX_SPORTS)
        elif hobby.lower() == 'reading':
            self.click(self.HOBBIES_CHECKBOX_READING)
        elif hobby.lower() == 'music':
            self.click(self.HOBBIES_CHECKBOX_MUSIC)
        else:
            self.logger.warning(f"Invalid hobby: {hobby}")

    def upload_picture(self, picture_path):
        """Upload a picture"""
        self.logger.info(f"Uploading picture: {picture_path}")
        picture_input = self.find_element(self.PICTURE_UPLOAD)
        picture_input.send_keys(picture_path)

    def select_state(self, state_name):
        """Select state from the dropdown"""
        self.logger.info(f"Selecting state: {state_name}")
        self.scroll_to_element(self.STATE_DROPDOWN)
        self.click(self.STATE_DROPDOWN)
        state_input = self.find_element(self.STATE_INPUT)
        state_input.send_keys(state_name)
        state_input.send_keys(Keys.ENTER)

    def select_city(self, city_name):
        """Select city from the dropdown"""
        self.logger.info(f"Selecting city: {city_name}")
        self.scroll_to_element(self.CITY_DROPDOWN)
        self.click(self.CITY_DROPDOWN)
        city_input = self.find_element(self.CITY_INPUT)
        city_input.send_keys(city_name)
        city_input.send_keys(Keys.ENTER)

    def is_submission_successful(self):
        try:
            message = self.find_element(self.SUBMISSION_MESSAGE, timeout=10).text
            self.logger.info(f"Submission message: {message}")
            return "Thanks for submitting the form" in message
        except Exception as e:
            self.logger.error(f"Submission failed: {e}")
            return False
