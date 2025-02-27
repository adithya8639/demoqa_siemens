from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from config.config import BASE_URL


class DynamicPropertiesPage(BasePage):
    ELEMENTS_MENU = (By.XPATH, "//h5[text()='Elements']/parent::div/preceding-sibling::div[@class='card-up']")
    DYNAMIC_PROP_BUTTON = (By.XPATH, "//span[text()='Dynamic Properties']")
    DYNAMIC_BUTTON = (By.ID, "visibleAfter")
    COLOR_CHANGE_BUTTON = (By.ID, "colorChange")

    def navigate_to_dynamic_properties(self):
        self.visit(BASE_URL)
        self.wait_for_visibility(self.ELEMENTS_MENU)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.find_element(self.ELEMENTS_MENU))
        self.click(self.ELEMENTS_MENU)
        self.wait_for_visibility(self.DYNAMIC_PROP_BUTTON)

        dynamic_button = self.find_element(self.DYNAMIC_PROP_BUTTON)
        self.driver.execute_script("arguments[0].click();", dynamic_button)

    def wait_for_button(self):
        self.wait_for_visibility(self.DYNAMIC_BUTTON)

    def refresh_page(self):
        self.driver.refresh()

    def wait_for_color_change(self, old_color):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*self.COLOR_CHANGE_BUTTON).value_of_css_property("color") != old_color)
