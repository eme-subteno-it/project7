#! /usr/bin/env python
import googlemaps
import requests
from config import API_KEY_GOOGLE


class Map:


    def __init__(self, location):
        self.location = location

    def get_geocode(self):
        gmaps = googlemaps.Client(API_KEY_GOOGLE)
        geocode_result = gmaps.geocode(self.location)
        address = {}

        if geocode_result:
            address['address_components'] = geocode_result[0]['address_components'][1]['long_name']
            address['formatted_address'] = geocode_result[0]['formatted_address']
            address['geometry'] = geocode_result[0]['geometry']['location']

            return address
        else:
            return False
