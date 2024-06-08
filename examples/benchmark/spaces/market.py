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
        self.macthed_offers = []

    def update(self):
        """ """
        self.matching()


    def matching(self):


        self.market_not_empty = True

        while self.has_demand():
            self.a_demand = self.get_demand()
            self.this_remaining_demand = self.a_demand.c_quantity
            self.buyer = self.a_demand.c_owner
            self.have_unmet_demand = True
            self.total_contracted_value = 0.0

            while self.have_unmet_demand:
                if self.has_offers():
                    self.an_offer = self.get_offer()
                    self.seller = self.an_offer.c_owner
                    if self.an_offer.c_quantity <= self.this_remaining_demand:
                        self.this_remaining_demand -= self.an_offer.c_quantity
                        # transfer ownership
                        self.an_offer.c_owner = self.a_demand.c_owner
                        self.total_contracted_value += self.an_offer.ammount()
                        self.macthed_offers.append(self.an_offer)
                        # include contract
                        # include payment
                        self.buyer.pay(self.seller, self.an_offer.ammount())
                        # transfer goods_services
                        # notify macht
                    else:
                        self.partial_offer = self.set_partial_offer(self.an_offer)
                        self.partial_offer.c_quantity = self.this_remaining_demand
                        # transfer ownership
                        self.partial_offer.c_owner = self.a_demand.c_owner
                        self.an_offer.c_quantity -= self.this_remaining_demand
                        self.macthed_offers.append(self.partial_offer)
                        self.this_remaining_demand = 0.0
                        self.have_unmet_demand = False
                        # include contract
                        # include payment
                        self.buyer.pay(self.seller, self.an_offer.ammount())
                        # notify macth                
                if self.this_remaining_demand == 0:
                    self.have_unmet_demand = False
                    self.release_offers()
                else:
                    self.market_has_no_offers()
                    self.have_unmet_demand = False


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
             a_demand = self.random_demand_matching()
         elif(self.market_type == "hop"):
             a_demand = self.hop_demand_matching()
         elif(self.market_type == "lop"):
             a_demand = self.lop_demand_matching()
         elif(self.market_type == "bhop"):
             a_demand = self.bhop_demand_matching()
         elif(self.market_type == "blop"):
             a_demand = self.blop_demand_matching()
         else:
             # Add error treatment here
             raise ValueError("Invalid market matching type")
         return a_demand
    
    def get_offer(self):
         """ Implements the maching in market """
         if(self.market_type == "random"):
             an_offer = self.random_offer_macthing()
         elif(self.market_type == "hop"):
             an_offer = self.hop_offer_matching()
         elif(self.market_type == "lop"):
             an_offer = self.lop_offer_matching()
         elif(self.market_type == "bhop"):
             an_offer = self.bhop_offer_matching()
         elif(self.market_type == "blop"):
             an_offer = self.blop__offer_matching()
         else:
             # Add error treatment here
             raise ValueError("Invalid market matching type")
         return an_offer

    def random_demand_matching(self):
        """ Randomly pop a demand from the demand dictionary and return it """
        if not self.demand:
            raise ValueError("No demand available in market ", self.name)
        else:
            a_demand = self.demand.popitem()[1]
            return a_demand

    def hop_demand_matching(self):
        pass

    def lop_demand_matching(self):
        pass

    def bhop_demand_matching(self):
        pass

    def blop_demand_matching(self):
        pass

    def has_offers(self):
        """ A market answers if is has offers (True or False) """
        if not self.offers:
            return False
        else:
            return True

    def has_demand(self):
        """ A market answers if is has demand (True or False) """
        if not self.demand:
            return False
        else:
            return True

    def no_of_offers(self):
        """ A market answers the number of offers it has """
        return self.offers.__len__()
        
    def random_offer_macthing(self):
        """ Randomly pop an offer from the offers dictionary and return it """
        offer = self.offers.popitem()[1]
        return offer

    def hop_offer_matching(self):
        pass

    def lop_offer_matching(self):
        pass

    def bhop_offer_matching(self):
        pass

    def blop_offer_matching(self):
        pass

    def market_has_no_offers(self):
        pass

    def release_demand(self):
        """Inform the bider that their demand was not satisfied
        """
        for demand in self.demand.values():
            demand.c_owner.release_demand()
            self.demand = {}

    def release_offers(self):
        """Inform the producers/household that their offer was not bought
        """
        for offer in self.offers.values():
            offer.c_producer.release_offer()
            self.offers = {}

    def set_partial_offer(self, an_offer):
        partial_offer = type(an_offer)()
        partial_offer = an_offer.copy_attributes(partial_offer)
        return partial_offer
        

    def notify_match(self, a_demmand, contracted_offers):
        """ Notify the agents that their bids where matched """
        self.contractor = a_demmand.c_owner
        self.contractor.get_contracted_offers(contracted_offers)
        for offer in contracted_offers.values():
            offer.producer_of_g.got_contract()

    def register_contract(self, a_demmand, contracted_offers):
        """ The matched bids become contracts """
        self.contractor = a_demmand.c_owner
        self.contracts[self.contractor] = contracted_offers
        self.contractor.get_contracted_offers(contracted_offers)




class CGMarket(Market):
    """Consumers Goods Market

    Args:
        Market (_type_): _description_
    """
    def __init__(self, model, name, variables):
        super().__init__(model, name, variables)


class LaborMarket(Market):
    """Labor Market

    Args:
        Market (_type_): _description_
    """

    def __init__(self, model, name, variables):
        super().__init__(model, name, variables)

        