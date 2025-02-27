import requests
from config.config import BOOKSTORE_API_URL

def fetch_books():
    response = requests.get(BOOKSTORE_API_URL)
    return response.json()["books"]
