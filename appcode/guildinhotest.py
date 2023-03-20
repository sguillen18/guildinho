import json
import os
from pandas.io.json import json_normalize


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