"""Basic Economic Agent

This module implements the basic functions of an economic agent 
in the benchmark model. The ``EconomicAgent`` class implements the basic 
actions for the economic agents in the model. 

Example:
        To create an economic agent we must include the agent definition 
        in the ``model.json`` file. The definition can be done as follows:

         "agents": [
                {
                "agent_type": "EconomicAgent",
                "agent_prefix": "EA",
                "agent_spaces": [
                    "Market"
                ],
                "no_of_agents": 500
                }
            ],

This will create 500 instances of the class EconomicAgent in the model and will
include the agents in the ``space`` ``Market``.

Economic agents are subclass of DiscreteEventAgent in the model kernel.
            

Todo:
    * implement agent methods

"""

from kernel.agent.basicAgents import DiscreteEventAgent


class EconomicAgent(DiscreteEventAgent):
    """ A basic economic agent"""
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        

    def step(self):
        """ Implemented by subclass"""
      

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
