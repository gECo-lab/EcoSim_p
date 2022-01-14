# -*- coding: utf-8 -*-
""" Banks from the basic macroeconomic model """
from numpy import random
from numpy.lib.shape_base import column_stack

from .agents import EconomicAgent
from .agents_accounting import Good, House



class Bank(EconomicAgent):
    """ A Bank economic agent """

    MARKET = 'CreditMarket'
    MARKET_NAME = 'Bank'

    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.credit_market = self.spaces['CreditMarket']
        self.first = True
        self.offered_houses = dict()
        self.previous_demand = 0


    def step(self):
        """ Step method for a bank """
        self.check_monetary_policy_rules()
        self.decides_credit_limits()

        self.form_expectations()

        self.offer_credit()

        if self.first:
            self.cb = self.get_cb()
            self.generate_first_offer()            
            self.first = False
        else:
            self.generate_offer()
        
        self.update_statistics()

        self.contract_credit()


    def check_monetary_policy_rules(self):
        """ The Bank checks the monetary policy rules in Central Bank """
        ## Note: Looks like the Central Bank can send the
        ## Monetary policy rules as a message
        pass

    def decides_credit_limits(self):
        """ 
           The bank, using it internal rules stablish the credit limits 
           to households 
        """
        pass

    def offer_credit(self):
        """ The bank offers credit in the credit market """
        ## Note: Each credit "opportunity" is a house
        ## with price and financing - its a financial good
        pass

    def contract_credit(self):
        """ The bank contracts the matched credit offers from the credit market """
        ## Note: see if the contract is Before the other actions in this step
        pass

    def get_cb(self):
        """ Get Central Bank from model """
        return self.model.agents_of_type("CentralBank")

    def get_government(self):
        """ Get government from model """
        return self.model.agents_of_type('Government')

    def generate_first_offer(self):
        """ The Construction Firm Generates its first offer """
        for i in range(1,self.housing_offer):
            house_name = "h_" + str(i)
            self.generate_house(house_name)
            

    def form_expectations(self):
         """ 
             The agent establish its expectations about the demmand 
         """
         self.offered_houses.clear()
         lower = int(self.housing_demand * .8)
         high = int(self.housing_demand * 1.2)
         house_it = self.step

         self.housing_offer = random.randint(lower, high)
    
         for i in range(1,self.housing_offer):
             house_name = "h_" + str(house_it) + "_" + str(i)
             house = self.generate_house(house_name)
             house.mark_up = house.mark_up * (1 + random.normal(0.2, 0.05))
             house.value_of_g = house.cost + (1 + house.mark_up)
            
    def generate_offer(self):
        """ The construction firm generates the number of houses in the REM """
        for house in self.offered_houses.values():
            self.credit_market.bid_market("O", house)
    
    def generate_house(self, house_name):
        """ 
            Returns a house price 
            A price is price plus mark_up.
        """
        self.scenario.initialize_one_var("house_cost", 
                                         self.MARKET_NAME,
                                         self)
        self.scenario.initialize_one_var("mark_up", 
                                         self.MARKET_NAME,
                                         self)
        self.house_price = self.house_cost * (1 + self.mark_up) 
        house = House(house_name,
                          value_of_g=self.house_price,
                          owner_of_g=self, 
                          producer_of_g=self
                          )
        
        house.cost = self.house_cost
        house.mark_up = self.mark_up
        self.offered_houses[house.name_of_g] = house
        
        return house

    def got_contract(self, contracted_offer):
        """ the agent got a contract for an offer """
        self.offer_accepted = True
        self.contracted_offer = contracted_offer
        house_name = contracted_offer.name_of_g
        bought_house = self.offered_houses.pop(house_name)
        self.revenue += bought_house.value_of_g

    def update_statistics(self):
        """ Update some variables """
        s_mark_up = 0
        s_cost = 0
        s_price = 0
        for house_name, house in self.offered_houses.items():
            s_mark_up += house.mark_up
            s_cost += house.cost
            s_price += house.value_of_g
        
        offered_houses_n = self.offered_houses.__len__()
        if offered_houses_n > 0:
            self.avg_mark_up = s_mark_up/offered_houses_n
            self.avg_house_cost = s_cost/offered_houses_n
            self.avg_house_price = s_price/offered_houses_n
        else:
            self.avg_mark_up = s_mark_up/1
            self.avg_house_cost = s_cost/1
            self.avg_house_price = s_price/1
        self.total_house_cost = s_cost
