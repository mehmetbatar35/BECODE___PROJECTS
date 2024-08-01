

from bs4 import BeautifulSoup as bs
import requests


url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&priceType=SALE_PRICE&page=1&orderBy=relevance"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
}

response = requests.get(url, headers = headers)

soup = bs(response.text, 'html.parser')

listings = soup.find_all('a', class_ = 'card__title-link')

print(listings)