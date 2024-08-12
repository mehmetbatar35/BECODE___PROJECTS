
import sys
from bs4 import BeautifulSoup as bs
import requests
import re
import json


class Property:
    def __init__(self):
        self.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
}
        self.first_url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&priceType=SALE_PRICE&page=1&orderBy=relevance"

        self.property_links : list[str] = []

        self.soup = self.get_soup(self.first_url)
        links = self.get_links()
        self.property_links.extend(links)

        self.get_details()





    def get_soup(self, url):
        response = requests.get(url, headers = self.headers)
        soup = bs(response.content, 'html.parser')
        return soup
    
    def get_links(self):
        list_links = []
        all_links = self.soup.find_all('a', attrs = {'class': 'card__title-link'})
        for link in all_links:
            list_links.append(link['href'])
        return list_links    
    
    def get_details(self):
        all_properties = []
        for link in self.property_links:
            soup = self.get_soup(link)
            property_json = self.get_property_json(soup)
        all_properties.append(property_json)

        with open("PROPERTIES.json", 'w') as f:
            json.dump(all_properties, f, indent = 4)

    def get_property_json(self, soup):
        json_scripts = soup.find_all('script', attrs = {'type': 'text/javascript'})
        for script in json_scripts:
            if 'window.classified' in script.text:
                json_text = script.text.replace('window.classified = ', '').replace(';', '')
                property_data = json.loads(json_text)
                return property_data


prop = Property()

for index, link in enumerate(prop.property_links, start=1):
    print(f"{index}. {link}")






















