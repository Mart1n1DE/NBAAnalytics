import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

url = "https://www.boxscoregeeks.com/players?sort=minutes&direction=desc"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
browser = webdriver.PhantomJS()
time.sleep(10)
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html,'lxml')

print(soup.prettify())