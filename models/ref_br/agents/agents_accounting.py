# -*- coding: utf-8 -*-
"""
This is the accounting module
This module contains all the necessary classes to do
"""
##########################################
# Quais os tipos específicos de bens?
# Que possíveis métodos ainda são necessários???
# Como implementar os protocolos de mercado????
# Ver nd-004 e nd-005
###########################################

class Contract(object):
    """
  
        A contract is a class that has:
            - a_creditor (an agent, can be self)
            - a_debtor (an agent, can be self)
            - a_market (a market where the contract occurs)
            - an_asset - associated with the contract (of creditor)
            - a_liability - associated with the contract (of debtor)
            - a_payment (from debitor to creditor)
            - periods (number of periods of the payments)
            - actual_periods (the actual period of the contrac)
            - value - value of the contract
            - actual_value - the actual value of the contract


        :version: 0.0.1
        :author: SLMR
    """

    CONTRACT_TYPES = ['credit', 'purchase', 'rent']

    def __init__(self, type_of_contract, 
                 a_creditor, 
                 a_debtor, 
                 a_market, 
                 an_asset, 
                 a_liability, 
                 a_payment_value, 
                 periods,
                 value):
            
        """ Initialize the contract """

        if type_of_contract in self.CONTRACT_TYPES:
            self.type_of_contract = type_of_contract
        else:
            raise Exception("Type of contract not valid - type: ", type_of_contract)
    
        self.creditor = a_creditor
        self.debtor = a_debtor
        self.market = a_market
        self.asset = an_asset
        self.liability = a_liability
        self.payment_value = a_payment_value
        self.periods = periods
        self.actual_periods = 0
        self.value = value
        self.actual_value = value


    def payment(self, a_payment):
        """
            Payment

            @return float :
            @author
        """
        if self.actual_periods >= 1:
            if a_payment >= self.payment_value:
                self.actual_value -= a_payment
                self.actual_periods -= 1


class Good(object):
    """A Basic Class representing a good."""
    TYPE = ["real", "financial"]

    """
        w  - Wages
        cg - Consumer_Good
        k  - Capital
        ph - Dividends
        d  - Deposit
        l  - Loan
        id - Interests on deposits
        il - Interests on loans
        b  - Bonds
        ib - Interests on bonds
        gw - Government wages
        gt - Government transfers (to households)
        ho - House
    """

    ASSET_CATEGORY = ['w', 'cg', 'k', 'ph', 'd', 'l', 'id', 'il', 'b', 'ib', 'gw', 'gt', 'ho']

    CONSUME = ["immediate", "depreciable", "debt", "continuous"]

    def __init__(self, name_of_g,
                 type_of_g,      # real or financial
                 asset_category_of_g,
                 consume_of_g,   # immediate, depreciable, debt or continuous
                 quantity_of_g=None,
                 value_of_g=None,
                 owner_of_g=None,
                 producer_of_g=None):
        """" Init method for a generic good """
        self.name_of_g = name_of_g

        if type_of_g in self.TYPE:
            self.type_of_g = type_of_g
        else:
            raise Exception("Type of ", name_of_g, " not valid - type: ", type_of_g)

        if asset_category_of_g in self.ASSET_CATEGORY:
            self.asset_category_of_g = asset_category_of_g
        else:
            raise Exception("Type of asset of :  ", name_of_g, "  not valid - type: ", asset_category_of_g)

        if consume_of_g in self.CONSUME:
            self.consume_of_g = consume_of_g
        else:
            raise Exception("Type of consume from ", name_of_g, " not valid - consume: ", consume_of_g)
        if quantity_of_g is not None:
            self.quantity_of_g = quantity_of_g 
        if value_of_g is not None:
            self.value_of_g = value_of_g
        if owner_of_g is not None:
            self.owner_of_g = owner_of_g
        if producer_of_g is not None:
            self.producer_of_g = producer_of_g

    def estimated_value(self, a_quantity_of_g):
        """ Calculates the estimated value of a good given a quantity as input """
        return self.value_of_g * a_quantity_of_g

    def total_value(self):
        """ Calculates the estimated value of a good for the existing quantity """
        return self.value_of_g * self.quantity_of_g


class House(Good):
    """A house"""

    QUALITY = [0,1,2,3,4,5,6,7,8,9]


    def __init__(self, name_of_g,
                 type_of_g="real",      # real or financial
                 asset_category_of_g='ho',
                 consume_of_g='depreciable',   # immediate, depreciable, debt or continuous
                 quantity_of_g='1',
                 value_of_g=None,
                 owner_of_g=None,
                 producer_of_g=None,
                 a_tenant=None,
                 quality=None) -> None:
        """House"""
        super().__init__(name_of_g,
                 type_of_g='real',      # real or financial
                 asset_category_of_g='ho',
                 consume_of_g='depreciable',   # immediate, depreciable, debt or continuous
                 quantity_of_g='1',
                 value_of_g=value_of_g,
                 owner_of_g=owner_of_g,
                 producer_of_g=producer_of_g)

        self.name_of_g = name_of_g if name_of_g is not None else 'house'
        self.tenant = a_tenant
        self.quality = quality
        self.rent = 0.0
        self.age = 0
        self.cost = 0.0
        self.mark_up = 0.0

    def new_owner(self, new_owner):
        """A house changes owner"""
        self.owner_of_g = new_owner

    def rent(self, a_tenant, rent):
        """Renting a House"""
        self.tenant = a_tenant
        self.rent = rent