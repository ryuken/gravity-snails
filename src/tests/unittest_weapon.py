import unittest

from weapon import Weapon
from team import Team
from turnmanager import TurnManager

class TestWeapon(unittest.TestCase):
    """
    A test class for the Weapon module.
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """        
        self.turnManager = TurnManager()
        self.teams = []
        
        self.team = Team("Akatsuki")
        self.team.addSnails(1)
        self.teams.append(self.team)
        
        self.turnManager.setTeams(self.teams)
        
        self.snail = None
        for snail in self.team.sprites():
            self.snail = snail
        
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