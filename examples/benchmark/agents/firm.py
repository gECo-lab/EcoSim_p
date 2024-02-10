 # -*- coding: utf-8 -*-
""" Generic Firm from the basic macroeconomic model 

Example:

The agents are created by the AgentCreator class 
in the AgentCreation muodule
T

      "agents_init": {
        "EconomicAgent": [
          {
            "var_name": "income",
            "var_type": "stochastic",
            "var_dist": "np.random.lognormal(6.0,1.0)",
            "var_value": 0.0
          }
        ]
        }

Todo:
    * Organize equations cals
"""

from examples.benchmark.agents.goods import ConsumerGood
from .agents import EconomicAgent
from .equations import CGFirmEquations
import random as rnd


class Firm(EconomicAgent):
    """ Generic Firm """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.eq = CGFirmEquations(self.active_scenario)

        ## Household Variables:

        initial_inventory_qnt = rnd.randint(10,50)
        initial_production_price = rnd.randint(1,5)

        initial_production_qnt = rnd.randint(70,100)
        initial_inventory_price = rnd.randint(1,5)

        self.y_c = self.create_initial_production(initial_production_qnt,
                                                         initial_production_price)

        self.inv = self.create_initial_inventory(initial_inventory_qnt,
                                                       initial_inventory_price)
        
 

    def step(self):
        """ Firm Agent Step method """
        ## Implemented By Subclass

    def create_expectations(self):
        """ Firm create expectations 
        """
        self.zet_1 = self.zet
        self.zt = self.zt * (1 + rnd.random())
        self.zet = self.eq.zet(self.zt, self.zet_1)

    def compute_desired_output(self):
        """ Firms compute desired input levels 
        """
        inv = self.inv.c_quantity
        self.y_c = self.eq.ydt(self.zet, inv)

    def compute_labor_demand(self):
        """ Firm compute their labor demand 
        """
        # implemented by subclass

    def set_output_price(self):
        """ Firm sets output price for product """



    def compute_credit_demand(self):
        """ Firm computes demand for credit """


    def select_lending_bank(self):
        """ Firm selects lending bank in the credit market """


    def produce(self):
        """ Firm produces output """


    def offer_goods(self):
        """ Firm offer goods in a market"""


    def pay_loans(self):
        """ Firm pays interest and share of principal on loans """


    def pay_wages(self):
        """ Firm pays wages to households (workers) """


    def create_initial_production(self, quantity, price):
        """Firm creates intitial production of goods

        Args:
            quantity (number): Initial quantity
            price (number): Initial price

        Returns:
            ConsumerGood: A consumer Good Stock
        """

        return ConsumerGood(c_quantity=quantity,
                            c_price=price,
                            c_owner=self,
                            c_producer=self)



    def create_initial_inventory(self, quantity, price):
        """Firm creates intitial production of goods

        Args:
            quantity (number): Initial quantity
            price (number): Initial price

        Returns:
            ConsumerGood: A consumer Good Stock
        """

        return ConsumerGood(c_quantity=quantity,
                            c_price=price,
                            c_owner=self,
                            c_producer=self)


