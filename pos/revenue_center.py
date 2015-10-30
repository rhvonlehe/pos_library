__author__ = 'rhvonlehe'

"""
This module exports:

RevenueCenter - a class that models a revenue_center in the POS system

"""

from identifiable import Identifiable

class RevenueCenter(Identifiable):

    def default(self):
        return self._state['default']

    def name(self):
        return self._state['name']

