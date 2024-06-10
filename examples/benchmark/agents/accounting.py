# -*- coding: utf-8 -*-
from .goods import Good, CapitalGood, ConsumptionGood, Loan, Cash, Labor

class BalanceSheet:
    """
    Represents a balance sheet for an agent in an economic simulation.

    Attributes:
        owner (an Agent): The owner of the balance sheet.
        assets (dictionary): dictionary of assets owned by the agent.
        liabilities (dictionary): dictionary of liabilities owed by the agent.
        cash_flow (dictionary): dictionary of cash flows associated with the agent.
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
    def __init__(self, owner, assets=None, liabilities=None, cash=None):
        self.owner = owner
        if assets is not None:
            if isinstance(assets, dict):
                self.assets = assets
            else:
                raise ValueError("Assets must be a dictionary.")
        else:
            self.assets = {}
        if liabilities is not None:
            if isinstance(liabilities, dict):
                self.liabilities = liabilities
            else:
                raise ValueError("Liabilities must be a dictionary.")
        else:
            self.liabilities = {}

        if cash is not None:
           my_cash = Cash(c_quantity=cash)
        else:
           my_cash = Cash(c_quantity=0.0)
        self.assets[my_cash.c_name] = my_cash

    


    def include_asset(self, asset):
        """
        Includes an asset in the balance sheet.

        Args:
            asset (Good): The asset to be included.

        Raises:
            ValueError: If the asset is not an instance of the Good class.
        """
        if isinstance(asset, Good):
            if asset.c_name in self.assets:
                existing_asset = self.assets[asset.c_name]
                existing_asset.c_quantity += asset.c_quantity
                existing_asset.c_price = (existing_asset.c_price + asset.c_price) / 2
            else:
                self.assets[asset.c_name] = asset
        else:
            raise ValueError("Asset must be an instance of the Good class.")
    
    def exclude_asset(self, asset):
        """
        Excludes an asset from the balance sheet.

        Args:
            asset (Good): The asset to be excluded.
        """
        if asset.c_name in self.assets:
            del self.assets[asset.c_name]
        else:
            raise ValueError("Asset not found in balance sheet.")
 

    def include_liability(self, liability):
        """
        Includes a liability in the balance sheet.

        Args:
            liability (Loan): The liability to be included.

        Raises:
            ValueError: If the liability is not an instance of the Loan class.
        """
        if isinstance(liability, Good):
            if liability.c_name in self.liabilitys:
                existing_liability = self.liabilitys[liability.c_name]
                existing_liability.c_quantity += liability.c_quantity
                existing_liability.c_price = (existing_liability.c_price + liability.c_price) / 2
            else:
                self.liabilitys[liability.c_name] = liability
        else:
            raise ValueError("Liability must be an instance of the Good class.")


    def exclude_liability(self, liability):
        """
        Excludes a liability from the balance sheet.

        Args:
            liability (Loan): The liability to be excluded.
        """
        if liability.c_name in self.assets:
            del self.assets[liability.c_name]
        else:
            raise ValueError("Liability not found in balance sheet.")


    def have_money(self, quantity):
        """
        Returns True if the agent has enough money, False otherwise.

        Args:
            quantity (float): The amount of money to check.

        Returns:
            bool: True if the agent has enough money, False otherwise.
        """
        if "cash" in self.assets:
            my_cash = self.assets["cash"].c_quantity
            return my_cash >= quantity
        else:
            raise ValueError("Cash not found in Balance Sheet")


    def pay(self, an_agent, quantity):
        """
        Pays a specified amount to another agent.

        Args:
            an_agent_balance_sheet (BalanceSheet): The balance sheet of the agent to pay.
            quantity: The amount of money to pay.

        Returns:
            bool: True if the payment was successful, False otherwise.
        """
        if self.have_money(quantity):
            self.assets["cash"].c_quantity -= quantity
            an_agent.balance_sheet.receive(quantity)
            return True
        else:
            return False        

    def receive(self, quantity):
        """
        Receives a specified amount of money.

        Args:
            quantity: The amount of money to receive.
        """
        self.assets["cash"].c_quantity += quantity

    def get_good(self, a_good):

        self.include_asset(a_good)






class HHBalanceSheet(BalanceSheet):

    def __init__(self, owner, assets=None, liabilities=None, 
                 cash=None, consumption=None):
        super().__init__(owner, assets, liabilities, cash)

        if consumption is not None:
            if isinstance(consumption, dict):
                self.consumption = consumption
            else:
                raise ValueError("consumption must be a dictionary.")
        else:
            self.consumption = ConsumptionGood(c_name=owner.name,
                                               c_owner=self.owner)
        

    def get_good(self, a_good):

        if isinstance(a_good, Good):
            self.assets.append(a_good)
        elif isinstance(a_good, Loan):
            self.liabilities.append(a_good)
        elif isinstance(a_good, ConsumptionGood):
            self.add_consumption_goods(a_good)
    

    def add_consumption_goods(self, consumption):
        
        self.consumption.c_quantity = consumption.c_quantity
        self.consumption.c_price = (self.consumption.c_price +
                                    consumption.c_price)/2
        
            





