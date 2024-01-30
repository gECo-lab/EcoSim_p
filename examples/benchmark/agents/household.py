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
        self.consume()
        self.pay_taxes()


    def create_expectations(self):
        self.zet_1 = self.zet
        self.zt = self.zt * (1 + rnd.random())
        self.zet = self.eq.zet(self.zt, self.zet_1)

    def compute_reservation_wages(self):
        """ Workers Compute their reservation wages """


    def offer_labor(self):
        """ Worker offer labor in labor market """

    def consume(self):
        """ Household consumes """



        
