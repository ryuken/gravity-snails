import unittest
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
        self.team1 = Team("team1")
        self.team2 = Team("team2")
        self.team1.setGravity(Direction.UP)
        self.team2.setGravity(Direction.DOWN)
        
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
        # test if the currentSnailTurn is 0
        self.team1.addSnails(self.maxSnails)
        self.assertEqual(self.team1.currentSnailTurn, 0)
        previousTurnSnail = self.team1.orderedSnailList[self.team1.currentSnailTurn]
        self.assertEqual(previousTurnSnail.hasTurn, True)
        self.team1.nextSnailTurn()
        self.assertEqual(self.team1.currentSnailTurn, 1)
        currentTurnSnail = self.team1.orderedSnailList[self.team1.currentSnailTurn]
        self.assertEqual(previousTurnSnail.hasTurn, False)
        self.assertEqual(currentTurnSnail.hasTurn, True)
    
    def testNextSnailTurnException(self):
        self.team1.addSnails(self.maxSnails)
        
        self.team1.orderedSnailList[0].hasTurn = False
        
        self.assertRaises(ValueError, self.team1.nextSnailTurn)

if __name__ == '__main__':
    unittest.main()