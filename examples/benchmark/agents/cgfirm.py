 # -*- coding: utf-8 -*-
""" Consumer Goods Firm Agent from the basic macroeconomic model 


This module implements the Household agent

Example:

The agents are created by the AgentCreator class 
in the AgentCreation muodule
T

      "agents_init": {
        "CGFirm": [
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
from .equations import CGFirmEquations
from .goods import CapitalGood, ConsumptionGood, Labor
import random as rnd


class CGFirm(Firm):
    """ Consumers Goods Firm """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        
        self.eq = CGFirmEquations(self.active_scenario)
        
        self.labor_mkt_name = "Labor_Market"
        self.cg_mkt_name = "CG_Market"

        ## TODO: This will be changed to calibration in initialization.

        initial_inventory_qnt = rnd.randint(10,50)
        initial_production_price = rnd.randint(1,5)

        initial_production_qnt = rnd.randint(70,100)
        initial_inventory_price = rnd.randint(1,5)

        ## Generate initial salaries (We_xt)
        self.We_xt = rnd.randint(10, 50)

     

        self.y_c = self.create_initial_production(initial_production_qnt,
                                                  initial_production_price)

        self.inv = self.create_initial_inventory(initial_inventory_qnt,
                                                 initial_inventory_price)

        

        initial_K_stock_qnt = rnd.randint(2,5)
        initial_K_stock_price = rnd.randint(2,5)

        initial_sales_qnt = rnd.randint(50,90)
        initial_sales_price = rnd.randint(1,5)

        self.K = self.create_initial_K_stock(initial_K_stock_qnt,
                                             initial_K_stock_price)
        
        self.s_c = self.create_initial_sales(initial_sales_qnt, 
                                             initial_sales_price)
        
        self.compute_labor_demand()
        self.labor_demand = self.create_initial_labor_demand(self.Ndc_t, self.We_xt)
        


    def step(self):
        """ Consumer Goods Firm Step 
        """
        self.create_expectations()
        self.compute_desired_output()
        self.compute_labor_demand()
        self.demand_labor()
        self.compute_capacity_utilization()
        self.set_output_price()
        self.compute_rate_of_capacity_growth()
        self.compute_demand_of_K_goods()
        self.choose_K_supplier()
        self.compute_credit_demand()
        self.select_lending_bank()
        self.produce()
        self.offer_goods()
        self.buy_K_goods()
        self.pay_loans()
        self.pay_wages()
        self.distribute_dividends()
        self.select_deposit_bank()
        self.pay_taxes()


    def compute_desired_output(self):
        """ Firms compute desired input levels 
        """
        inv = self.inv.c_quantity
        self.y_c.c_quantity = self.eq.ydt(self.zet, 
                                          inv
                                         )
        
    def compute_labor_demand(self):
        """Consumer good firm computes labor demand
        """
        #Todo: Needs to recalculate unity price of labor (We_xt)

        # self.We_xt

        self.Ndc_t = self.eq.ndct(self.y_c.c_quantity)


    def demand_labor(self):
        """
        Sets the labor demand for the firm in the labor market.

        This method sets the labor demand for the firm in the 
        specified labor market.
        
        It calls the `set_demand` method of the labor market 
        object to update the demand.

        Parameters:
        - self: The current instance of the CGFirm class.

        Returns:
        - None
        """
        self.get_a_space(self.labor_mkt_name).set_demand(self, self.labor_demand)


    def compute_capacity_utilization(self):
        """CG Firm computes capacity utilization
        """

        self.ud_t = self.eq.udt(self.y_c.
                                c_quantity,
                                self.kc_t
                               )

    def set_output_price(self):
        """ Firm sets output price for product """

        self.y_c.c_price =self.eq.pt(self.mu_ct,
                                      self.We_t,
                                      self.Ndc_t,
                                      self.y_c.c_quantity
                                     )

    def compute_rate_of_capacity_growth(self):
        """CG Firms compute their rate of capacity growth 
        """

    def compute_demand_of_K_goods(self):
        """ With the expected rate of capacity growth CG firms
            Compute their demand for K goods 
        """

    def choose_K_supplier(self):
        """ CG firms choose their capital supplier in K market 
        """

    def buy_K_goods(self):
        """ CG Firms buy capital goods
        """

    def create_initial_production(self, quantity, price):
        """Firm creates intitial production of goods

        Args:
            quantity (number): Initial quantity
            price (number): Initial price

        Returns:
            ConsumptionGood: A consumer Good Stock
        """

        self.y_ct =  ConsumptionGood(c_quantity=quantity,
                            c_price=price,
                            c_owner=self,
                            c_producer=self)
        return self.y_ct
    

    def create_initial_inventory(self, quantity, price):
        """Firm creates intitial production of goods

        Args:
            quantity (number): Initial quantity
            price (number): Initial price

        Returns:
            ConsumptionGood: A consumer Good Stock
        """

        return ConsumptionGood(c_quantity=quantity,
                            c_price=price,
                            c_owner=self,
                            c_producer=self)
    

    def create_initial_K_stock(self, quantity, price):
            """Firm creates intitial Capital Stock

            Args:
                quantity (number): Initial quantity
                price (number): Initial price

            Returns:
                CapitalGood: A Capital Goods Stock
            """

            return CapitalGood(c_quantity=quantity,
                                c_price=price,
                                c_owner=self,
                                c_producer=None)
    

    def create_initial_sales(self, quantity, price):
        """Firm creates intitial sales of goods

        Args:
            quantity (number): Initial quantity
            price (number): Initial price

        Returns:
            ConsumptionGood: A consumption Good (sold)
        """

        return ConsumptionGood(c_quantity=quantity,
                            c_price=price,
                            c_owner=self,
                            c_producer=self)
    

    def create_initial_labor_demand(self, Ndc_t, We_xt):

        return Labor(c_quantity = Ndc_t,
                     c_price=We_xt,
                     c_owner=self,
                     c_producer=self)
    

    def produce(self):
        """CG firm produce consumption goods"""
        # NOTE: This method is just to test the market. Needs developing
    
        self.y_ct.c_quantity=self.y_c.c_quantity
        self.y_ct.c_price=self.y_c.c_price
        

    def offer_goods(self):
        """
        Sets the offer of goods for the CG Market.

        This method sets the offer of goods for the CG Market
        by calling the `set_offer` method of the `CG_Market` object.

        Parameters:
        - None

        Returns:
        - None
        """
        self.has_offer = True
        space = self.get_a_space(self.cg_mkt_name)
        self.bookkeeper.set_offer(space, self.y_ct)
