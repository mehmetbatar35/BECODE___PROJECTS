# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options = chrome_options)
# driver.get("https://fr.whoscored.com/Matches/1818891/MatchReport/Belgique-Jupiler-Pro-League-2024-2025-Genk-Westerlo")
driver.get("https://fr.whoscored.com/Matches/1818891/MatchReport/Belgique-Jupiler-Pro-League-2024-2025-Genk-Westerlo")


# score = driver.find_element(By.CLASS_NAME, value = "col12-lg-4 col12-m-4 col12-s-2 col12-xs-0 result")
# score = driver.find_element(By.CLASS_NAME , value = "col12-lg-4 col12-m-4 col12-s-2 col12-xs-0 result")
score = driver.find_element(By.CLASS_NAME , "result")
print(score.text)


driver.quit()