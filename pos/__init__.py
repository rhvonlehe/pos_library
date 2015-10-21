__author__ = 'rhvonlehe'

"""
omnivore API wrapper
"""

import requests


#
#class Config:
#   """A class containing the configuration of the omnivore site"""
#


class Pos:

    # TODO: possibly move some of this to Config class
    #
    _version = '0.1'
    _location_base = 'https://api.omnivore.io/' + _version + '/locations/'

    API_PATHS = {'employees': 'employees',
                 'revenue_centers': 'revenue_centers',
                 'tables': 'tables',
                 'order_types': 'order_types',
                 'tickets': 'tickets'}

    def __init__(self, api_key, location):
        self._api_key = api_key
        self._location = self._location_base + location + '/'
        self._headers={'Api-Key': self._api_key}

    def _get_uri(self, resource):
        return self._location + self.API_PATHS[resource]


    def employees(self):
        req = self._get_uri('employees')
        print req
        r = requests.get(req, headers=self._headers)
        #        print r.json()

        return r.text