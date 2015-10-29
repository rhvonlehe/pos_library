__author__ = 'rhvonlehe'

"""
This module exports:

Employee - a class that models an employee in the POS system

"""

#from hal_resource import HalResource ## TODO remove

class Employee:
    def __init__(self, state):
        self._state = state

    def first_name(self):
        return self._state['first_name']

    def last_name(self):
        return self._state['last_name']


