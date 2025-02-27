from faulthandler import is_enabled

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.config import BASE_URL
from utils import logger

class CheckboxPage(BasePage):
    ELEMENTS_MENU = (By.XPATH, "//h5[text()='Elements']/parent::div/preceding-sibling::div[@class='card-up']")
    CHECKBOX_BUTTON = (By.XPATH, "//span[text()='Check Box']")
    EXPAND_BUTTON = (By.CLASS_NAME, "rct-option-expand-all")
    HOME_CHECKBOX_LABEL = (By.XPATH, "//span[@class='rct-checkbox']")

    def navigate_to_checkbox(self):
        self.visit(BASE_URL)
        self.click(self.ELEMENTS_MENU)
        self.click(self.CHECKBOX_BUTTON)

    def expand_tree(self):
        self.click(self.EXPAND_BUTTON)

    def select_home_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.HOME_CHECKBOX_LABEL)).click()

    def are_checkboxes_selected(self):
        checkboxes = self.find_elements(self.HOME_CHECKBOX_LABEL)
        if not checkboxes:
            logger.log_info("No checkboxes found!")
            return False
        selected_status = []
        for index, checkbox in enumerate(checkboxes, start=1):
            try:
                svg_icon = checkbox.find_element(By.TAG_NAME, "svg")
                class_attribute = svg_icon.get_attribute("class")
                is_selected = "rct-icon-check" in class_attribute
                selected_status.append(is_selected)
                logger.log_info(" ".join(["Checkbox", str(index) + ":", "Selected" if is_selected else "Not Selected"]))
            except Exception as e:
                print(f"Error checking Checkbox {index}: {e}")
                selected_status.append(False)
        return all(selected_status)