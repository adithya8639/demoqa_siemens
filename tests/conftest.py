import pytest
import logging
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@pytest.fixture
def driver():
    logging.info("Starting WebDriver...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    logging.info("Closing WebDriver...")
    driver.quit()
