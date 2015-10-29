__author__ = 'rhvonlehe'

"""
omnivore API wrapper
"""

from restnavigator import Navigator
from employee import Employee

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
        self._navigator = Navigator.hal(self._url_base, headers=self._headers)

    def _get_url(self, resource):
        return self._url_base + self.API_PATHS[resource]

    def _get_json_content(self, resource):
        req = self._get_url(resource)
        resp = requests.get(req, headers=self._headers)

        return resp.json()

    def revenue_centers(self):
        revs = self._navigator['revenue_centers']
        print revs()
        print revs['revenue_centers'][0].state

    def employees1(self):
        emps = self._navigator['employees']
        employee_list = []

        for index in range(0, emps()['count']):
            employee_state = emps['employees'][index].state
            employee_list += [Employee(employee_state)]



        print
        print emps()
        print emps['employees'][0].state
        print emps['employees'][0].state['first_name']
        print

        return employee_list


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