import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/seasons')
def seasons():
    now = datetime.datetime.now()
    
    current_year = now.year
    current_month = now.strftime("%B")    
    return render_template('seasons.html',year = current_year, month = current_month)

@app.route('/time')
def time():
    now = datetime.datetime.now()
    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second
    current_mic = now.microsecond

    return render_template('time.html',hour = current_hour, min = current_min,sec = current_sec, micro = current_mic)

@app.route('/day')
def day():
    now = datetime.datetime.now()
    
    return render_template('day.html',dayNum = now.day,dayW = now.weekday() )