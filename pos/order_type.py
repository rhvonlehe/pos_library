__author__ = 'rhvonlehe'

"""
This module exports:

OrderType - a class that models an order type in the POS system

"""

from identifiable import Identifiable

class OrderType(Identifiable):

    def available(self):
        return self._state['available']

    def name(self):
        return self._state['name']
