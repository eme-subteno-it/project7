#! /usr/bin/env python
# -*- coding: utf-8 -*-

import googlemaps
from config import API_KEY_GOOGLE


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
            This method connects to the GoogleMap API using an API key
            and uses its geocode method to retrieve and return the coordinates
            of the location chosen by the user.
        """
        gmaps = googlemaps.Client(API_KEY_GOOGLE)
        geocode_result = gmaps.geocode(self.location)
        address = {}

        if geocode_result:
            address['address_components'] = geocode_result[0]['address_components'][1]['long_name']
            address['formatted_address'] = geocode_result[0]['formatted_address']
            address['geometry'] = geocode_result[0]['geometry']['location']

            return address

        return False
