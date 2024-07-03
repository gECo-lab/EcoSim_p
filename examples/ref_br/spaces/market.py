# -*- coding: utf-8 -*-
""" Basic Market Class implementation """

from space.basicSpaces import Space
from sortedcontainers import SortedDict


class Market(Space):
    """ Abstract Market """
    BID_TYPE = ['O', 'D']

    def __init__(self, model, name, actions_set_file, action_class, variables):
        """ Intialize abstract market """
        super().__init__(model, name, actions_set_file, action_class, variables)
        self.offers = SortedDict()
        self.demand = SortedDict()
        self.contracts = {}
        self.excess_demand = 0

    def update(self):
        """ Implemented by subclass - Testing update """
        self.match_bids()

    def match_bids(self):
        """
        Market matching of offer and demand
        This method can be specialized depending on  market
        Is prepared to be an assincronous method
        """
        self.bids_not_matched = True
        self.contracted_offers = {}
        self.total_contracted_value = 0.0

        while self.bids_not_matched:
            if self.has_demand():
                self.a_demand = self.get_highest_demand()
                self.demand_not_satisfied = True
                self.demand_owner = self.a_demand.owner_of_g
                self.total_contracted_value = 0.0

                while self.demand_not_satisfied:
                    if self.has_offers():
                        self.an_offer = self.get_lowest_offer()
                        self.an_offer.owner_of_g = self.demand_owner
                        self.contracted_offers[self.an_offer.producer_of_g] = self.an_offer
                        self.total_contracted_value += self.an_offer.value_of_g
                        if self.total_contracted_value >= self.an_offer.value_of_g:
                            self.demand_not_satisfied = False
                    else:
                        self.demand_not_satisfied = False
                        self.release_demand()
                        self.demand.clear()

                self.notify_match(self.a_demand, self.contracted_offers)
                self.register_contract(self.a_demand, self.contracted_offers)
            else:
                self.bids_not_matched = False
                self.release_offers()
                self.offers.clear()

    def bid_market(self, bid_type, a_good):
        """ include an  offer in the market """
        if bid_type in self.BID_TYPE:
            if bid_type == 'O':
                self.offers[a_good.value_of_g] = a_good
            else:
                if bid_type == 'D':
                    self.demand[a_good.value_of_g] = a_good
                else:
                    raise Exception("Type of bid not valid - type: ", bid_type)

    def notify_match(self, a_demand, contracted_offers):
        """ Notify the agents that their bids where matched """
        self.contractor = a_demand.owner_of_g
        self.contractor.get_contracted_offers(contracted_offers)
        for offer in contracted_offers.values():
            offer.producer_of_g.got_contract()

    def register_contract(self, a_demand, contracted_offers):
        """ The matched bids become contracts """
        self.contractor = a_demand.owner_of_g
        self.contracts[self.contractor] = contracted_offers
        self.contractor.get_contracted_offers(contracted_offers)

    def release_offers(self):
        """ When some bid passed the timeout of the system, the market release the bid """
        for bid, an_offer in self.offers.items():
            an_offer.producer_of_g.release_offer()

    def release_demand(self):
        """ When some bid passed the timeout of the system, the market release the bid """
        self.excess_demand = self.total_demands()
        for bid, a_demand in self.demand.items():
            a_demand.producer_of_g.release_demand()

    def init_offers(self, new_offers):
        """ Get new offers dict and check if is a sorted dict - if yes, set it """
        if isinstance(new_offers, SortedDict):
            self.offers = new_offers
        else:
            print('The input is not a sorted dictionary')

    def offer_gs(self, offered_good):
        """ include an  offer in the market """
        self.offers[offered_good.value_of_g] = offered_good

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

    def total_demands(self):
        """ A market answers the number of offers it has """
        return self.demand.__len__()


    def get_lowest_offer(self):
        """ A market answers the offer with the lowest value (in the self.offers ordered dict) """
        self.key, self.value = self.offers.popitem(0)
        return self.value

    def get_highest_offer(self):
        """ A market answers the offer with the highest value (in the self.offers ordered dict) """
        self.key, self.value = self.offers.popitem(-1)
        return self.value

    def get_lowest_demand(self):
        """ A market answers the demand with the lowest value (in the self.demand ordered dict) """
        self.key, self.value = self.demand.popitem(0)
        return self.value

    def get_highest_demand(self):
        """ A market answers the demand with the highest value (in the self.demand ordered dict) """
        self.key, self.value = self.demand.popitem(-1)
        return self.value

    def return_offer(self, gs):
        """ A market receives an offer of a good or service """
        self.offer_gs(gs)

    def show_offer(self, an_agent):
        """ Show offer """
        an_agent.show_offer()
        print("")
        print("Model: ", an_agent.model.name)
        print("------------")

    def compute_production_price(self):
        """ Agent compute production price """
        pass

    def pay_taxes(self, an_agent):
        """ An agent pay taxes """
        pass
