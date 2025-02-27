from pages.dynamic_properties_page import DynamicPropertiesPage
from utils import logger

def test_dynamic_button(driver):
    dynamic_page = DynamicPropertiesPage(driver)

    logger.log_info("Navigating to Dynamic Properties page")
    dynamic_page.navigate_to_dynamic_properties()

    logger.log_info("Waiting for the dynamic button to become visible")
    dynamic_page.wait_for_button()

    logger.log_info("verify wheather dynamic button dispalyed")
    assert dynamic_page.find_element(dynamic_page.DYNAMIC_BUTTON).is_displayed()
    logger.log_info("Dynamic button displayed")


def test_button_color_change(driver):
    dynamic_page = DynamicPropertiesPage(driver)

    logger.log_info("Navigating to Dynamic Properties page")
    dynamic_page.navigate_to_dynamic_properties()
    old_color = dynamic_page.find_element(dynamic_page.COLOR_CHANGE_BUTTON).value_of_css_property("color")

    logger.log_info("Waiting for the button color to change")
    dynamic_page.wait_for_color_change(old_color)
    new_color = dynamic_page.find_element(dynamic_page.COLOR_CHANGE_BUTTON).value_of_css_property("color")

    logger.log_info("Validating that the button color has changed")
    assert old_color != new_color
    logger.log_info("Successfully button color has changed")
