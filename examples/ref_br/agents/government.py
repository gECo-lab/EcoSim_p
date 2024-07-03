# -*- coding: utf-8 -*-
""" Agents from the basic macroeconomic model """

from .agents import EconomicAgent


class Government(EconomicAgent):
    """ The Government economic agetn """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.credit_market = self.spaces['CreditMarket']
        #self.deposits_market = self.spaces['DepositsMarket']

    def step(self):
        """ Step method for Government Agent """
        pass