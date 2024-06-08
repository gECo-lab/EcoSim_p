# -*- coding: utf-8 -*-
from numpy import  number
from .goods import CapitalGood, Loan, Cash
import random as rnd

class BalanceSheet:
    """
    Represents a balance sheet for an agent in an economic simulation.

    Attributes:
        owner (an Agent): The owner of the balance sheet.
        assets (list): List of assets owned by the agent.
        liabilities (list): List of liabilities owed by the agent.
        cash_flow (list): List of cash flows associated with the agent.
        cash (Cash): The amount of cash owned by the agent.

    Methods:
        __init__(self, owner, assets=None, liabilities=None, cash_flow=None, cash=None): 
            Initializes a new instance of the BalanceSheet class.
        include_asset(self, asset): Includes an asset in the balance sheet.
        exclude_asset(self, asset): Excludes an asset from the balance sheet.
        include_liability(self, liability): Includes a liability in the balance sheet.
        exclude_liability(self, liability): Excludes a liability from the balance sheet.
        include_cash_flow(self, cash_flow): Includes a cash flow in the balance sheet.
        exclude_cash_flow(self, cash_flow): Excludes a cash flow from the balance sheet.
        have_money(self, quantity): Checks if the agent has enough money.
        pay(self, an_agent_balance_sheet, quantity): Pays a specified amount to another agent.
        receive(self, quantity): Receives a specified amount of money.
    """

    # TODO: include consumption (deal with this for firms)

    def __init__(self, owner, assets=None, liabilities=None, cash_flow=None, cash=None):
        self.owner = owner
        if assets is not None:
            if isinstance(assets, list):
                self.assets = assets
            else:
                raise ValueError("Assets must be a list.")
        else:
            self.assets = []

        if liabilities is not None:
            if isinstance(liabilities, list):
                self.liabilities = liabilities
            else:
                raise ValueError("Liabilities must be a list.")
        else:
            self.liabilities = []

        if cash_flow is not None:
            if isinstance(cash_flow, list):
                self.cash_flow = cash_flow
            else:
                raise ValueError("Cash Flow must be a list.")
        else:
            self.cash_flow = []
        if cash is not None:
            if isinstance(cash, number):
                self.cash.c_quantity =+ cash
            else:
                raise ValueError("Cash must be a number")
        else:
            self.cash = Cash(c_quantity=rnd.randint(100,10000),
                             c_owner=self.owner)


    def include_asset(self, asset):
        """
        Includes an asset in the balance sheet.

        Args:
            asset (CapitalGood): The asset to be included.

        Raises:
            ValueError: If the asset is not an instance of the CapitalGood class.
        """
        if isinstance(asset, CapitalGood):
            self.assets.append(asset)
        else:
            raise ValueError("Asset must be an instance of the CapitalGood class.")
        self.assets.append(asset)


    def exclude_asset(self, asset):
        """
        Excludes an asset from the balance sheet.

        Args:
            asset (CapitalGood): The asset to be excluded.
        """
        self.assets.remove(asset)
 

    def include_liability(self, liability):
        """
        Includes a liability in the balance sheet.

        Args:
            liability (Loan): The liability to be included.

        Raises:
            ValueError: If the liability is not an instance of the Loan class.
        """
        if isinstance(liability, Loan):
            self.assets.append(liability)
        else:
            raise ValueError("Liability must be an instance of the Loan class.")
        self.liabilities.append(liability)


    def exclude_liability(self, liability):
        """
        Excludes a liability from the balance sheet.

        Args:
            liability (Loan): The liability to be excluded.
        """
        self.liabilities.remove(liability)


    def include_cash_flow(self, cash_flow):
        """
        Includes a cash flow in the balance sheet.

        Args:
            cash_flow: The cash flow to be included.
        """
        self.cash_flow.append(cash_flow)

    def exclude_cash_flow(self, cash_flow):
        """
        Excludes a cash flow from the balance sheet.

        Args:
            cash_flow: The cash flow to be excluded.
        """
        self.cash_flow.remove(cash_flow)


    def have_money(self, quantity):
        """
        Checks if the agent has enough money.

        Args:
            quantity: The amount of money to check.

        Returns:
            bool: True if the agent has enough money, False otherwise.
        """
        if self.cash.c_quantity >= quantity:
            return True
        else:
            return False


    def pay(self, an_agent_balance_sheet, quantity):
        """
        Pays a specified amount to another agent.

        Args:
            an_agent_balance_sheet (BalanceSheet): The balance sheet of the agent to pay.
            quantity: The amount of money to pay.

        Returns:
            bool: True if the payment was successful, False otherwise.
        """
        if self.have_money(quantity):
            self.cash.c_quantity =- quantity
            an_agent_balance_sheet.receive(quantity)
            return True
        else:
            return False
        

    def receive(self, quantity):
        """
        Receives a specified amount of money.

        Args:
            quantity: The amount of money to receive.
        """
        self.cash.c_quantity =+ quantity


    