from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
options.add_experimental_option('excludeSwitches', ['enable-logging'])

for year in range(1977,2022):
    url = "https://www.boxscoregeeks.com/players?sort=minutes&direction=desc&season=" + str(year)
    #using Selenium for a GET request to a dynamic page
    driver = webdriver.Chrome(options = options, executable_path=r"./chromedriver.exe")                                    
    driver.get(url)                 
    #table is dynamically loaded using JavaScript so I need to wait before parsing data 
    #sleep was the best solution since Selenium's wait for class function does not work with this website
    time.sleep(3)
    soupdata = bs(driver.page_source)
    table = soupdata.find("table")   
    df = pd.read_html(str(table))
    playerdata = df[0]
    print(playerdata)
    #rename columns
    playerdata.columns = ['name','team','position','games_played','minutes','adjusted_plus_minus_per_48','wins_produced_per_48','wins_produced','points_over_par_per_48','points_per_48','rebounds_per_48','assists_per_48']
    yearcolumn = [year]*(len((playerdata.index)))
    #insert newly created year column
    playerdata.insert(0,"Year",yearcolumn) 
    #write dataframe to csv file
    output_file = str(year) + str(year+1) + ".csv"
    playerdata.to_csv(output_dir / output_file, index = False)
    print("success" + str(year))
    driver.quit()                     