# this file handels the home page
from flask import render_template
from app import app

@app.route('/')
def home ():
    return render_template('index.html')
