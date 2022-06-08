import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import os
import pandas as pd 
from pathlib import Path
import json

#function created to store files with errors into error log json file
def write_to_error_log(error_json, jsonfilename):
    with open(jsonfilename,'r+') as file:
        file_data = json.load(file)
        file_data["error_files"].append(error_json)
        file.seek(0)
        json.dump(file_data, file, indent = 4)


#define file directories and Snowflake table names for data sources
boxscoregeeks = {
    "dir": "./boxscoregeeks",
    "table": "CommonNbaStats"
}

eightytwogamesindividualstats = {
    "dir": "./eightytwogames",
    "table": "IndividualPlayerStats"
}

eightytwogamesfivemanunit = {
    "dir": "./eightytwogamesfivemanunit",
    "table": "FiveManUnitStats"
}

eightytwogamesfivemandetails = {
    "dir": "./eightytwogamesfivemandetails",
    "table": "FiveManUnitDetails"
}

nbaapidata = {
    "dir": "./nbaAPIdata",
    "table": "NBAAPIshotdetails"
}

#create error log json file
json_obj = {}
json_obj['error_files'] = []
error_json_file_name = 'error.json'
with open(error_json_file_name,'w') as f:
    json.dump(json_obj,f)

#boxscoregeeks,eightytwogamesindividualstats,
listofdatasources = [eightytwogamesfivemanunit,eightytwogamesfivemandetails]

#connect to snowflake and set cursor
ctx = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT")
    )
cs = ctx.cursor()

#truncate table and load data into Snowflake table
try:
    cs.execute("USE DATABASE nbadatabase")
    cs.execute("USE SCHEMA public")

    for datasource in listofdatasources:
        cs.execute('TRUNCATE TABLE "' + datasource["table"] + '"')
        listoffiles = os.listdir(datasource["dir"])
        output_dir = Path(datasource["dir"])
        
        for file in listoffiles:
            df = pd.read_csv(output_dir / file, header = 0, sep = ",")
            print(file)
            #try to load data to Snowflake
            try:
                write_pandas(ctx,df,table_name = datasource["table"])
            #if error occurs during loading of csv, then update error json file to correct later
            except:
                error_json = {
                    'table':datasource["table"],
                    'dir':datasource["dir"],
                    'file':file
                }
                write_to_error_log(error_json,error_json_file_name)
finally:
    cs.close()
ctx.close() 