import unittest
from team import Team
from enums import Direction

class TestTeam(unittest.TestCase):
    """
    A test class for the Team module.
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """        
        self.maxSnails = 3
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
        self.assertEquals(self.team1.currentSnailWithTurn, self.team1.orderedSnailList[0])
        self.assertEqual(len(self.team1.sprites()), self.maxSnails)
        self.assertEqual(len(self.team1.orderedSnailList), self.maxSnails)
        self.assertEqual(self.team1.orderedSnailList[0].hasTurn, True)
        for i in range(0, len(self.team1.orderedSnailList)):
            if i == 0:
                self.assertEqual(self.team1.orderedSnailList[i].hasTurn, True)
            else:
                self.assertEqual(self.team1.orderedSnailList[i].hasTurn, False)
        
    def testNextSnailTurn(self):
        """
        Test if the next time get's the turn
        """
        # test if the currentSnailTurn is 0
        self.team1.addSnails(self.maxSnails)
        
        # Check when all the snails had the turn, if the first snail gets turn again
        for i in range(0, self.maxSnails):
            print i
            self.assertEqual(self.team1.orderedSnailList[i].hasTurn, True)
            self.team1.nextSnailTurn()
            self.assertEqual(self.team1.orderedSnailList[i].hasTurn, False)
            
            
        # check if the first snail in the list has the turn again
        self.assertEqual(self.team1.orderedSnailList[0].hasTurn, True)
    
        
    

#    def testIsDead(self):
#        self.team1.addSnails(self.maxSnails)
#        
#        # Get the middle snail
#        middleSnail = self.team1.orderedSnailList[self.maxSnails / 2]
#        self.assertTrue(self.team1.isAlive())
#        for snail in self.team1.orderedSnailList:
#            snail.kill()
#        self.assertFalse(self.team1.isAlive())
            
if __name__ == '__main__':
    unittest.main()