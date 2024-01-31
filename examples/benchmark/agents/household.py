 # -*- coding: utf-8 -*-
""" Household Agents from the basic macroeconomic model 


This module implements the Household agent

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

from .agents import EconomicAgent
from .equations import Equations
from .goods import ConsumerGood, Labor
import random as rnd


class Household(EconomicAgent):
    """ Household Agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.eq = Equations(self.active_scenario)
        

        ## Household Variables:

    def step(self):
        """ Household Agent Step method """
        self.create_expectations()
        self.compute_reservation_wages()
        if self.unemployed:
            self.offer_labor()
        self.demand_goods()
        self.consume()
        self.pay_taxes()


    def create_expectations(self):
        self.zet_1 = self.zet
        self.zt = self.zt * (1 + rnd.random())
        self.zet = self.eq.zet(self.zt, self.zet_1)

    def compute_reservation_wages(self):
        """ Workers Compute their reservation wages """
        self.hourly_wage = 1 + rnd.randint(1,10)


    def offer_labor(self):
        """ Worker offer labor in labor market """
        self.labor_qnt = 40

        self.offered_labor = Labor(c_quantity=self.labor_qnt,
                                   c_price=self.hourly_wage,
                                     c_owner = self,
                                     c_producer=self)



    def demand_goods(self):
        """ Household demand goods """
        self.demand_qnt = 1 + rnd.randint(1,10)

        self.c_demand = ConsumerGood(c_quantity=self.demand_qnt,
                                     c_owner = self)

    def consume(self):
        """ Household consumes """



        
