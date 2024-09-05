from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import pandas as pd
import urllib.request


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options = chrome_options)
# driver.get("https://www.whoscored.com/Regions/22/Tournaments/18/Seasons/10304/Belgique-Jupiler-Pro-League")
driver.get("https://www.football-data.co.uk/belgiumm.php")


link_elements = driver.find_elements(By.LINK_TEXT, 'Jupiler League')

csv_files = []

for index, i in enumerate(link_elements):
    if index < 5:
        href = i.get_attribute('href')
        csv_files.append(href)

for  index, i in enumerate(csv_files):
    print((index + 1), i)

directory = 'csv_files'
if not os.path.exists(directory):
    os.makedirs(directory)


for index, url in enumerate(csv_files):
    file_name = os.path.join(directory, f"{url.split("/")[-2]}.csv")
    print(file_name)
    urllib.request.urlretrieve(url, file_name)
print("All files downloaded successfully")


driver.quit()




# dfs = []

# for file_name in os.listdir(directory):
#     if file_name.endswith(".csv"):
#         file_path = os.path.join(directory, file_name)
#         df = pd.read_csv(file_path)
#         dfs.append(df)

# merged_df = pd.concat(dfs, ignore_index= True)

# merged_file_path = 'merged_file.csv'
# merged_df.to_csv(merged_file_path, index = False)

# print(f"All files merged successfully into  'merged_file_path'")




# score = driver.find_element(By.CLASS_NAME, value = "col12-lg-4 col12-m-4 col12-s-2 col12-xs-0 result")
# score = driver.find_element(By.CLASS_NAME , value = "col12-lg-4 col12-m-4 col12-s-2 col12-xs-0 result")
# score = driver.find_element(By.CLASS_NAME , "result")
# print(score.text)




# href_value = driver.find_element(By.ID, 'statsBtn-1818891').get_attribute('href')
# print(href_value)
# driver.quit()