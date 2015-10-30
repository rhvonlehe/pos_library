__author__ = 'rhvonlehe'

"""
This module exports:

Table - a class that models a table in the POS system

"""

from identifiable import Identifiable

class Table(Identifiable):

    def available(self):
        return self._state['available']

    def name(self):
        return self._state['name']

    def number(self):
        return self._state['number']

    def seats(self):
        return self._state['seats']