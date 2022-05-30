from app import app
from flask import render_template 


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/fortress')
def fort():
    return render_template('fortress.html')
