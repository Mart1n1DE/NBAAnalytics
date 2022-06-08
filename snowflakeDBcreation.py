import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import os
import pandas as pd 
from pathlib import Path

#connect to snowflake and set cursor
ctx = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT")
    )
cs = ctx.cursor()
#create new database and associated tables
try:
    cs.execute("CREATE OR REPLACE DATABASE nbadatabase")
    cs.execute("USE DATABASE nbadatabase")
    cs.execute("USE SCHEMA public")
    cs.execute('CREATE OR REPLACE TABLE "CommonNbaStats" ("Year" integer, "name" string, "team" string, "position" float,"games_played" integer, "minutes" integer, "adjusted_plus_minus_per_48" float, "wins_produced_per_48" float, "wins_produced" float, "points_over_par_per_48" float, "points_per_48" float, "rebounds_per_48" float, "assists_per_48" float)')
    cs.execute('CREATE OR REPLACE TABLE "IndividualPlayerStats" ("Year" string, "Team" string, "Player" string, "Min" string, "Own" string, "Opp" float, "Production_Net" float, "On" float, "Off" float, "Net" float, "Rating" float)')
    cs.execute('CREATE OR REPLACE TABLE "FiveManUnitStats" ("Year" string, "Team" string, "#" integer, "Unit" string, "Min" integer, "Off" float, "Def" float, "+/-" integer, "W" integer, "L" integer, "Win%" float)')
    cs.execute('CREATE OR REPLACE TABLE "FiveManUnitDetails" ("Year" string, "Team" string, "#" integer, "Unit" string, "eFG" float, "eFGA" float, "FTA" integer, "Close" string, "dClose" string, "Reb" string, "T/O" string)')
    cs.execute('CREATE OR REPLACE TABLE "NBAAPIshotdetails" ("Name" string, "Team" string, "GROUP_SET" string, "GROUP_VALUE" string, "FGM" integer, "FGA" integer, "FG_PCT" float, "FG3M" integer, "FG3A" integer, "FG3_PCT" float, "EFG_PCT" float, "BLKA" integer, "PCT_AST_2PM" float, "PCT_UAST_2PM" float, "PCT_AST_3PM" float, "PCT_UAST_3PM" float, "PCT_AST_FGM" float, "PCT_UAST_FGM" float, "FGM_RANK" integer, "FGA_RANK" integer, "FG_PCT_RANK" integer, "FG3M_RANK" integer, "FG3A_RANK" integer, "FG3_PCT_RANK" integer, "EFG_PCT_RANK" integer ,"BLKA_RANK" integer,"PCT_AST_2PM_RANK" integer,"PCT_UAST_2PM_RANK" integer,"PCT_AST_3PM_RANK" integer,"PCT_UAST_3PM_RANK" integer,"PCT_AST_FGM_RANK" integer,"PCT_UAST_FGM_RANK" integer,"CFID" integer, "CFPARAMS" string)')

finally:
    cs.close()
ctx.close()