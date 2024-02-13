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
from examples.benchmark.agents.goods import CapitalGood
from .firm import Firm
from .equations import KGFirmEquations
import random as rnd





class KGFirm(Firm):
    """ Capital Goods Firm """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)

        self.eq = KGFirmEquations(self.active_scenario)

        ## These variables can be initialised in json scenario file.
        initial_sales_qnt = rnd.randint(50,90)
        initial_sales_price = rnd.randint(1,5)

        initial_inventory_qnt = rnd.randint(10,50)
        initial_production_price = rnd.randint(1,5)

        initial_production_qnt = rnd.randint(70,100)
        initial_inventory_price = rnd.randint(1,5)

     

        self.y_c = self.create_initial_production(initial_production_qnt,
                                                         initial_production_price)

        self.inv = self.create_initial_inventory(initial_inventory_qnt,
                                                       initial_inventory_price)
        

        self.s_c = self.create_initial_sales(initial_sales_qnt, 
                                             initial_sales_price)


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

        self.Ndk_t = self.eq.ndkt(self.y_c.c_quantity)

    def set_output_price(self):
        """ Firm sets output price for product """

        self.y_c.c_price =self.eq.pt(self.mu_kt, self.We_t, self.Ndk_t, self.y_c.c_quantity)

    def create_initial_inventory(self, quantity, price):
        """Firm creates intitial production of goods

        Args:
            quantity (number): Initial quantity
            price (number): Initial price

        Returns:
            ConsumerGood: A consumer Good Stock
        """

        return CapitalGood(c_quantity=quantity,
                            c_price=price,
                            c_owner=self,
                            c_producer=self)
    

    def create_initial_production(self, quantity, price):
        """Firm creates intitial production of goods

        Args:
            quantity (number): Initial quantity
            price (number): Initial price

        Returns:
            ConsumerGood: A consumer Good Stock
        """

        return CapitalGood(c_quantity=quantity,
                            c_price=price,
                            c_owner=self,
                            c_producer=self)
     
      



  
