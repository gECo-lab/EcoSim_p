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


class Firm(EconomicAgent):
    """ Generic Firm """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.eq = Equations(self.active_scenario)

        ## Household Variables:

    def step(self):
        """ Firm Agent Step method """
        ## Implemented By Subclass

    def create_expectations(self):
        """ Firm create expectations """
        self.zet_1 = self.zet
        self.zt = self.zt * (1 + rnd.random())
        self.zet = self.eq.zet(self.zt, self.zet_1)

    def compute_desired_output(self):
        """ Firms compute desired input levels """

    def compute_labor_demand(self):
        """ Firm compute their labor demand """

    def set_output_price(self):
        """ Firm sets output price for product """

    def compute_credit_demand(self):
        """ Firm computes demand for credit """

    def select_lending_bank(self):
        """ Firm selects lending bank in the credit market """




        


class CGFirm(Firm):
    """ Consumers Goods Firm """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)


    def step(self):
        """ Consumers Good Step """
        self.create_expectations()
        self.compute_desired_output()
        self.compute_labor_demand()
        self.set_output_price()
        self.compute_rate_of_capacity_growth()
        self.compute_demand_of_K_goods()
        self.choose_K_supplier()
        self.compute_credit_demand()
        self.select_lending_bank()
        


    def compute_rate_of_capacity_growth(self):
        """ CG Firms compute their rate of capacity growth """

    def compute_demand_of_K_goods(self):
        """ With the expected rate of capacity growth CG firms
            Compute their demand for K goods 
        """

    def choose_K_supplier(self):
        """ CG firms choose their capital supplier in K market """
    

class KGFirm(Firm):
    """ Capital Goods Firm """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)


    def step(self):
        """ Consumers Good Step """
        self.create_expectations()
        self.compute_desired_output()
        self.compute_labor_demand()
        self.set_output_price()
        self.compute_credit_demand()
        self.select_lending_bank()

