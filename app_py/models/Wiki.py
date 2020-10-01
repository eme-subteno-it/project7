#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" The model's module contains all classes usefull for the application """

import requests


# pylint: disable=invalid-name, too-few-public-methods
class Wiki:
    """
        This class get the searched address and retrieves the wikipedia related to it.
        :param arg1: It's the searched address.
        :param arg2: The wiki api's session for get the datas.
        :param arg3: The api's url to get the datas.
    """

    def __init__(self, keyword):
        self.keyword = keyword
        self.session = requests.Session()
        self.url = 'https://fr.wikipedia.org/w/api.php'

    @staticmethod
    def get_page_id(data):
        """
            Method to get the page id to target the datas.
        """
        keys = data.keys()
        list_keys = list(keys)
        page_id = list_keys[0]

        return page_id

    def get_story(self):
        """
            Method to get the api's datas and returns to json format.
        """
        params = {
            'action': 'query',
            'generator': 'prefixsearch',
            'gpssearch': self.keyword,
            'prop': 'extracts',
            'exintro': '1',
            'explaintext': '1',
            'redirects': '1',
            'inprop': 'url|talkid',
            'format': 'json',
        }

        get_url = {
            'action': 'query',
            'titles': self.keyword,
            'prop': 'info',
            'inprop': 'url|talkid',
            'format': 'json',
        }

        result = {}
        request = self.session.get(url=self.url, params=params)
        data = request.json()

        get_url_page = self.session.get(url=self.url, params=get_url)
        url = get_url_page.json()

        page_id = Wiki.get_page_id(data['query']['pages'])
        page_id_url = Wiki.get_page_id(url['query']['pages'])

        result['extract'] = data['query']['pages'][str(page_id)]['extract']
        result['url'] = url['query']['pages'][str(page_id_url)]['fullurl']

        return result
