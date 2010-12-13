import unittest

import sys
sys.path.append("../")

from game import Game
from team import Team
from timer import Timer

class testTimer(unittest.TestCase):

    """
    A test class for the Timer module.
    """


    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        self.game = Game()
        
        self.game.addTeam("team1", 2)
        self.game.addTeam("team2", 4)
        
        self.timer = Timer(position=(0,0), size=(20,20), startTime="30", teams=self.game.teams)


    def testFirstTurn(self):
        self.assertEqual(self.timer.teams[0].hasTurn, True)

def suite():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(testTimer))

    return suite


if __name__ == '__main__':

    #unittest.main()

    suiteFew = unittest.TestSuite()

    suiteFew.addTest(testFirstTurn())

    unittest.TextTestRunner(verbosity=2).run(suiteFew)

    #unittest.TextTestRunner(verbosity=2).run(suite())