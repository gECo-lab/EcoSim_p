# -*- coding: utf-8 -*-
""" Basic Market Class implementation 

This module implements the generic macthing process 
in an economic market.

Example:


Todo: 
"""

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
        """ """
        self.matching()
        self.contract()
        self.release_bids()


    def matching(self):
        """ Implements the maching in market """
        pass


    def contract(self):
        """ Register the contracts """
        pass

    def release_bids(self):
        """ Releases bids not matched """
        pass