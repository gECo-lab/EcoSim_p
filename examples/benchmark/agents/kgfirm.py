 # -*- coding: utf-8 -*-
""" Capital Good Firm from the basic macroeconomic model 

Example:

The agents are created by the AgentCreator class 
in the AgentCreation muodule
T

      "agents_init": {
        "KGFirm": [
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
from .firm import Firm
from .equations import KGFirmEquations




class KGFirm(Firm):
    """ Capital Goods Firm """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)

        self.eq = KGFirmEquations(self.active_scenario)



    def step(self):
        """ Capital Goods Firm Step 
        """
        self.create_expectations()
        self.compute_desired_output()
        self.compute_labor_demand()
        self.set_output_price()
        self.compute_credit_demand()
        self.select_lending_bank()
        self.produce()
        self.pay_taxes()



    def compute_labor_demand(self):
        """Capital Firms compute labor demand (ndkt)
        """

        self.ndkt = self.eq.ndkt(self.y_c)
