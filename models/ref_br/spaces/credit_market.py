# Space Class  Implementation

from .market import Market


class CreditMarket(Market):
    """ The Credit Market """

    def match_bids(self):
        """
        Market matching of offer and demand
        This method can be specialized depending on  market
        Is prepared to be an assincronous method
        This method here is specialized to the RE market
        """
        self.bids_not_matched = True
        self.contracted_offer = None
        self.total_contracted_value = 0.0
        self.excess_demand = self.total_demands()

        while self.bids_not_matched:
            if self.has_demand():
                self.a_demand = self.get_highest_demand()
                self.demand_not_satisfied = True
                self.demand_owner = self.a_demand.owner_of_g
                self.total_contracted_value = 0.0

                while self.demand_not_satisfied:
                    if self.has_offers():
                        self.an_offer = self.get_highest_offer()
                        if self.a_demand.value_of_g >= self.an_offer.value_of_g:
                            self.an_offer.owner_of_g = self.demand_owner
                            self.contracted_offer = self.an_offer
                            self.total_contracted_value += self.an_offer.value_of_g
                            self.demand_not_satisfied = False
                            self.notify_match(self.a_demand, self.contracted_offer)
                            self.register_contract(self.a_demand, self.contracted_offer)
                    else:
                        self.demand_not_satisfied = False
                        self.release_demand()
                        self.demand.clear()
            else:
                self.bids_not_matched = False
                self.release_offers()
                self.offers.clear()

    def notify_match(self, a_demand, contracted_offer):
        """ Notify the agents that their bids where matched """
        self.contractor = a_demand.owner_of_g
        self.contractor.get_contracted_offers(contracted_offer)
        contracted_offer.producer_of_g.got_contract(contracted_offer)

    def decide_cr_target(self, a_bank):
        """ A bank agent decides capital ratio target """
        pass

    def decide_interest_rate_strategy(self, a_bank):
        """A bank decides the strategy for interest rate determination """
        pass

    def offer_credit(self, a_bank):
        """ A bank offer credit on the credit market """
        pass

    def contract_credit(self, an_agent, a_bank):
        """ An agent contracts credit from a Bank """
        pass

    def calculate_exposure(self, a_bank):
        """ A bank calculates its exposure """
        pass

    def contract_cash_advances(self):
        """ Central Bank Contract Cash Advances on the Credit Market """
        pass

    def receive_advances_CB(self, a_bank, central_bank, ammount):
        """ A bank receive some ammount of money  from the central bank at some interest rate """
        pass

    def buy_gov_bonds(self, a_bank, gov, ammount):
        """ A bank buy government bonds """
        pass

    def pay_gov_bonds_interest(self):
        """ A government pays bonds and interests """
        pass

    def offer_new_bonds(self):
        """ A government offers bonds """
        pass
