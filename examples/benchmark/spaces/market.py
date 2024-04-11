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
        """
        Set the demand for a good.

        Parameters:
        - an_owner: The owner of the demand.
        - a_good: The good for which the demand is being set.
        """
        self.demand[an_owner] = a_good

    def set_offer(self, an_owner, a_good):
        """
        Set the offer for a good.

        Parameters:
        - an_owner (str): The owner of the offer.
        - a_good (str): The good being offered.

        Returns:
        None
        """
        self.offers[an_owner] = a_good

