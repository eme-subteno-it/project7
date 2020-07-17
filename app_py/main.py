#! /usr/bin/env python
from flask import Flask, render_template, url_for, request, json
from app_py.models.Parsing import Parsing
from app_py.models.Map import Map
from app_py.models.Wiki import Wiki

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/get_response/', methods=['POST'])
def get_response():
    response = request.get_data(cache=False, as_text=True)

    question = Parsing(response)
    values = question.parsing_question()

    mapping = Map(values)
    result = mapping.get_geocode()

    return json.dumps(result)
