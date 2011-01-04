import unittest

from weapon import Weapon

class TestWeapon(unittest.TestCase):
    """
    A test class for the Weapon module.
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """        
        
        self.weapon = Weapon("Canon", 20)
        self.weapon.ammo = 5
        
        
    def testInitialized(self):
        """
        Test if init goes good
        """
        self.assertEqual(self.weapon.name, "Canon")
        self.assertEqual(self.weapon.power, 20)
        self.assertEqual(self.weapon.ammo, 5)
        
    def testShoot(self):
        self.weapon.shoot()
        self.assertEqual(self.weapon.ammo, 4)
    
if __name__ == '__main__':
    unittest.main()
