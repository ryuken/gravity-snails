import unittest

import sys
sys.path.append("../")

from team import Team
from enums import Direction

class TestTeam(unittest.TestCase):

    """
    A test class for the Timer module.
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """        
        self.maxSnails = 5
        self.team1 = Team("team1", Direction.UP)
        self.team2 = Team("team2", Direction.UP)
        
        
    
    def testInitialized(self):
        """
        Test if init goes good
        """
        self.assertEqual(self.team1.name, "team1")
        self.assertEqual(self.team1.hasTurn, False)
    
    def testAddSnails(self):
        self.team1.addSnails(self.maxSnails)
        self.assertEqual(self.team1.currentSnailTurn, 0)
        self.assertEqual(len(self.team1.sprites()), self.maxSnails)
        self.assertEqual(len(self.team1.orderedSnailList), self.maxSnails)
        self.assertEqual(self.team1.orderedSnailList[0].hasTurn, True)
        for i in range(0, len(self.team1.orderedSnailList)):
            if i == 0:
                self.assertEqual(self.team1.orderedSnailList[i].hasTurn, True)
            else:
                self.assertEqual(self.team1.orderedSnailList[i].hasTurn, False)
        self.assertEqual
        
    def testNextSnailTurn(self):
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