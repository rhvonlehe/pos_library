__author__ = 'rhvonlehe'

"""
This module exports:

Employee - a class that models an employee in the POS system

"""

from identifiable import Identifiable

class Employee(Identifiable):

    def check_name(self):
        return self._state['check_name']

    def first_name(self):
        return self._state['first_name']

    def last_name(self):
        return self._state['last_name']

    def login(self):
        return self._state['login']

