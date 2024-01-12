# -*- coding: utf-8 -*-
""" Basic Market Class implementation """

from kernel.space.basicSpaces import Space
from sortedcontainers import SortedDict


class Market(Space):
    """ Abstract Market """
    BID_TYPE = ['O', 'D']

    def __init__(self, model, name, variables):
        """ Intialize abstract market """
        super().__init__(model, name, variables)
        self.offers = SortedDict()
        self.demmand = SortedDict()
        self.contracts = {}

    def update(self):
        """ Implemented by subclass - Testing update """
        pass
