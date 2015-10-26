__author__ = 'rhvonlehe'

"""
omnivore API wrapper
"""

#from restnavigator import Navigator

import requests # TODO - remove
#import json # TODO - remove


# TODO - remove
#
#class Config:
#   """A class containing the configuration of the omnivore site"""
#


class Pos:

    # TODO: possibly move some of this to separate Config class
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
        self._url_base = self._location_base + location + '/'
        self._headers={'Api-Key': self._api_key}

    def _get_url(self, resource):
        return self._url_base + self.API_PATHS[resource]

    def _get_json_content(self, resource):
        req = self._get_url(resource)
        resp = requests.get(req, headers=self._headers)

        return resp.json()

    def employees(self):
        # req = self._get_url('employees')
        # resp = requests.get(req, headers=self._headers)
        #
        # resp = resp.json()

        resp = self._get_json_content('employees')

        print resp
        # embedded = json['_embedded']
        # print embedded
        #print embedded['employees']
        # for emp in embedded['_employees']:
        #     print emp


        # print json['count']
        # print json['_links']
        # print json['_embedded']

        return #r.text