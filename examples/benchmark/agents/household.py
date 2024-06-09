 # -*- coding: utf-8 -*-
from examples.benchmark.agents.accounting import HHBalanceSheet
from .agents import EconomicAgent
from .goods import Labor
from .equations import Equations
import random as rnd


class Household(EconomicAgent):
    """ Household Agents from the basic macroeconomic model 


    This module implements the Household agent

    Example:

    The agents are created by the AgentCreator class 
    in the AgentCreation module

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

    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
       
        self.balance_sheet = HHBalanceSheet(self)
        self.eq = Equations(self.active_scenario)

        self.Labor_Market = self.get_a_space('Labor_Market')
        self.CG_Market = self.get_a_space("CG_Market")


        ## Household Variables:
        self.demand_qnt = 1 + rnd.randint(100,10000)
        self.demand_expected_price = rnd.randint(10,50)
        self.labor_qnt = rnd.randint(20,60)
        self.hourly_wage = self.compute_reservation_wages()

        ## Create Initial consumer demand
        ## Transfer to Balance Sheet??
        self.consumption_good = self.create_consumer_demand(self.demand_expected_price,
                                                            self.demand_qnt)
      
        ## Create Labor Offer
        ## Transfer to Balance Sheet??
        self.labor = self.create_labor_offer(self.labor_qnt, 
                                             self.hourly_wage)
 

    def step(self):
        """Household Agent Step method
        """

        self.create_expectations()
        self.compute_reservation_wages()
        if self.unemployed:
            self.offer_labor()
            self.receive_dole()
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

        # Todo: Rewrite 
        """
        self.labor.c_quantity =  rnd.randint(20,60)
        self.labor.c_price = self.compute_reservation_wages()
        self.Labor_Market.set_offer(self, self.labor)

    def receive_dole(self):
        """ Unemployed worker receive dole from government

        Todo: Rewrite
        """


    def demand_goods(self):
        """ Household demand goods 
        """
        self.calculate_consumer_demand()
        self.update_consumer_demand()

        ## Make good offer
        self.CG_Market.set_demand(self, self.consumption_good)
                     

    def consume(self):
        """ Household consumes 
        """

        # include payment
        self.consumption_good.c_quantity = 0


  
    def create_consumer_demand(self, expected_price, demand_qnt):
        """Household creates ConsumerGood object

        Args:
            demand_qnt (number): the quantity of demand 

        Returns:
            Consumption (Good): returns a ConsumerGood object
        """

        ## Transfer to Balance Sheet?
            
        return self.balance_sheet.consumption
    

    def update_consumer_demand(self):  
        self.consumption_good.c_quantity = self.demand_qnt

    def calculate_consumer_demand(self):

        self.demand_qnt = 1 + rnd.randint(100,10000)
        return self.demand_qnt



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
    



    

