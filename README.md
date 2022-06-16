# NBA Analytics

## Description

This project allowed me to scrape data from the web, load it into Snowflake libraries, then build aggregations and visualizations on top of the data. For the process in building this project please visit https://martinhleung.com/portfolios#nbaproject. An example dashboard:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="http://martinhleung.com/wp-content/uploads/2022/06/BI-screenshot-1.png">
  <img alt="Power BI visualization of Jokic" src="http://martinhleung.com/wp-content/uploads/2022/06/BI-screenshot-1.png">
</picture>

## Installation and Usage

1. Create a Python environment and install from requirements.txt.
2. Create a Snowflake account and update environment variables with relevant user, password,and account data. 
3. Run the python scripts in the order of boxscoregeeks.py,eightytwogames.py,eightytwogamesfivemanlineup.py,snowflakeDBcreation.py,snowflakedatatransfer.py
4. Check error.json for csvs with errors that you would like to use then run snowflakedatatransfer_forcorrectedfiles.py
5. Connect visualization tool to Snowflake database 

### Heroku Usage
It is possible to schedule this project on Heroku. First, you must install Chromedriver via https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/.
Then, deploy repository onto Heroku and start from instruction 2. 
