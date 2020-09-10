#! /usr/bin/env python
from app_py.models.Map import Map
from io         import BytesIO
import json
import urllib.request


class TestMap:

    def test_get_geocode(self, monkeypatch):
        location = "openclassrooms"
        the_map = Map(location)

        result = [{
            'address_components': 'Quai de la Charente',
            'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
            'geometry': {
                'lat': 48.8975156,
                'lng': 2.3833993
            }
        }]

        def mockreturn(request):
            return BytesIO(json.dumps(result).encode())
        
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        if result:
            address = result[0]
            assert the_map.get_geocode() == address
        else:
            assert the_map.get_geocode() is False
