import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import csv


class Property:
    def __init__(self):
        self.property_list : list[str] = []

        self.cheat_immo = {
                "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)            Chrome/91.0.4472.124 Safari/537.36"
            }
        self.appartment_root_url : list[str] = [
            f"https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&priceType=SALE_PRICE&page={i}&orderBy=relevance"
            for i in range(1, 334)
        ]
        self.house_root_url : list[str] = [
            f"https://www.immoweb.be/en/search/house/for-sale?countries=BE&priceType=SALE_PRICE&page={i}&orderBy=relevance"
            for i in range(1, 334)
        ]

        for url in self.appartment_root_url:
            self.soup = self.get_soup(url)
            list_of_links = self.get_links()
            self.property_list.extend(list_of_links)

        for url in self.house_root_url:
            self.soup = self.get_soup(url)
            list_of_links = self.get_links()   
            self.property_list.extend(list_of_links)

        self.get_details()    
        self.get_csv_file()

    def get_soup(self, url):
        response = requests.get(url, headers = self.cheat_immo)
        soup = bs(response.content, 'html.parser')
        return soup
    
    def get_links(self):
        list_links = []

        maison_link_soup = self.soup.find_all('a', attrs = {'class': 'card__title-link'})

        for link in maison_link_soup:
            list_links.append(link['href'])
        return list_links
        
    def get_details(self):
        for link in self.property_list:
            if "new-real-estate-project" in link:
                continue
            soup = self.get_soup(link)
            property_json = self.get_property_json(soup)

            prop_dict = {}
            # prop_dict ["Locality"] = property_json["property"]["location"]["postalCode"]
            # try:
            #     prop_dict["Locality"] = property_json["property"]["location"]["postalCode"]
            # except (KeyError, TypeError, AttributeError):
            #     prop_dict["Locality"] = None 
            prop_dict ["Type of property"] = property_json["property"]["type"]  
            # prop_dict ["Subtype of property"] = property_json["property"]["subtype"]
            # prop_dict ["Price"] = property_json['price']['mainValue']
            # for i in property_json['flags']:
            #     if property_json['flags'][i] == True:
            #         type_of_sale = i
            # prop_dict ["Type of Sale"] = type_of_sale
            # prop_dict ["Number of rooms"] = property_json['property']['bedroomCount']
            # prop_dict ["Living Area"] = property_json["property"]["netHabitableSurface"]
            # if property_json["property"]['kitchen'] and property_json["property"]['kitchen']['type'] != None:
            #     prop_dict ["Kitchen Fully Equiped"] = True if "HYPER" in property_json["property"]['kitchen']['type'] else False
            # else:   
            #     prop_dict ["Kitchen Fully Equiped"] = False
            # prop_dict ["Furnished"] = True if property_json['transaction']['sale']['isFurnished'] else False
            # prop_dict ["Open fire"] = True if property_json['property']['fireplaceExists'] else False
            # prop_dict ["Terrace"] = property_json['property']['terraceSurface'] if property_json['property']['hasTerrace'] else 0
            # prop_dict ["Garden"] = property_json['property']['gardenSurface'] if property_json['property']['hasGarden'] else 0
            # prop_dict ["Surface Land"] = property_json["property"]['land']["surface"] if property_json["property"]['land'] else None
            # prop_dict ["Number of facades"] = property_json['property']['building']['facadeCount'] if property_json['property']['building'] else None
            # prop_dict ["Swimming Pool"] = True if property_json['property']['hasSwimmingPool'] else False
            # prop_dict ["State of the building"] = property_json["property"]['building']["condition"] if property_json["property"]['building'] else None
            self.property_list.append(prop_dict)




    def get_property_json(self, soup):
        json_link = soup.find_all('script', attrs = {"type": "text/javascript"})
        for i in json_link:
            if 'window.classified' in i.text:
                i = i.text.replace("window.classified = ", "").replace(";", "")
                i = json.loads(i)
                return i
        
    def get_csv_file(self):
        df = pd.DataFrame(self.property_list)
        df.to_csv("6_JULY.csv", index = False)
        print("File created successfully")


