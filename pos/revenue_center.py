__author__ = 'rhvonlehe'

"""
This module exports:

RevenueCenter - a class that models a revenue_center in the POS system

"""

class RevenueCenter():
    def __init__(self, state):
        self._state = state

    def name(self):
        return self._state['name']

