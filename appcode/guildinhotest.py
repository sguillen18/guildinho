import json
import os
import pandas as pd

#fetches the list of competitions
def get_competitions():
    # Get the current working directory
    current_dir = os.getcwd()

    # Define the relative path to the JSON file
    relative_path = 'appcode/open-data-master/data/competitions.json'

    # Join the current working directory with the relative path
    comp_file_name = os.path.join(current_dir, relative_path)

    with open(comp_file_name) as data_file:
        data = json.load(data_file)
    df = pd.json_normalize(data, sep="_")
    de = df[["competition_name", "season_name", "competition_id", "season_id"]]
    competitions = de.to_dict(orient='records')
    return json.dumps(competitions)

# take comp id input and return info regarding it  + return all teams involved in that competition
def process_competition(comp_id, season_id):
    comp_id = int(comp_id)
    season_id = int(season_id)
    competitions = json.loads(get_competitions())
    selected_competition = None

    for competition in competitions:
        if competition['competition_id'] == comp_id and competition['season_id'] == season_id:
            selected_competition = competition
            break

    if selected_competition:
        # Get the current working directory
        current_dir = os.getcwd()
        relative_path = f"appcode/open-data-master/data/matches/{selected_competition['competition_id']}/{selected_competition['season_id']}.json"
        comp_file_name = os.path.join(current_dir, relative_path)

        with open(comp_file_name) as data_file:
            data = json.load(data_file)
            print(data)

        result = f"Competition ID: {selected_competition['competition_id']}, Competition Name: {selected_competition['competition_name']}, Competition Name: {selected_competition['season_name']}, Competition Name: {selected_competition['season_id']}"
        print(result)
    else:
        result = f"Competition not found for ID: {comp_id}"
    return result

    # # Add a list to hold the home and away team names
    #Probably needs to be separate function
    # team_names = []
    #
    # # Loop over the list of matches and extract the home and away team names
    # for match in data:
    #     home_team_name = match['home_team']['home_team_name']
    #     away_team_name = match['away_team']['away_team_name']
    #     team_names.append((home_team_name, away_team_name))
    #
    # #print(team_names)
    # return team_names

#this works when running this script from term but will break the flask app.
#process_competition(16,4)