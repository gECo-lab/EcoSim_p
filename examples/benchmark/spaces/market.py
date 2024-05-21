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


        self.market_not_empty = True

        while self.has_demand:
            self.a_demand = self.get_demand()
            self.have_unmet_demand = True
            self.total_contracted_value = 0.0

            while self.have_unmet_demand:
                if self.has_offers():
                    self.an_offer = self.get_offer_at_random()
                    self.an_offer.c_owner = self.a_demand.c_owner
                    self.contracts[self.an_offer.c_producter] = self.an_offer
                    self.total_contracted_value += self.an_offer.c_price
                    if self.total_contracted_value >= self.an_offer.c_price:
                        self.have_unmet_demand = False
                else:
                    
                    self.release_offers()
                    self.offers.clear()
                
            self.release_demand()
            self.clear_demand()
                    


# continua daqui
                        self.an_offer.owner_of_g = self.demmand_owner
                        self.contracted_offers[self.an_offer.producer_of_g] = self.an_offer
                        self.total_contracted_value += self.an_offer.value_of_g
                        if self.total_contracted_value >= self.an_offer.value_of_g:
                            self.demmand_not_satisfied = False
                    else:
                        self.demmand_not_satisfied = False
                        self.release_demmand()
                        self.demmand.clear()

                self.notify_match(self.a_demmand, self.contracted_offers)
                self.register_contract(self.a_demmand, self.contracted_offers)
            else:
                self.bids_not_matched = False
                self.release_offers()
                self.offers.clear()

       
            


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
    


    def get_demand(self):
         """ Implements the maching in market """
         if(self.market_type == "random"):
             self.random_matching()
         elif(self.market_type == "hop"):
             self.hop_matching()
         elif(self.market_type == "lop"):
             self.lop_matching()
         elif(self.market_type == "bhop"):
             self.bhop_matching()
         elif(self.market_type == "blop"):
             self.blop_matching()
         else:
             # Add error treatment here
             raise ValueError("Invalid market matching type")

    def random_matching(self):
         """ Randomly pop a demand from the demand dictionary and return it """
                
         owner = next(iter(self.demand.keys()))
         demand = self.demand.pop(owner)
         return demand

    def hop_matching(self):
        pass

    def lop_matching(self):
        pass

    def bhop_matching(self):
        pass

    def blop_matching(self):
        pass

    def has_offers(self):
        """ A market answers if is has offers (True or False) """
        if self.offers.__len__() > 0:
            return True
        else:
            return False

    def has_demand(self):
        """ A market answers if is has demand (True or False) """
        if self.demand.__len__() > 0:
            return True
        else:
            return False

    def no_of_offers(self):
        """ A market answers the number of offers it has """
        return self.offers.__len__()

        
    def get_offer_at_random(self):
        """ Randomly pop an offer from the offers dictionary and return it """
        owner = next(iter(self.offers.keys()))
        offer = self.offers.pop(owner)
        return offer
    
    def release_demand(self):
        pass

    def clear_demand(self):
        pass

    def notify_match(self, a_demmand, contracted_offers):
        """ Notify the agents that their bids where matched """
        self.contractor = a_demmand.owner_of_g
        self.contractor.get_contracted_offers(contracted_offers)
        for offer in contracted_offers.values():
            offer.producer_of_g.got_contract()

    def register_contract(self, a_demmand, contracted_offers):
        """ The matched bids become contracts """
        self.contractor = a_demmand.owner_of_g
        self.contracts[self.contractor] = contracted_offers
        self.contractor.get_contracted_offers(contracted_offers)

