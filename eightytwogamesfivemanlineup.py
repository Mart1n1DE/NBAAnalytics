import pandas as pd
from bs4 import BeautifulSoup as bs 
import urllib.request

teams = ['ATL','BOS','BKN','CHA','CHI','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
years = ['0708','0809','0910','1011','1112','1213','1314','1415','1516','1617','1718','1819','1920','2021','2122']
df = pd.DataFrame()
#iterate through years and teams and concatenate data into a single data frame
for year in years:
    for team in teams: 
        #renaming teams that used to have a different name
        if int(year[:2]) <8 and team == 'OKC':
            team = 'SEA'
        if int(year[:2])<12 and team == 'BKN':
            team = 'NJN'
        if int(year[:2])<14 and team == 'NOP':
            team = 'NOH' 
        url = 'http://www.82games.com/' + year + '/' + year + team + '2.HTM'
        print(url)
        source = urllib.request.urlopen(url)
        soupdata = bs(source, 'lxml')
        table = soupdata.find_all('table')
        #there may be a more efficient way to do this as every concat requires reallocation of memory, i may revisit this 
        fivemanunit = pd.concat([df,pd.read_html(str(table))[4]])
        fivemandetails = pd.concat([df,pd.read_html(str(table))[5]]) 
    fivemanunit.to_csv(r"./eightytwogames/fivemanunitdata" + year + ".csv",index = False)
    fivemandetails.to_csv(r"./eightytwogames/fivemandetailsdata" + year + ".csv",index = False)
