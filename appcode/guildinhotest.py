import json
import os
from pandas.io.json import json_normalize

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
    df = json_normalize(data, sep="_")
    de = df[["competition_name", "season_name", "competition_id", "season_id"]]
    competitions = de.to_dict(orient='records')
    return json.dumps(competitions)

# take comp id input and return info regarding it
def process_competition(comp_id):
    comp_id = int(comp_id)
    competitions = json.loads(get_competitions())
    selected_competition = None

    for competition in competitions:
        if competition['competition_id'] == comp_id:
            selected_competition = competition
            break

    if selected_competition:
        result = f"Competition ID: {selected_competition['competition_id']}, Competition Name: {selected_competition['competition_name']}, Competition Name: {selected_competition['season_name']}"
    else:
        result = f"Competition not found for ID: {comp_id}"

    return result
