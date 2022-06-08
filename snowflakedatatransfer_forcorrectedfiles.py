import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import os
import pandas as pd 
from pathlib import Path
import json

error_json_file_name = 'error.json'

file_data = []

with open(error_json_file_name,'r+') as file:
    file_data = json.load(file)

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

    for file in file_data["error_files"]:
        csv_location = file['dir'] +'/' + file['file']
        df = pd.read_csv(csv_location, header = 0, sep = ",")
        #try to loading corrected data to Snowflake
        try:
            write_pandas(ctx,df,table_name = file['table'])
        #if error occurs during loading of csv, then print error occured
        except:
            print('error occured loading fixed data')
finally:
    cs.close()
ctx.close() 