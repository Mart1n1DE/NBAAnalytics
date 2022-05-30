from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats as ps 
from nba_api.stats.endpoints import playerdashboardbyshootingsplits as ss 

# get_teams returns a list of 30 dictionaries, each an NBA team.
# nba_players = players.get_active_players()
# print('Number of players fetched: {}'.format(len(nba_players)))
# print(nba_players[:3])
career = ss.PlayerDashboardByShootingSplits(player_id = '203500')
career = career.get_data_frames()[3]
print(career)
