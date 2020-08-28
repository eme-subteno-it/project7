#! /usr/bin/env python

""" All routes usefull for the application """

from flask import Flask, render_template, request, json
from app_py.models.ParsingBot import ParsingBot
from app_py.models.Map import Map
from app_py.models.Wiki import Wiki

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    """ The main page """
    return render_template('index.html')


@app.route('/get_response/', methods=['POST'])
def get_response():
    """ Get the user's question, parsing the question and return the data's google maps api. """
    response = request.get_data(cache=False, as_text=True)
    error = {
        'error': 'Il faut taper sur les touches de ton clavier \
            si tu recherches un endroit à visiter.'
    }

    if response:
        question = ParsingBot(response)
        values = question.parsing_question()

        mapping = Map(values)
        result = mapping.get_geocode()

        return json.dumps(result)

    return json.dumps(error)


@app.route('/get_story/', methods=['POST'])
def get_story():
    """ Call the class Wiki for get the data's api. """
    response = request.get_data(cache=False, as_text=True)

    wiki = Wiki(response)
    story = wiki.get_story()

    return json.dumps(story)
