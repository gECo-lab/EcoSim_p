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

from .agents import EconomicAgent



class Firm(EconomicAgent):
    """ Generic Firm """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)

       

    def step(self):
        """ Firm Agent Step method """
        ## Implemented By Subclass


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

    def distribute_dividends(self):
        """Firm distributes dividends to households
        """




