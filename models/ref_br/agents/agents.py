# -*- coding: utf-8 -*-
""" Agents from the basic macroeconomic model """

from agent.basicAgents import DiscreteEventAgent


class EconomicAgent(DiscreteEventAgent):
    """ A basic economic agent"""
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.demand_satisfied = False
        self.offer_accepted = False
        self.contracted_offers = {}

    def step(self):
        """ Implemented by subclass"""
        pass

    def get_contracted_offers(self, contracted_offers):
        """ The agent get the contracted_offers """
        self.contracted_offers = contracted_offers
        self.demand_satisfied = True

    def got_contract(self, contracted_offer):
        """ the agent got a contract for an offer """
        # TODO: define better - Implemented by subclass
        self.offer_accepted = True
        self.contracted_offer = contracted_offer

    def release_offer(self):
        """ Agent releases an offer """
        # TODO: Implemented by subclass
        self.offer_accepted = False

    def release_demand(self):
        """ Agent releases a demmand """
        # TODO: Implemented by subclass
        self.demand_satisfied = False

    def notify_policy(self, interst_rate, macroprudential_policy):
        """ The agent receives notification for interest rate 
            and macroprudential policy 
        """
        self.interst_rate = interst_rate
        self.macroprudential_policy = macroprudential_policy
