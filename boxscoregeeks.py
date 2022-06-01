from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd
from bs4 import BeautifulSoup as bs
import time
from pathlib import Path

#create directory for csv files if directory does not exist
output_dir = Path(r'./boxscoregeeks')
output_dir.mkdir(parents = True, exist_ok = True)

#prevents browser from opening up
options = Options()                 
options.add_argument("--headless")   

for year in range(1977,2022):
    url = "https://www.boxscoregeeks.com/players?sort=minutes&direction=desc&season=" + str(year)
    #using Selenium for a GET request to a dynamic page
    driver = webdriver.Firefox(options = options, executable_path=r"./geckodriver.exe")                                    
    driver.get(url)                 
    #table is dynamically loaded using JavaScript so I need to wait before parsing data 
    #sleep was the best solution since Selenium's wait for class function does not work with this website
    time.sleep(5)
    soupdata = bs(driver.page_source)
    table = soupdata.find("table")   
    df = pd.read_html(str(table))
    output_file = str(year) + str(year+1) + ".csv"
    df[0].to_csv(output_dir / output_file, index = False)
    driver.quit()                     