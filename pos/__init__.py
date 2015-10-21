__author__ = 'rhvonlehe'

"""
omnivore API wrapper
"""

import requests

__version__ = '0.1'
__location_base__ = 'https://api.omnivore.io/' + __version__ + '/locations/'


class Config:
    """A class containing the configuration of the omnivore site"""

    API_PATHS = {'employees': 'employees',
                 'revenue_centers': 'revenue_centers',
                 'tables': 'tables',
                 'order_types': 'order_types',
                 'tickets': 'tickets'}



class Pos:
    def __init__(self, api_key, location):
        self._api_key = api_key
        self._location = __location_base__ + location + '/'
        self._headers={'Api-Key': self._api_key}

    def employees(self):
        req = self._location + Config.API_PATHS['employees']
        print req
        r = requests.get(req, headers=self._headers)
        #        print r.json()

        return r.text