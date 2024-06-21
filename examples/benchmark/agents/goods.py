""" Goods

This module implements the commodities traded in an economy.
Subclasses will implement specific goods if necessary.

Example:


Todo:

"""

class Good(object):
    """A Basic Class representing a good."""
    
    TYPE = ["real", "financial"]

    """
        w  - Labor (wages are the payment for labor)
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
        csh - Cash 
    """

    c_CATEGORY = ['w', 
                  'cg', 
                  'k', 
                  'ph', 
                  'd', 
                  'l', 
                  'id', 
                  'il', 
                  'b', 
                  'ib', 
                  'gw', 
                  'gt',
                  'csh']
    

    CONSUME = ["immediate", "depreciable", "debt", "continuous", "cash"]

    def __init__(self, 
                 c_name,
                 c_type,      # real or financial
                 c_category,
                 c_consume,   # immediate, depreciable, debt or continuous
                 c_quantity,
                 c_price,
                 c_owner=None,
                 c_producer=None):
        
        """" Init method for a generic good """

        self.c_name = c_name

        if c_type in self.TYPE:
            self.c_type = c_type
        else:
            raise Exception("Type of ", c_name, " not valid - type: ", c_type)

        if c_category in self.c_CATEGORY:
            self.c_category = c_category
        else:
            raise Exception("Type of asset of :  ", c_name, "  not valid - type: ", c_category)

        if c_consume in self.CONSUME:
            self.c_consume = c_consume
        else:
            raise Exception("Type of consume from ", c_name, " not valid - consume: ", c_consume)

        self.c_quantity = c_quantity
        self.c_price = c_price
        self.c_owner = c_owner
        self.c_producer = c_producer

    def c_value(self):
        "Return the value of good - c_price * c_quantity"
        return self.c_price * self.c_quantity
 
    def ammount(self):
        "Return the value of good - c_price * c_quantity"
        return self.c_price * self.c_quantity

    
    def copy_attributes(self, a_good):
        """Copy attributes from self to a_good if they are of the same class."""
        if isinstance(a_good, self.__class__):
            for attr in self.__dict__:
                setattr(a_good, attr, getattr(self, attr))
        return a_good


class ConsumptionGood(Good):
    """A Consumer Good
    
       TYPE :"real"

       c_CATEGORY: cg - Consumer_Good

       CONSUME: immediate
    """

    def __init__(self, 
                 c_name = None,
                 c_type = None,  
                 c_category = None,
                 c_consume = None,  
                 c_quantity = 0.0,
                 c_price = 0.0,
                 c_owner=None,
                 c_producer=None):
        
        """" Init method for a consumption good """

        self.c_name = "consumer good"
        self.c_type = "real"
        self.c_category = "cg"
        self.c_consume = "immediate"
        self.c_quantity = c_quantity
        self.c_price = c_price
        self.c_owner = c_owner
        self.c_producer = c_producer


class CapitalGood(Good):
    """A Capital Good
    
       TYPE :"real"

       c_CATEGORY: kg Capital_Good

       CONSUME: depreciable
    """

    def __init__(self, 
                 c_name = None,
                 c_type = None,  
                 c_category = None,
                 c_consume = None,  
                 c_quantity = None,
                 c_price = None,
                 c_owner=None,
                 c_producer=None):
        
        """" Init method for a consumption good """

        self.c_name = "capital good"
        self.c_type = "real"
        self.c_category = "kg"
        self.c_consume = "depreciable"
        self.c_id = 0
        self.c_quantity = c_quantity
        self.c_price = c_price
        self.c_owner = c_owner
        self.c_producer = c_producer




class Labor(Good):
    """A Consumer Good
    
       TYPE :"real"

       c_CATEGORY: w - Labor (and wages)

       CONSUME: immediate
    """

    def __init__(self, 
                 c_name = None,
                 c_type = None,  
                 c_category = None,
                 c_consume = None,  
                 c_quantity = None,
                 c_price = None,
                 c_owner=None,
                 c_producer=None):
        
        """" Init method for Workers Labor """

        self.c_name = "labor"
        self.c_type = "real"
        self.c_category = "w"
        self.c_consume = "immediate"
        self.c_quantity = c_quantity
        self.c_price = c_price
        self.c_owner = c_owner
        self.c_producer = c_producer


class Loan(Good):

      def __init__(self, 
                 c_name = None,
                 c_type = None,  
                 c_category = None,
                 c_consume = None,  
                 c_quantity = None,
                 c_price = None,
                 c_owner=None,
                 c_producer=None):
        
        """" Init method for Loans """

        self.c_name = "loan"
        self.c_type = "financial"
        self.c_category = "l"
        self.c_consume = "debt"
        self.c_quantity = c_quantity
        self.c_price = c_price
        self.c_owner = c_owner
        self.c_producer = c_producer

class Cash(Good):

      def __init__(self, 
                 c_name = None,
                 c_type = None,  
                 c_category = None,
                 c_consume = None,  
                 c_quantity = None,
                 c_price = 1,
                 c_owner=None,
                 c_producer=None):
        
        """" Init method for Workers Labor """

        self.c_name = "cash"
        self.c_type = "financial"
        self.c_category = "csh"
        self.c_consume = "cash"
        self.c_quantity = c_quantity
        self.c_price = 1
        self.c_owner = c_owner
        self.c_producer = None








