"""Contracts

This module implements the Contract class, which represents a contract between a seller and a buyer.

Attributes:
    CONTRACT_TYPE (list): A list of valid contract types.

Classes:
    Contract: Represents a contract between a seller and a buyer.

"""

CONTRACT_TYPE = ["loan",
                 "c_good",
                 "k_good",
                 "job",
                 "finance"
                 ]


class Contract:
    """
    Represents a contract between a seller and a buyer.

    Attributes:
        seller (str): The name of the seller.
        buyer (str): The name of the buyer.
        amount (float): The total amount of the contract.
        time (int): The duration of the contract in months.
        price (float): The price per unit of the contract.
        qt_payments (int): The total number of payments to be made.
        type (str): The type of the contract.
        paid (float): The total amount paid towards the contract.
        current_debt (float): The remaining debt to be paid.
        due_payments (int): The number of payments yet to be made.

    Methods:
        make_payment: Makes a payment towards the current debt.

    """

    def __init__(self, supplier, contractor, amount, time, price, qt_payments, type):
        self.seller = supplier
        self.contractor = contractor
        self.amount = amount
        self.time = time
        self.price = price
        self.qt_payments = qt_payments
        self.paid = 0.0
        self.current_debt = self.amount
        self.due_payments = self.qt_payments

        if type in self.CONTRACT_TYPE:
            self.type = type
        else:
            raise Exception("Type of contract: ", type, " - not valid")

    def make_payment(self, value, no_of_payments):
        """
        Makes a payment towards the current debt.

        Args:
            value (float): The value of the payment.
            no_of_payments (int): The number of payments made.

        Returns:
            None
        """
        self.paid += value
        self.current_debt -= value
        self.due_payments -= no_of_payments