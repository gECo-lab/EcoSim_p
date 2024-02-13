# -*- coding: utf-8 -*-
""" Basic Market Class implementation 

This module implements the generic macthing process 
in an economic market.

Example:


Todo: 
"""

from kernel.space.basicSpaces import Space

class Market(Space):
    """ Abstract Market """
    def __init__(self, model, name, variables):
        """ Intialize abstract market """
        super().__init__(model, name, variables)
        self.offers = {}
        self.demand = {}
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

    def set_demand(self, an_owner, a_good):
        "Set the demand for a good"
        self.demand[an_owner] = a_good

    def set_offer(self, an_owner, a_good):
        "Set the offer for a good"
        self.offers[an_owner] = a_good

