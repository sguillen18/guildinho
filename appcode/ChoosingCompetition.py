#-- /Users/sean.guillen/Documents/python/datascience/SoccermaticsForPython-master --#
import json
from pandas import json_normalize
#from PlotShotsAndPassesForPlayer import plotShotsAndPasses


#Get Competition Loaded and Selected
comp_file_name='open-data-master/data/competitions.json'
with open(comp_file_name) as data_file:
        data=json.load(data_file)
        #parse out json
        df = json_normalize(data, sep = "_")
        de = df[["competition_name", "season_name", "competition_id", "season_id"]]
        print(de[['competition_name', 'season_name']])


comp_id = input("Enter your competition ID: ")

selectedDf = (de.iloc[[comp_id]])
selectedCompId=str(selectedDf.iloc[0]['competition_id'])
selectedSeasonId=str(selectedDf.iloc[0]["season_id"])



#Get Matches Loaded and Selected
match_file_name='open-data-master/data/matches/' + selectedCompId + "/" + selectedSeasonId +'.json'

with open(match_file_name) as matches_file:
        matches_data=json.load(matches_file)
        matches_df = json_normalize(matches_data, sep = "_")
        cleaned_matches_df = matches_df[["match_id", "home_team_home_team_name", "away_team_away_team_name", "competition_stage_name"]]
        
for ind in cleaned_matches_df.index:
    print(ind,cleaned_matches_df['competition_stage_name'][ind], ": ", cleaned_matches_df['home_team_home_team_name'][ind], " vs ", cleaned_matches_df['away_team_away_team_name'][ind])
    
match_input = input("Enter your match ID: ")

selected_matchDf = (cleaned_matches_df.iloc[[match_input]])
selected_matchId = str(selected_matchDf.iloc[0]["match_id"])


#Get Players Loaded and Selected
events_file_name = 'open-data-master/data/events/' + selected_matchId + '.json'

with open(events_file_name) as event_file:
        event_data=json.load(event_file)
        event_df=json_normalize(event_data, sep="_")
        players_df=json_normalize(event_df['tactics_lineup'], sep="_")
        home_team_players = players_df.iloc[0]
        away_team_players = players_df.iloc[1]
        
        #converting to a dataframe so i can use iterrows or other things that a series cannot do
        home_team_players = home_team_players.reset_index(name='players')
        away_team_players = away_team_players.reset_index(name='players')

while True:
    select_team = input("Chose between tracking a home team player or an away team player by selecting 1 or 2\n1. Home Team \n2. Away Team\n")
    if select_team == '1':
        for index, row in home_team_players.iterrows():
            player_name=row['players']['player_name']
            print(f"{index}: {player_name}")
        break
    elif select_team == '2':
        for index, row in away_team_players.iterrows():
            player_name=row['players']['player_name']
            print(f"{index}: {player_name}")
        break
    else:
        print("Invalid input. Please try again")
        
player_index = int(input("Enter the number next to the player you'd like stats from: \n"))

player_name =away_team_players.iloc[player_index]['players']['player_name']
print(player_name)

#plotShotsAndPasses(match_file_name, select_team, player_name)

        