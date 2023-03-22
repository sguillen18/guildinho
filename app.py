from flask import Flask, render_template, request, redirect, url_for
from appcode.guildinhotest import get_competitions, process_competition

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/competitions')
def competitions():
    competition_data = get_competitions()
    return(competition_data)

# New route for processing competition form submission
@app.route('/process_competition', methods=['POST'])
def process_competition_route():
    comp_id = request.form['comp_id']
    result = process_competition(comp_id)
    return redirect(url_for('results', result=result))

# New route for displaying results
@app.route('/results')
def results():
    result = request.args.get('result', None)
    return render_template('results.html', result=result)

# Other Flask routes go here

if __name__ == "__main__":
    app.run(port=5003)