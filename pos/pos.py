__author__ = 'rhvonlehe'

"""
This module exports:

Pos - a class representing a point of sale system whose data has been synced and is available
      via the omnivore HTTP API.

"""

import requests
import employee

class Pos:
    _location_base = 'https://api.omnivore.io/0.1/locations/'
    def __init__(self, api_key, location):
        self._api_key = api_key
        self._location = self._location_base + location + '/'
        self._headers={'Api-Key': self._api_key}

    def employees(self):
        req = self._location + 'employees'
        r = requests.get(req, headers=self._headers)
        #        print r.json()

        return
