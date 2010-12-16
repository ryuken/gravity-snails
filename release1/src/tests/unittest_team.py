import unittest

import sys
sys.path.append("../")

from team import Team

class TestTeam(unittest.TestCase):

    """
    A test class for the Timer module.
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """        
        self.teams= []
        self.team1 = Team("team1", 2)
        self.team2 = Team("team2", 4)
        
        self.team1.addSnails(2)
        self.team2.addSnails(3)
        
        self.teams.append(self.team1)
        self.teams.append(self.team2)
    
    def testInitialized(self):
        """
        Test if init goes good
        """
        self.assertEqual(self.teams[0], self.team1)
        
    def testChangeTurnTeam(self):
        """
        Test if the next time get's the turn
        """
        a = 1
        
    def testChangeTurnSnail(self):
        """
        Test if the next snail get's the turn
        """
        a = 1
        
    def testFirstTurnTeam(self):
        """
        Test if the first team in the team list got the turn when the turnManager starts 
        """
        self.assertEqual(self.turnManager.teams[0].hasTurn, True)
        
    def testFirstTurnSnail(self):
        """
        Test if the first snail of the team who got the turn has the turn
        """
        a = 1

if __name__ == '__main__':
    unittest.main()