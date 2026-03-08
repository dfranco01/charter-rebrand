from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/services-1')
def services():
    return "service"