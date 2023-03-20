from flask import Flask, render_template
from appcode.guildinhotest import get_competitions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/competitions')
def competitions():
    competition_data = get_competitions()
    return(competition_data)

# Other Flask routes go here

if __name__ == "__main__":
    app.run(port=5003)