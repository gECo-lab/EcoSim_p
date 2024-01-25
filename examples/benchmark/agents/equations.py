"""Economic Agent Basic Equations

This module implements the economic agent basic equations. 
Each equation is maitained as an independent method inside the equations class.
Subclasses will implement specific equations for different agents.

Example:

from equations import HouseholdEquations


Todo:
    * Organize equations calss

"""

import numpy as np
import random as rnd

class Equations():
    """ The equations class for the benchmark model implementation"""
    def __init__(self, active_scenario):
        self.active_scenario = active_scenario

        ## Constants
        self.expect_lambda = self.active_scenario.expect_lambda



## General Equations  

    def zet(self, zt, zet_1):
        return zet_1 + self.expect_lambda*(zt - zet_1) 




