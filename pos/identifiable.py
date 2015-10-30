__author__ = 'rhvonlehe'

"""
This module exports:

Identifiable - a base for various leaf resources that have an ID and other state variables

"""

class Identifiable:
    def __init__(self, state):
        self._state = state

    def id(self):
        return self._state['id']

