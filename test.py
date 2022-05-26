from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd
from bs4 import BeautifulSoup as bs
import time

options = Options()                 
options.add_argument("--headless")   

for year in range(2020,2022):
    year = str(year)
    url = "https://www.boxscoregeeks.com/players?sort=minutes&direction=desc&season=" + year
    #using Selenium for a GET request to a dynamic page
    driver = webdriver.Firefox(options = options, executable_path=r"D:/Projects/NBAAnalytics/geckodriver.exe")                                    
    driver.get(url)                 
    #table is dynamically loaded using JavaScript so I need to wait before parsing data 
    #sleep was the best solution since Selenium's wait for class did not work
    #I may revisit to solve later 
    time.sleep(5)
    soupdata = bs(driver.page_source)
    table = soupdata.find("table")   
    df = pd.read_html(str(table))
    df[0].to_csv(r"D:/Projects/NBAAnalytics/boxscoregeeks/" + year + ".csv",index = False)
    print (df)                    
    driver.quit()                     