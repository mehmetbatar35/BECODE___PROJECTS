from bs4 import BeautifulSoup as bs
import requests


def __init__(self):
    pass


url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
    }

html = requests.get(url, headers= headers).content

soup = bs(html, "html.parser")

links = soup.find_all('a', {"class" : "card__title-link"})

hrefs = [link.get('href') for link in links]

for href in hrefs:
    print(href)

