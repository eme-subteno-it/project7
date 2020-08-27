#! /usr/bin/env python
from app_py.models.ParsingBot import ParsingBot
from io import BytesIO


class TestParsing:

    def setup_method(self):
        question = " Connais-tu l'adresse d'Openclassrooms ? "
        self.parsing = ParsingBot(question)

    def test_set_question(self):
        assert self.parsing.question == " Connais-tu l'adresse d'Openclassrooms ? "

    def test_parsing_question(self):
        parsing_question = self.parsing.parsing_question()
        assert parsing_question == 'openclassrooms'
