# -*- coding: utf-8 -*-
""" Agents from the basic macroeconomic model """

from agent.basicAgents import DiscreteEventAgent


class EconomicAgent(DiscreteEventAgent):
    """ A basic economic agent"""
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        self.demmand_satisfied = False
        self.offer_accepted = False
        self.contracted_offers = {}

    def step(self):
        """ Implemented by subclass"""
        pass

    def get_contracted_offers(self, contracted_offers):
        """ The agent get the contracted_offers """
        self.contracted_offers = contracted_offers
        self.demmand_satisfied = True

    def got_contract(self):
        """ the agent got a contract for an offer """
        # TODO: define better - Implemented by subclass
        self.offer_accepted = True

    def release_offer(self):
        """ Agent releases an offer """
        # TODO: Implemented by subclass
        self.offer_accepted = False

    def release_demmand(self):
        """ Agent releases a demmand """
        # TODO: Implemented by subclass
        self.demmand_satisfied = False
