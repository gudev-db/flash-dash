from application import app
from flask import render_template


@app.route('/')
def index():
  return render_template('index.html', title='index')


@app.route('/layout')
def index2():
  return render_template('layout.html', title='layout')
