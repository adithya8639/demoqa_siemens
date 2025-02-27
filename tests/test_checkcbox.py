import time
from pages.checkbox_page import CheckboxPage
from utils import logger

def test_checkbox(driver):
    checkbox_page = CheckboxPage(driver)

    logger.log_info("Navigating to elements -> checkbox")
    checkbox_page.navigate_to_checkbox()

    logger.log_info("Click on + icon to expand tree")
    checkbox_page.expand_tree()

    logger.log_info("Click on home checkcbox (parent node)")
    checkbox_page.select_home_checkbox()
    time.sleep(5)

    logger.log_info("Verifying selected checkboxes")
    assert checkbox_page.are_checkboxes_selected()