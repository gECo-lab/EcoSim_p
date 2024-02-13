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

from scipy.stats import foldnorm



class Equations():
    """ The equations class for the benchmark model implementation"""
    def __init__(self, active_scenario):
        self.active_scenario = active_scenario

        ## Constants
        self.expect_lambda = self.active_scenario.expect_lambda
        self.nu = self.active_scenario.nu
        self.l_k = self.active_scenario.l_k
        self.mu_k = self.active_scenario.mu_k
        self.mu_n = self.active_scenario.mu_n


    def zet(self, zt, zet_1):
        """Compute expectations in t

        Args:
            zt (number): Value in t (production, income, revenue)
            zet_1 (number): Value in t - 1 (production, income, revenue)

        Returns:
            number: expectations in T
        """

        return zet_1 + self.expect_lambda*(zt - zet_1) 
    

    def ydt(self, s_et, inv_t_1):
        """Compute production in T

        Args:
            s_et (number): Expected sales in t
            inv_t_1 (number): Inventory in t - 1

        Returns:
            number: Production in t
        """

        return s_et * (1 + self.nu * inv_t_1)
    
    def udt(self, yd_t, kc_t):
        """Calculates rate of utilization of capital stock

        Args:
            yd_t (number): production in t
            kc_t (number): capital stock in t

        Returns:
            float: rate of utilization (0 < udt <= 1)
        """

        return min(1, yd_t/(kc_t*self.mu_k))
    
    def uvc(self, We_xt, Nd_xt, yd_xt):

        return (We_xt * Nd_xt)/yd_xt
    

    def pt(self, mu_xt, We_xt, Nd_xt, yd_xt):
        """Calculates production prices

        Args:
            mu_xt (number): markup for firms in t
            We_xt (number): unity price of labor in t
            Nd_xt (number): quantity of labor in t
            yd_xt (number): production in t

        Returns:
            number: unitary price of good in t
        """

        return (1 + mu_xt)*(We_xt * Nd_xt)/yd_xt
    

    def muxt(self, mu_xt, inv_t_1, s_et):
        """Updates mark-up

        Args:
            mu_xt (number): Mark-up
            inv_t_1 (number): Inventories in t
            s_et (number): Sales in t
            self.nu (number): desired inventory proportion

        Returns:
            number: new mark-up
        """

        FN = foldnorm.rvs(self.nu, size=1)

        if inv_t_1/s_et <= self.nu:
            return mu_xt + (1 + FN)
        else:
            return mu_xt + (1 - FN)
        
    def sales(self, s_ct):
        """Calculate sales value

        Args:
            s_ct (consumerGood): _description_

        Returns:
            number: Total value of sales
        """

        return s_ct.c_quantity * s_ct.c_price
    

    def interest(self, i_d):

        return i_d.c_quantity * i_d.c_price
    

    def inventory(self, inv):

        return inv.c_quantity * inv.c_price
    

    def revenue(self, s_ct, i_d, inv):
        
        sales = self.sales(s_ct)
        interest = self.interest
        inv_costs = self.inventory()

        return sales + interest + inv_costs


    
 

class CGFirmEquations(Equations):
    """Consumer Goods Firm specific equations

    Args:
        Equations (Object): Specific equations for consumer goods firm
    """

    def ndct(self, y_c):
        """Calculates the labor demmand for CG firms

        Args:
            y_c (number): Expected production of consumer goods
            mu_k (number): Capital Productivity at some technology
            l_k (number): Fixed capital/labor ratio

        Returns:
            N_ct: Number of workers needed
        """

        return y_c/self.mu_k*self.l_k
    

class KGFirmEquations(Equations):
    """Capital goods firm specific equations

    Args:
        Equations (Object): Equations for capital goods firm
    """

    def ndkt(self, y_c):
        """Calculates Labor demand for capital firms

        Args:
            y_c (number): desired output

        Returns:
            ndkt: Labor demand for capital firms
        """

        return y_c/self.mu_n