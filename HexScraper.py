import requests
from bs4 import BeautifulSoup

def scrape_hexvalues():
    URL = "https://opensea.io/collection/the-colors-dot-art"
    page = requests.get(URL)
    print(page.text) # Returning a security alert, have to work with api 