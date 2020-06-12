#! /usr/bin/env python
from app.models import Parsing
import pytest


question = "Connais-tu l'adresse d'Openclassrooms ?"

class TestParsing:

    def setup_method(self):
        self.parsing = Parsing(question)

    def test_parsing_question(self):
        assert self.parsing.question == question

    def test_analyze_words(self):
        for word in self.parse_word:
            pass


class TestQuestion:


    def test_get_question(self, question):
        self.question = "Est-ce que tu connais l'adresse d'Openclassrooms ?"


# Récupération des données reçu via le formulaire de question


# Tester l'API Google Maps


# Création d'un mock après la récupération de la réponse de la part de l'API Google Maps


# Tests sur AJAX
