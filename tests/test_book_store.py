from pages.book_store_page import BookStorePage
from utils import logger

def test_book_store_data(driver):
    book_store_page = BookStorePage(driver)

    logger.log_info("Navigated to the book store page")
    book_store_page.navigate_to_book_store()

    displayed_books = book_store_page.get_displayed_books()
    logger.log_info(f"Retrieved displayed books: {displayed_books}")

    api_books = book_store_page.get_books_from_api()
    logger.log_info(f"Retrieved books from API: {api_books}")

    assert displayed_books == api_books, f"Book list mismatch: {displayed_books}\nAPI: {api_books}"
