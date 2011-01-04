import unittest

from inventory import Inventory
from weapon import Weapon

class TestInventory(unittest.TestCase):
    """
    A test class for the Inventory module.
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """        
        
        self.inv = Inventory()
        
        self.weapon = Weapon("Canon", 20)
        self.inv.addWeapon(self.weapon)
        
        
    def testInitialized(self):
        """
        Test if init goes good
        """

        self.assertEqual(self.weapon.name, "Canon")
        self.assertEqual(self.weapon.power, 20)
        
        self.assertEqual(len(self.inv.weapons), 1)
        self.assertEqual(self.inv.weapons[0], self.weapon)
    
if __name__ == '__main__':
    unittest.main()