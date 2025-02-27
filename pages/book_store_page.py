import requests
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL
import time
from config.config import API_URL

class BookStorePage(BasePage):
    BOOK_STORE_MENU = (By.XPATH, "//h5[text()='Book Store Application']")
    BOOK_STORE_BUTTON = (By.XPATH, "//span[text()='Book Store']")
    BOOK_TITLES = (By.XPATH, "//span[@class='mr-2']")
    FIXED_BANNER = (By.ID, "fixedban")

    def remove_ads(self):
        try:
            banner = self.driver.find_element(*self.FIXED_BANNER)
            self.driver.execute_script("arguments[0].remove();", banner)
        except:
            pass

    def navigate_to_book_store(self):
        self.visit(BASE_URL)
        self.wait_for_visibility(self.BOOK_STORE_MENU)
        self.remove_ads()
        book_store_menu = self.find_element(self.BOOK_STORE_MENU)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", book_store_menu)
        self.driver.execute_script("arguments[0].click();", book_store_menu)
        self.wait_for_visibility(self.BOOK_STORE_BUTTON)
        self.driver.execute_script("arguments[0].click();", self.find_element(self.BOOK_STORE_BUTTON))

    def get_displayed_books(self):
        self.wait_for_visibility(self.BOOK_TITLES)
        time.sleep(2)
        return [book.text.strip() for book in self.driver.find_elements(*self.BOOK_TITLES)]

    def get_books_from_api(self):
        response = requests.get(API_URL)
        assert response.status_code == 200, f"API request failed! Status: {response.status_code}"
        books_data = response.json().get("books", [])
        return [book["title"].strip() for book in books_data]
