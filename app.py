import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, redirect, url_for
from appcode.guildinhotest import get_competitions, process_competition, get_teams

app = Flask(__name__)

# Configure logging
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
#CHANGE THIS BASED ON WHERE YOU'RE RUNNING OR COMMENT OUT TO NOT COLLECT LOGS
log_file_handler = RotatingFileHandler('/Users/sean.guillen/Documents/flasklogs/guildinho.log', maxBytes=10485760, backupCount=5)
log_file_handler.setFormatter(log_formatter)
log_file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(log_file_handler)

# Define Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/competitions')
def competitions():
    competition_data = get_competitions()
    return competition_data

# New route for processing competition form submission
@app.route('/process_competition', methods=['POST'])
def process_competition_route():
    comp_id_season_id = request.form['comp_id']
    comp_id, season_id = comp_id_season_id.split(',')

    #get competition info
    result = process_competition(comp_id, season_id)

    #get teams
    teams = get_teams(comp_id, season_id)

    return render_template('results.html', result=result, teams=teams)

# New route for displaying results
@app.route('/results')
def results():
    result = request.args.get('result', None)
    return render_template('results.html', result=result)

#route for taking the team selection
@app.route('/process_team', methods=['POST'])
def process_team_route():
    team = request.form['team_name']
    print(team)
    return render_template('results.html', team=team)

# Other Flask routes go here

if __name__ == "__main__":
    app.run(port=5003, debug=True)
