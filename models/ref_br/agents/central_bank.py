# -*- coding: utf-8 -*-
""" Agents from the basic macroeconomic model """

from .agents import EconomicAgent


class CentralBank(EconomicAgent):
    """ The Central Bank economic agent """
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.credit_market = self.spaces['CreditMarket']
        self.central_bank_market = self.spaces['CentralBankMarket']
        self.first = True
        self.update_interval = 12

    def step(self):
        """ Step method for the Central bank Agent """
        if (self.my_step % self.update_interval) == 0:
            self.decide_monetary_policy()
            

    def decide_monetary_policy(self):
        """Central Bank decides monetary policy"""

        self.central_bank_market.policy_update(
            self.interest_rate,
            self.macroprudential_policy
        )

