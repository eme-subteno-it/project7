#! /usr/bin/env python
from flask import Flask, render_template, escape, url_for, request

app = Flask(__name__)
# app.config.from_object('../config')


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')