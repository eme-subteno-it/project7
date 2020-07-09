#! /usr/bin/env python
from app.models import Parsing, Map, Wiki
import pytest


class TestParsing:

    def setup_method(self):
        question = "Connais-tu l'adresse de la Tour Eiffel ?"
        self.parsing = Parsing(question)

    def test_parsing_question(self):
        self.parsing.question = " Connais-tu l'adresse d'Openclassrooms ? "
        assert self.parsing.question == " Connais-tu l'adresse d'Openclassrooms ? "


class TestMap:

    def test_get_geocode(self):
        return [{
            'formatted_address': '7 Cité Paradis, 75010 Paris, France',
            'geometry': {
                'location': {'lat': 48.8748465, 'lng': 2.3504873}
            }
        }]


class TestWiki:
    pass