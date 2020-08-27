#! /usr/bin/env python
from flask import Flask, render_template, url_for, request, json
from app_py.models.ParsingBot import ParsingBot
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
    error = {'error': 'Il faut taper sur les touches de ton clavier si tu recherches un endroit à visiter.'}
    print(response)

    if response:
        question = ParsingBot(response)
        values = question.parsing_question()

        mapping = Map(values)
        result = mapping.get_geocode()

        return json.dumps(result)
    else:
        return json.dumps(error)

@app.route('/get_story/', methods=['POST'])
def get_story():
    response = request.get_data(cache=False, as_text=True)

    wiki = Wiki(response)
    story = wiki.get_story()

    return json.dumps(story)
