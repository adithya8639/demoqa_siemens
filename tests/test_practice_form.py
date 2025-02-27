import time

from charset_normalizer import from_path

from pages.practice_form_page import PracticeFormPage
from utils import logger

def test_successful_form_submission(driver):
    form_page = PracticeFormPage(driver)
    logger.log_info("Navigating to the Practice Form page")
    form_page.navigate_to_practice_form()
    form_page.fill_form(
        first_name="Adithya",
        last_name="Aleti",
        email="adithya12345@example.com",
        mobile="9989834219",
        address="123 street, Hyderabad"
    )
    form_page.submit_form()

    logger.log_info("Validating form submission successful")
    assert form_page.is_submission_successful(), "Form submission should be successful"

def test_invalid_email_validation(driver):
    form_page = PracticeFormPage(driver)

    logger.log_info("Navigating to the Practice Form page")
    form_page.navigate_to_practice_form()

    logger.log_info("Filling out the form with invalid email")
    form_page.fill_form(first_name="adithya", last_name="aleti", email="invalid-email", mobile="8639564475",address="Hyderabad")
    form_page.submit_form()

    logger.log_info("Validating the email error message")
    assert form_page.validate_email(), "Please provide proper email"

def test_invalid_mobile_validation(driver):
    form_page = PracticeFormPage(driver)

    logger.log_info("Navigating to the Practice Form page")
    form_page.navigate_to_practice_form()

    logger.log_info("Filling out the form with invalid mobile")
    form_page.fill_form(first_name="adithya", last_name="aleti", email="adithya.aleti1@gmail.com", mobile="",address="Hyderabad")
    form_page.submit_form()

    logger.log_info("Validating the mobile error message")
    assert form_page.validate_mobile(), "Please provide valid mobile number"

#same script can be used for last name aswel
def test_invalid_firstname(driver):
    form_page = PracticeFormPage(driver)

    logger.log_info("Navigating to the Practice Form page")
    form_page.navigate_to_practice_form()

    logger.log_info("Filling out the form with invalid firstname")
    form_page.fill_form(first_name="123", last_name="aleti", email="invalid-email", mobile="8639564475",address="Hyderabad")
    form_page.submit_form()

    logger.log_info("Validating the firstname error message")
    assert form_page.validate_mobile(), "Please provide valid first name"


def test_upload_picture(driver):
    form_page = PracticeFormPage(driver)

    logger.log_info("Navigating to the Practice Form page")
    form_page.navigate_to_practice_form()

    logger.log_info("Upload image available in resources")
    form_page.upload_image()

