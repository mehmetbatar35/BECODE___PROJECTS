
import sys
from bs4 import BeautifulSoup as bs
import requests
import re
import json
import pandas as pd


class Property:
    def __init__(self):
        self.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
}
        self.first_url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&priceType=SALE_PRICE&page=1&orderBy=relevance"

        self.property_links : list[str] = []
        self.property_list : list[str] = []

        self.soup = self.get_soup(self.first_url)
        links = self.get_links()
        self.property_links.extend(links)

        self.get_details()
        self.get_csv_file()

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
        # all_properties = []
        for link in self.property_links:
            soup = self.get_soup(link)
            property_json = self.get_property_json(soup)

        # all_properties.append(property_json)
        # with open("PROPERTIES.json", 'w') as f:
        #     json.dump(all_properties, f, indent = 4)

        prop_dict = {}

        prop_dict['Locality'] = property_json['property']['location']['postalCode']
        prop_dict['Type of Property'] = property_json['property']['type']
        prop_dict['Subtype of Property'] = property_json['property']['subtype']
        prop_dict ["Price"] = property_json['price']['mainValue']
        prop_dict ["Type of Sale"] = property_json['transaction']['type']
        prop_dict ["Number of rooms"] = property_json['property']['bedroomCount']
        prop_dict ["Living Area"] = property_json["property"]["netHabitableSurface"]


        self.property_list.append(prop_dict)

    def get_property_json(self, soup):
        json_scripts = soup.find_all('script', attrs = {'type': 'text/javascript'})
        for script in json_scripts:
            if 'window.classified' in script.text:
                json_text = script.text.replace('window.classified = ', '').replace(';', '')
                property_data = json.loads(json_text)
                return property_data
    def get_csv_file(self):
        df = pd.DataFrame(self.property_list)
        df.to_csv('bakBakalimDogru_Mu.csv', index = False)
        print("File SAVED.")


prop = Property()

# for index, link in enumerate(prop.property_links, start=1):
#     print(f"{index}. {link}")






















