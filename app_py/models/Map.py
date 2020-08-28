#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The model's module contains all classes usefull for the application
"""
import os
import googlemaps


if os.environ.get('API_KEY_GOOGLE') is None:
    from config import API_KEY_GOOGLE
    api_key_google = API_KEY_GOOGLE
else:
    api_key_google = os.environ['API_KEY_GOOGLE']


# pylint: disable=invalid-name, too-few-public-methods
class Map:
    """
        This class the coordinate receipt by the user.
        She use the GoogleMap API.
        :param arg1: The location name receipt by the user
    """

    def __init__(self, location):
        self.location = location

    def get_geocode(self):
        """
            This method connects to the GoogleMaps API using an API key
            and uses its geocode method to retrieve and return the coordinates
            of the location chosen by the user.
        """
        gmaps = googlemaps.Client(api_key_google)
        geocode_result = gmaps.geocode(self.location)
        address = {}

        if geocode_result:
            address['address_components'] = geocode_result[0]['address_components'][1]['long_name']
            address['formatted_address'] = geocode_result[0]['formatted_address']
            address['geometry'] = geocode_result[0]['geometry']['location']

            return address

        return False
