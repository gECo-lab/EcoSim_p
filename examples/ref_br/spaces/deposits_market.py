# Space Class  Implementation

from .market import Market


class DepositsMarket(Market):
    """ The Deposits Market"""

    def deposit(self, a_bank, an_agent, amount):
        """ An agent deposits some amount in its' account """
        pass

    def cash(self, a_bank, an_agent, amount):
        """ An agent cash some amount from its' account """
        pass

    def pay(self, a_bank_to_cash, a_bank_to_deposit, payer, receiver, ammount):
        """ An agent pays some amount to a receiver """
        pass

    def interests_on_deposits(self, a_bank):
        """ A bank decides the interest rates on deposits """
        pass

    def pay_unempl_benefits(self):
        """The government pays unemployment benefits to households"""
        pass

    def transfer_profits_gov(self):
        """ Central Bank transfer profits to Government """
        pass
