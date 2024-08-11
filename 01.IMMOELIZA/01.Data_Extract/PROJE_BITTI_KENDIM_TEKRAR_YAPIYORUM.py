
import sys
from bs4 import BeautifulSoup as bs
import requests
import re


# Set console encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&priceType=SALE_PRICE&page=1&orderBy=relevance"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
}

response = requests.get(url, headers = headers)

soup = bs(response.text, 'html.parser')

listings = soup.find_all('a', class_ = 'card__title-link')

links = [listing.get('href') for listing in listings if listing.get('href') ]

for link in links:
    property_response = requests.get(link, headers = headers)
    property_soup = bs(property_response.text, 'html.parser')
    script_tag = property_soup.find('script', text = re.compile(r'window\.classified'))