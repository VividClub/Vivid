from email import header
import requests
from bs4 import BeautifulSoup

# API Documentation : https://docs.opensea.io/reference/retrieving-a-single-collection

class Scraper:
    def __init__(self):
        self.TheDotCollection = ''
        
    def scrape_collection_info(self):
        URL = "https://api.opensea.io/api/v1/collection/the-colors-dot-art"
        #URL = "https://api.opensea.io/api/v1/collection/doodles-official"
        
        response = requests.request("GET", URL)
        
        print(response.text) 
        
    def scrape_assets(self):
        #URL = "https://api.opensea.io/api/v1/collection/the-colors-dot-art"
        URL = "https://api.opensea.io/api/v1/assets?order_by=pk&order_direction=desc&limit=20&offset=0"
        
        headers = {"Accept": "application/json"}
        
        response = requests.request("GET", URL, headers=headers)
        
        print(response.text)