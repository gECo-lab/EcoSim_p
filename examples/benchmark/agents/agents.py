
from kernel.agent.basicAgents import DiscreteEventAgent
from .accounting import Bookkeeper
import random as rnd


class EconomicAgent(DiscreteEventAgent):

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
    def __init__(self, simulation, model, agent_number, agent_def):
        super().__init__(simulation, model, agent_number, agent_def)
        
          # note: these variables need to go to some
          # bookeeping object (that will deal with them)

        self.income = rnd.randint(10,1000)
        self.expenses = rnd.randint(10,1000)
        self.bookkeeper = Bookkeeper(self)
        self.has_offer = False
        self.demand_satisfied = False
        


    def step(self):
        """ Implemented by subclass"""
    

    def get_contracted_offers(self, contracted_offers):
        """ The agent get the contracted_offers """
        self.contracted_offers = contracted_offers
        self.demmand_satisfied = True

    def got_contract(self):
        """ the agent got a contract for an offer """
        # TODO: define better - Implemented by subclass
        pass


    def release_offer(self, an_offer):
        """ Agent releases an offer """
        # TODO: Implemented by subclass
        pass

    def release_demand(self):
        """ Agent releases a demmand """
        # TODO: Implemented by subclass
        self.demand_satisfied = False


    def demand_is_met(self):
        self.demand_satisfied = True
    
    def demand_not_met(self):
        self.demand_satisfied = False



    def pay_taxes(self): 
        """ Economic Agent pay taxes"""

    
    def select_deposit_bank(self):
        """Economic Agent select deposit bank"""


    def pay(self, seller, quantity):
        self.bookkeeper.pay(seller, quantity)

    def receive(self, quantity):
        self.bookkeeper.receive(quantity)


    # def got_good(self, a_good):
    #     self.bookkeeper.got_good(a_good)
    
    def offer_accepted(self, buyer):
        
        self.bookkeeper.offer_accepted(buyer)
        self.has_offer = False
        
    def offer_partially_accepted(self, buyer, an_offer):

        self.bookkeeper.offer_partially_accepted(buyer, an_offer)

    def get_accepted_offers(self, accepted_offers):

        self.bookkeeper.get_accepted_offers(accepted_offers)
   