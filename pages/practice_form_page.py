import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.config import BASE_URL
import os

class PracticeFormPage(BasePage):
    # Navigation Elements
    FORMS_MENU = (By.XPATH, "//h5[text()='Forms']")
    PRACTICE_FORM_BUTTON = (By.XPATH, "//span[text()='Practice Form']")

    # Form Fields
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL_FIELD = (By.ID, "userEmail")
    MOBILE = (By.ID, "userNumber")
    ADDRESS = (By.ID, "currentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    GENDER = (By.XPATH,"#//input[@id='gender-radio-1']")

    # Validation Elements
    EMAIL_ERROR_MSG = (By.XPATH, "//input[@id='userEmail' and contains(@class, 'error')]")
    MOBILE_ERROR_MSG = (By.XPATH, "//input[@id='userNumber' and contains(@class, 'error')]")

    IFRAME_AD = (By.TAG_NAME, "iframe")
    OVERLAY_AD = (By.XPATH, "//div[contains(@id, 'google_ads_iframe')]")

    UPLOAD_BUTTON = (By.XPATH,'//input[@id="uploadPicture"]')
    DELETEIT = (By.XPATH,'//input[@id="uploadPicture"]/parent::div')

    def remove_ads(self):
        try:
            for iframe in self.driver.find_elements(*self.IFRAME_AD):
                self.driver.execute_script("arguments[0].remove();", iframe)
            for overlay in self.driver.find_elements(*self.OVERLAY_AD):
                self.driver.execute_script("arguments[0].remove();", overlay)
        except:
            pass

    def navigate_to_practice_form(self):
        self.visit(BASE_URL)
        self.wait_for_visibility(self.FORMS_MENU)
        self.remove_ads()
        forms_menu = self.find_element(self.FORMS_MENU)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", forms_menu)
        self.driver.execute_script("arguments[0].click();", forms_menu)
        self.wait_for_visibility(self.PRACTICE_FORM_BUTTON)
        self.driver.execute_script("arguments[0].click();",self.find_element(self.PRACTICE_FORM_BUTTON))

    def validate_firstname(self):
        error_color = "rgb(206, 208, 214)"
        #validate firstname
        first_name = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        first_name_border_color = first_name.value_of_css_property("border-color")
        if first_name_border_color == error_color:
            return False
        else:
            return True

    def validate_email(self):
        error_color = "rgb(206, 208, 214)"
        # validate email
        email = self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        email_border_color = email.value_of_css_property("border-color")
        if email_border_color == error_color:
            return False
        else:
            return True

    def validate_mobile(self):
        error_color = "rgb(206, 208, 214)"
        # validate mobile number
        mobile = self.wait.until(EC.visibility_of_element_located(self.MOBILE))
        mobile_border_color = mobile.value_of_css_property("border-color")
        if mobile_border_color == error_color:
            return False
        else:
            return True


    def submit_form_without_filling(self):
        submit_button = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()

    def fill_form(self, first_name, last_name, email, mobile, address):
        self.wait_for_visibility(self.FIRST_NAME).send_keys()
        time.sleep(3)
        self.find_element(self.LAST_NAME).send_keys(last_name)
        self.find_element(self.EMAIL_FIELD).send_keys(email)
        self.find_element(self.MOBILE).send_keys(mobile)
        self.find_element(self.ADDRESS).send_keys(address)

    def submit_form(self):
        self.wait_for_visibility(self.SUBMIT_BUTTON)
        self.remove_ads()
        submit_button = self.find_element(self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def is_submission_successful(self):
        try:
            self.wait_for_visibility((By.CLASS_NAME, "modal-title"))
            return self.find_element((By.CLASS_NAME, "modal-title")).is_displayed()
        except:
            return False

    def upload_image(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../resources/hanuman.jpg"))
        upload = self.wait_for_visibility(self.UPLOAD_BUTTON)
        upload.send_keys(file_path)
        time.sleep(5)