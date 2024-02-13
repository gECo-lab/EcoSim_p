 # -*- coding: utf-8 -*-
""" Bank Agent from the basic macroeconomic model 


This module implements the Bank agent

Example:

The agents are created by the AgentCreator class 
in the AgentCreation muodule
T

      "agents_init": {
        "Bank": [
          {
            "var_name": "credit",
            "var_type": "stochastic",
            "var_dist": "np.random.lognormal(6.0,1.0)",
            "var_value": 0.0
          }
        ]
        }

Todo:

"""

from .agents import EconomicAgent
from .equations import Equations
import random as rnd


class Bank(EconomicAgent):
    """ Bank Agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.eq = Equations(self.active_scenario)
        

        ## Bank Variables:

    def step(self):
        """ Bank Agent Step method """
        self.create_expectations()
        self.compute_interest_loans()
        self.compute_interest_deposits()
        self.evaluate_loan_requests()
    


    def create_expectations(self):
        self.zet_1 = self.zet
        self.zt = self.zt * (1 + rnd.random())
        self.zet = self.eq.zet(self.zt, self.zet_1)

    def compute_interest_loans(self):
        """ Bank Compute the interest on loans """


    def compute_interest_deposits(self):
        """ Bank Compute the interest on deposits """

    def evaluate_loan_requests(self):
        """ Bank evaluate loan requests """    

    def supply_credit(self):
        """ Bank supply demanded credit """    

    def pay_interest(self):
        """ Bank pays interest on deposits """
        
