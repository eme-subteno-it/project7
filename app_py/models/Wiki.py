#! /usr/bin/env python
import requests


class Wiki:


    def __init__(self, keyword):
        self.keyword = keyword
        self.session = requests.Session()
        self.url = 'https://fr.wikipedia.org/w/api.php'

    def get_page_id(self, data):
        keys = data.keys()
        list_keys = list(keys)
        page_id = list_keys[0]

        return page_id

    def get_story(self):
        
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

        page_id = self.get_page_id(data['query']['pages'])

        result['extract'] = data['query']['pages'][str(page_id)]['extract']
        result['url'] = url['query']['pages'][str(page_id)]['fullurl']

        return result
