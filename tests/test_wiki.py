#! /usr/bin/env python
from app_py.models.Wiki import Wiki
from io                 import BytesIO
import json
import urllib.request


class TestWiki:

    def setup_method(self):
        keyword = "Cité Paradis"
        self.wiki = Wiki(keyword)

    def test_get_page_id(self):
        pass
    
    def test_get_story(self, monkeypatch):
        result =  {
            'extract': 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n\n',
            'url': 'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis',
        }

        def mockreturn(request):
            return BytesIO(json.dumps(result).encode())
        
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert self.wiki.get_story() == result
