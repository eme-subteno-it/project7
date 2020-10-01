#! /usr/bin/env python
from app_py.models.Wiki import Wiki
from io                 import BytesIO
import json
import requests


class TestWiki:

    def setup_method(self):
        keyword = "Quai de la Charente"
        self.wiki = Wiki(keyword)

    def test_get_page_id(self):
        data = {
            '5653202': {
                'pageid': 3120618,
                'ns': 0,
                'title': 'Quai de la Charente',
                'index': 1,
                'extract': 'Le quai de la Charente est un quai situé le long du canal Saint-Denis, à Paris, dans le 19e arrondissement.'
            }
        }
        get_page_id = self.wiki.get_page_id(data)
        assert get_page_id == '5653202'

    def test_get_story(self, monkeypatch):
        result = {
            'extract': 'Le quai de la Charente est un quai situé le long du canal Saint-Denis, à Paris, dans le 19e arrondissement.',
            'url': 'https://fr.wikipedia.org/wiki/Quai_de_la_Charente',
        }

        def mockreturn(request):
            return BytesIO(json.dumps(result).encode())

        monkeypatch.setattr(requests, 'get', mockreturn)
        assert self.wiki.get_story() == result
