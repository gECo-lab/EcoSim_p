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
        self.demmand = SortedDict()
        self.contracts = {}

    def update(self):
        """ Implemented by subclass - Testing update """
        self.match_bids()

    def match_bids(self):
        """
        Market matching of offer and demmand
        This method can be specialized depending on  market
        Is prepared to be an assincronous method
        """
        self.bids_not_matched = True
        self.contracted_offers = {}
        self.total_contracted_value = 0.0

        while self.bids_not_matched:
            if self.has_demmand():
                self.a_demmand = self.get_highest_demmand()
                self.demmand_not_satisfied = True
                self.demmand_owner = self.a_demmand.owner_of_g
                self.total_contracted_value = 0.0

                while self.demmand_not_satisfied:
                    if self.has_offers():
                        self.an_offer = self.get_lowest_offer()
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

    def bid_market(self, bid_type, a_good):
        """ include an  offer in the market """
        if bid_type in self.BID_TYPE:
            if bid_type == 'O':
                self.offers[a_good.value_of_g] = a_good
            else:
                if bid_type == 'D':
                    self.demmand[a_good.value_of_g] = a_good
                else:
                    raise Exception("Type of bid not valid - type: ", bid_type)

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

    def release_offers(self):
        """ When some bid passed the timeout of the system, the market release the bid """
        for bid, an_offer in self.offers.items():
            an_offer.producer_of_g.release_offer()

    def release_demmand(self):
        """ When some bid passed the timeout of the system, the market release the bid """
        for bid, a_demmand in self.demmand.items():
            a_demmand.producer_of_g.release_demmand()

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

    def has_demmand(self):
        """ A market answers if is has demmand (True or False) """
        if self.demmand.__len__() > 0:
            return True
        else:
            return False

    def no_of_offers(self):
        """ A market answers the number of offers it has """
        return self.offers.__len__()

    def get_lowest_offer(self):
        """ A market answers the offer with the lowest value (in the self.offers ordered dict) """
        self.key, self.value = self.offers.popitem(0)
        return self.value

    def get_highest_offer(self):
        """ A market answers the offer with the highest value (in the self.offers ordered dict) """
        self.key, self.value = self.offers.popitem(-1)
        return self.value

    def get_lowest_demmand(self):
        """ A market answers the demmand with the lowest value (in the self.demmand ordered dict) """
        self.key, self.value = self.demmand.popitem(0)
        return self.value

    def get_highest_demmand(self):
        """ A market answers the demmand with the highest value (in the self.demmand ordered dict) """
        self.key, self.value = self.demmand.popitem(-1)
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
