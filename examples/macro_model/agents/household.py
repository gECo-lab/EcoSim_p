 # -*- coding: utf-8 -*-
""" Household Agents from the basic macroeconomic model """

from .agents import EconomicAgent

from .agents_accounting import Good


class Household(EconomicAgent):
    """ Household Agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.labor_market = self.spaces['LaborMarket']
        self.employed = False

    def step(self):
        """ Household Agent Step method """
        if not self.employed:
            self.generate_offer()
            self.offer_workforce()
        self.formulate_price_expectations()
        self.calculate_income()
        self.establish_demmand()
        self.buy_goods()
        self.pay_taxes()

    def show_offer(self):
        """ Show Offer The agent show an offer in some market """
        print(" I, ", self.name,
              "am offering ",
              self.labor_offer.quantity_of_g,
              "hour of work at ",
              self.labor_offer.value_of_g,
              "hourly wage."
              )

    def generate_offer(self):
        """ The Household decides wage to offer """
        self.decide_hourly_wage()
        self.labor_offer = Good('Labor',
                                'real',
                                'w',
                                'immediate',
                                self.labor_capacity,
                                self.hourly_wage,
                                self,
                                self)

    def decide_hourly_wage(self):
        """ The Household decides wage to offer """
        self.hourly_wage = self.labor_market.average_labor_price()
        if self.hourly_wage == 0.0:
            self.hourly_wage = self.expected_wage

    def offer_workforce(self):
        """ The Household offer its workforce """
        self.labor_market.bid_market('O', self.labor_offer)
        self.offered_workforce = True

    def formulate_price_expectations(self):
        """ The household formulates price expectations for consumer goods """
        pass

    def calculate_income(self):
        """ The household calculates its income """
        pass

    def establish_demmand(self):
        """ The HH establish its demmand """
        pass

    def buy_goods(self):
        """ The HH buy goods in the goods market """
        pass

    def pay_taxes(self):
        """ The HH pay taxes to the government """
        pass

    def got_contract(self):
        """ The household is employed """
        self.employed = True

    def reslease_bid(self):
        """ The agent now is unemployed """
        self.labor_offer = None
        self.employed = False
