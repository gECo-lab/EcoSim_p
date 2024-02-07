"""Economic Agent Basic Equations

This module implements the economic agent basic equations. 
Each equation is maitained as an independent method inside 
the equations class.
Subclasses will implement specific equations 
for different agents.

Example:

from equations import Equations


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
        self.nu = self.active_scenario.nu
        self.l_k = self.active_scenario.l_k
        self.mu_k = self.active_scenario.mu_k



## General Equations  

    def zet(self, zt, zet_1):
        return zet_1 + self.expect_lambda*(zt - zet_1) 
    

    def ydt(self, s_et, inv_t_1):

        return s_et * (1 + self.nu * inv_t_1)
    
 

class CGFirmEquations(Equations):
    """Consumer Goods Firm specific equations

    Args:
        Equations (Object): Specific equations for consumer goods firm
    """

    def ndt(self, y_c):
        """Calculates the labor demmand for CG firms

        Args:
            y_c (number): Expected production of consumer goods
            mu_k (number): Capital Productivity at some technology
            l_k (number): Fixed capital/labor ratio

        Returns:
            N_ct: Number of workers needed
        """
        return y_c/self.mu_k*self.l_k
