import pandas as pd
from bs4 import BeautifulSoup as bs 
import urllib.request
from pathlib import Path

teams = ['ATL','BOS','BKN','CHA','CHI','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
years = ['0708','0809','0910','1011','1112','1213','1314','1415','1516','1617','1718','1819','1920','2021','2122']

#create directory for csv files if directory does not exist
output_dir = Path(r'./eightytwogames')
output_dir.mkdir(parents = True, exist_ok = True)

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
        #send request for urldata and parse using beautifulsoup and pandas
        source = urllib.request.urlopen(url)
        soupdata = bs(source, 'lxml')
        table = soupdata.find_all('table')
        #there may be a more efficient way to do this as every concat requires reallocation of memory, i may revisit this 
        fivemanunit = pd.read_html(str(table))[4]
        fivemandetails = pd.read_html(str(table))[5]
        #create new columns in each table to store team and year
        teamcolumn = ["Team"] + [team]*(len((fivemanunit.index))-1)
        fivemanunit.insert(0,"DummyHeader",teamcolumn)
        yearcolumn = ["Year"] + [year]*(len((fivemanunit.index))-1)
        fivemanunit.insert(0,"DummyHeader2",yearcolumn)
        teamcolumn = ["Team"] + [team]*(len((fivemandetails.index))-1)
        fivemandetails.insert(0,"DummyHeader",teamcolumn)
        yearcolumn = ["Year"] + [year]*(len((fivemandetails.index))-1)
        fivemandetails.insert(0,"DummyHeader2",yearcolumn)
        #save csv files without pandas index
        outputfile_fivemanunit = "fivemanunitdata" + year + team + ".csv"
        outputfile_fivemandetails = "fivemandetailsdata" + year + team + ".csv"
        fivemanunit.to_csv(output_dir / outputfile_fivemanunit, index = False)
        fivemandetails.to_csv(output_dir / outputfile_fivemandetails, index = False)
