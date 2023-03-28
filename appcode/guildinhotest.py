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

        result = f"Competition ID: {selected_competition['competition_id']}, Competition Name: {selected_competition['competition_name']}, Competition Name: {selected_competition['season_name']}, Competition Name: {selected_competition['season_id']}"
    else:
        result = f"Competition not found for ID: {comp_id}"
    return result

def get_teams(comp_id, season_id):
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

    # Add a set to hold the unique team names
    unique_team_names = set()

    # Loop over the list of matches and extract the home and away team names
    for match in data:
         home_team_name = match['home_team']['home_team_name']
         away_team_name = match['away_team']['away_team_name']
         unique_team_names.add(home_team_name)
         unique_team_names.add(away_team_name)

    # Convert set to list for returning
    team_names = list(unique_team_names)
    return team_names
