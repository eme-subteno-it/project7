#! /usr/bin/env python
from app_py.models.Wiki import Wiki
from io                 import BytesIO
import json
import requests


class TestWiki:

    def setup_method(self):
        keyword = "Cité Paradis"
        self.wiki = Wiki(keyword)

    def test_get_page_id(self):
        data = {
            '5653202': {
                'pageid': 5653202,
                'ns': 0,
                'title': 'Cité Paradis',
                'index': 1,
                'extract': 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.'
            }
        }
        get_page_id = self.wiki.get_page_id(data)
        assert get_page_id == '5653202'
    
    def test_get_story(self, monkeypatch):
        result =  {
            'extract': 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.',
            'url': 'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis',
        }

        def mockreturn(request):
            return BytesIO(json.dumps(result).encode())
        
        monkeypatch.setattr(requests, 'get', mockreturn)
        assert self.wiki.get_story() == result
