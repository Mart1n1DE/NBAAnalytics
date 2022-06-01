from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats as ps 
from nba_api.stats.endpoints import playerdashboardbyshootingsplits as ss 
from nba_api.stats.endpoints import commonplayerinfo as cp
from pathlib import Path
import time

#create directory for csv files if directory does not exist
output_dir = Path(r'./nbaAPIdata')
output_dir.mkdir(parents = True, exist_ok = True)

# fetch all active nba players and iterate through them
nba_players = players.get_active_players()
for player in nba_players:
    #the api has a maximum amount of requests per second so time.sleep must be used
    time.sleep(1)
    #obtain player id from JSON structure and use id to further use API
    playerid = player['id']
    playerteam = cp.CommonPlayerInfo(player_id = playerid)
    time.sleep(1)
    playerdata = playerteam.get_data_frames()[0]
    team = playerdata['TEAM_ABBREVIATION'][0]
    name = playerdata['LAST_NAME'][0]
    career = ss.PlayerDashboardByShootingSplits(player_id = playerid)
    time.sleep(1)
    career = career.get_data_frames()[3]
    if (not career.empty):
        teamcolumn = [team]*(len((career.index)))
        namecolumn = [name]*(len((career.index)))
        career.insert(0,"Team",teamcolumn)
        career.insert(0,"Name",namecolumn)    
        print(career)
        #save relevant data into csv
        output_file = str(playerid) + ".csv"
        career.to_csv(output_dir/output_file, index = False)
    




