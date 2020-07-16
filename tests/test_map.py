#! /usr/bin/env python
from app_py.models.Map import Map
from io         import BytesIO
import json
import urllib.request


class TestMap:

    def setup_method(self):
        location = "openclassrooms"
        self.map = Map(location)

    def test_get_geocode(self, monkeypatch):
        result = [{
            'address_components': 'Cité Paradis',
            'formatted_address': '7 Cité Paradis, 75010 Paris, France',
            'geometry': {
                'lat': 48.8748465,
                'lng': 2.3504873
            }
        }]

        def mockreturn(request):
            return BytesIO(json.dumps(result).encode())
        
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        if result:
            address = result[0]
            assert self.map.get_geocode() == address
        else:
            assert self.map.get_geocode() == False
