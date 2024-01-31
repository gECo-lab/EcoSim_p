""" Commodities

This module implements the commodities traded in an economy.
Subclasses will implement specific goods if necessary.

Example:


Todo:

"""

class Commodity(object):
    """A Basic Class representing a good."""
    
    TYPE = ["real", "financial"]

    """
        w  - wages (from Workers Labor)
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
                  'gt']
    

    CONSUME = ["immediate", "depreciable", "debt", "continuous"]

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




class ConsumerGood(Commodity):
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
                 c_quantity = None,
                 c_price = None,
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




class Labor(Commodity):
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




