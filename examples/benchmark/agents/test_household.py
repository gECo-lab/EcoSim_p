import unittest
from .household import Household

class TestHousehold(unittest.TestCase):

    def test_create_consumer_demand(self):
        household = Household()
        demand_qnt = 10
        consumer_good = household.create_consumer_demand(demand_qnt)
        
        self.assertEqual(consumer_good.c_quantity, demand_qnt)
        self.assertEqual(consumer_good.c_owner, household)

if __name__ == '__main__':
    unittest.main()