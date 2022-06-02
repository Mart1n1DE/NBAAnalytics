import snowflake.connector
import os

#connect to snowflake and set cursor
ctx = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT")
    )
cs = ctx.cursor()
try:
    cs.execute("CREATE OR REPLACE DATABASE nbadatabase")
    cs.execute("CREATE OR REPLACE TABLE CommonNbaStats (name string, team string, position float, minutes integer, adjusted_plus_minus_per_48 float, wins_produced_per_48 float, wins_produced float, points_over_par_per_48 float, points_per_48 float, rebounds_per_48 float, assists_per_48 float)")
    cs.execute("PUT FILE://D:/Projects/NBAAnalytics/boxscoregeeks/*.csv @")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()