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


        self.create_initial_values()
     


    def step(self):
        """ Consumer Goods Firm Step 
        """
        self.create_expectations()
        self.compute_desired_output()
        self.compute_capacity_utilization()
        self.compute_labor_demand()
        self.demand_labor()
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


    def create_expectations(self):
        """Agent Creates Expectations
        """
        self.Se_ct = self.eq.zet(self.Se_ct, 
                                          self.Se_ct_1)
        # Expected sales
        self.Se_ct_1 = self.Se_ct

    def compute_desired_output(self):
        """ Firms compute desired input levels 
        """
        self.yd_ct.c_quantity = self.eq.ydt(self.Se_ct, 
                                           self.inv_ct_1.c_quantity
                                           )
        
        self.yd_ct_q = self.yd_ct.c_quantity



    def compute_capacity_utilization(self):
        """CG Firm computes capacity utilization
        """

        self.ud_ct = self.eq.udct(self.yd_ct.c_quantity,
                                self.K_ct.c_quantity
                               )
    
 


    def compute_labor_demand(self):
        """Consumer good firm computes labor demand
        """

        self.lay_off_from_turnover()

        self.Ndc_t_1 = self.Ndc_t_1    
        self.Ndc_t = self.eq.ndct(self.K_ct.c_quantity, self.ud_ct)
  
        self.N_ct = self.Ndc_t - self.Ndc_t_1

        if self.N_ct > 0:
            self.labor_demand.c_quantity = self.N_ct
        elif self.N_ct < 0:
            self.N_ct *= -1
            self.lay_off(self.N_ct)

    def lay_off(self, N_ct):
        """ Lay of the employees"""
        self.bookkeeper.lay_off(N_ct) 

    def lay_off_from_turnover(self):
        """ Lay of the employees"""
        self.bookkeeper.lay_off_from_turnover(self.eq.upsilon)    

        

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


    def set_output_price(self):
        """ Firm sets output price for product """

        self.y_ct.c_price =self.eq.pt(self.mu_ct,
                                      self.We_t,
                                      self.Ndc_t,
                                      self.y_ct.c_quantity+1
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
    
        self.y_ct.c_quantity=self.yd_ct.c_quantity
        self.y_ct.c_price=self.yd_ct.c_price
        self.update_inventory(self.y_ct)
        

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
        self.bookkeeper.set_offer(space, self.inv_ct)

    def update_inventory(self, y):

        self.inv_ct_1 = self.inv_ct

        self.inv_ct.c_price = (self.inv_ct.c_price + y.c_price)/2
        self.inv_ct.c_quantity += y.c_quantity



    def create_initial_values(self):
        """
        Creates the initial values for various attributes of the CGFirm class.

        This method initializes the following attributes:
        - inv_ct: Inventory quantity and price
        - yd_ct: Desired production quantity and price
        - y_ct: Actual production quantity and price
        - Se_ct: Expected sales quantity and price
        - K: Capital stock quantity and price
        - s_ct: Sales quantity and price
        - We_xt: Initial salaries
        - labor_demand: Initial labor demand

        Returns:
        None

        TODO: This will be changed to calibration in initialization.
        """
        # Inventory (inv_ct)
        initial_inventory_qnt = rnd.randint(10,50)
        initial_inventory_price = rnd.randint(1,5)
        self.inv_ct= self.create_initial_inventory(initial_inventory_qnt,
                                            initial_inventory_price)

        # Inventory t-1 (inv_ct_1)
        initial_inventory_t_1_qnt = rnd.randint(10,50)
        initial_inventory_t_1_price = rnd.randint(1,5)
        self.inv_ct_1= self.create_initial_inventory(initial_inventory_t_1_qnt,
                                            initial_inventory_t_1_price)


        # Desired output (yd_ct)
        initial_desired_production_qnt = rnd.randint(70,100)
        initial_desired_production_price = rnd.randint(1,5)
        self.yd_ct = self.create_initial_production(initial_desired_production_qnt,
                                                  initial_desired_production_price)


        # Production (output) (y_ct)
        initial_production_qnt = rnd.randint(70,100)
        initial_production_price = rnd.randint(1,5)
        self.y_ct = self.create_initial_production(initial_production_qnt,
                                                  initial_production_price)
        
        # Expected Sales
        self.Se_ct = rnd.randint(70,100)
        self.Se_ct_1 = rnd.randint(70,100)
        

        # Capital
        # Capital Stock need to be  actually a dict. 
        # With different machines
        # TODO: Implement capital stock as a dict
        initial_K_stock_qnt = rnd.randint(2,5)
        initial_K_stock_price = rnd.randint(2,5)
        self.K_ct = self.create_initial_K_stock(initial_K_stock_qnt,
                                             initial_K_stock_price)


        # Sales
        initial_sales_qnt = rnd.randint(50,90)
        initial_sales_price = rnd.randint(1,5)
        self.s_ct = self.create_initial_sales(initial_sales_qnt, 
                                             initial_sales_price)
        
        ## Generate initial salaries (We_xt)
        self.ud_ct = rnd.random()
        self.We_xt = rnd.randint(10, 50)
        self.Ndc_t = rnd.randint(10, 50)
        self.Ndc_t_1 = rnd.randint(10, 50)
        self.labor_demand = self.create_initial_labor_demand(self.Ndc_t, 
                                                             self.We_xt)
        self.bookkeeper.include_asset(self.labor_demand)
   

       
