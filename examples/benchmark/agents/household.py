 # -*- coding: utf-8 -*-
""" Household Agents from the basic macroeconomic model 


This module implements the Household agent

Example:

The agents are created by the AgentCreator class 
in the AgentCreation muodule

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
        self.market = self.spaces['Market']

        ## Household Variables:
        demand_qnt = 1 + rnd.randint(1,10)
        labor_qnt = rnd.randint(20,60)
        hourly_wage = self.compute_reservation_wages()

        ## Create Initial consumer demand
        self.consumer_good = self.create_consumer_demand(demand_qnt)
      
        ## Create Labor Offer
        self.labor = self.create_labor_offer(labor_qnt, hourly_wage)
 

    def step(self):
        """Household Agent Step method
        """

        self.create_expectations()
        self.compute_reservation_wages()
        if self.unemployed:
            self.offer_labor()
        self.demand_goods()
        self.consume()
        self.pay_taxes()


    def compute_reservation_wages(self):
        """ Workers Compute their reservation wages

        Todo: Rewrite  
        """

        return 1 + rnd.randint(1,10)


    def offer_labor(self):
        """ Worker offer labor in labor market

        Todo: Rewrite 
        """
        
        self.labor.c_quantity =  rnd.randint(20,60)
        self.labor.c_price = self.compute_reservation_wages()
        self.market.set_offer(self, self.labor)


    def demand_goods(self):
        """ Household demand goods 
        """

       ## Make good offer
        self.market.set_demand(self, self.consumer_good)
                     

    def consume(self):
        """ Household consumes 
        """
        self.consumer_good.c_quantity = 1 + rnd.randint(1,10)


  
    def create_consumer_demand(self, demand_qnt):
        """Household creates ConsumerGood object

        Args:
            demand_qnt (number): the quantity of demand 

        Returns:
            CosumerGood (Good): returns a ConsumerGood object
        """
            
        return ConsumerGood(c_quantity=demand_qnt,
                                     c_owner = self)
    


    def create_labor_offer(self, labor_qnt, hourly_wage):
        """Household creates labor offer

        Args:
            labor_qnt (number): quantity of available labor
            hourly_wage (number): the minimum hourly wage

        Returns:
            Labor (Good): returns a Labor object
        """
        
        return Labor(c_quantity=labor_qnt, 
                     c_price=hourly_wage, 
                     c_owner=self, 
                     c_producer=self)
        


    

