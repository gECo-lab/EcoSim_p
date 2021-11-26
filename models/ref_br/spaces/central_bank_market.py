# Space Class  Implementation

from .market import Market

class CentralBankMarket(Market):
    """ The Real State Market """

    def __init__(self, model, name, actions_set_file, action_class, variables):
        """ Intialize abstract market """
        super().__init__(model, name, actions_set_file, action_class, variables)
        self.policy_updated = True

    
    def update(self):
        """
        The Central Bank updates policy
        """
        if self.policy_updated:
            for agent in self.agents.values():
                agent.notify_policy(self.interest_rate, self.macroprudential_policy)
            self.policy_updated = False
        


    def policy_update(self, interest_rate, macroprudential_policy):
        """Receive update of Central Bank Policy """
        self.interest_rate = interest_rate
        self.macroprudential_policy = macroprudential_policy
        self.policy_updated = True
        
