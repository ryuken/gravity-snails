import unittest

import sys
sys.path.append("../")

from team import Team
from turnmanager import TurnManager
from settings import Settings
from enums import TurnStatus
import time

class TestTimer(unittest.TestCase):

    """
    A test class for the Timer module.
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        
        self.team1 = Team("team1", 2)
        self.team2 = Team("team2", 4)
        self.teams= []
        self.teams.append(self.team1)
        self.teams.append(self.team2)
        
        self.turnManager = TurnManager(self.teams)
    
    def testInitialized(self):
        """
        Test if init goes good
        """
        self.assertEqual(self.turnManager.teams, self.teams)
        self.assertEqual(self.turnManager.status, TurnStatus.BREAK)
        self.assertEqual(self.turnManager.startTime, Settings.TIMER_STARTTIME)
        self.assertEqual(self.turnManager.size, Settings.TIMER_SIZE)
        self.assertEqual(self.turnManager.position, Settings.TIMER_POSITION)
        self.assertEqual(self.turnManager.font_size, Settings.TIMER_FONT_SIZE)
        
    def testBreak(self):
        """
        Test if the turnManager's status switches from CurrentTurn to Break when counter is 0
        """
        self.assertEqual(self.turnManager.status, TurnStatus.BREAK)
        self.turnManager.startTimer()
        
        time.sleep(Settings.TIMER_BREAKTIME + 2)
        
        self.assertEqual(self.turnManager.status, TurnStatus.CURRENTTURN)
        
        time.sleep(Settings.TIMER_STARTTIME + 7)
        self.assertEqual(self.turnManager.status, TurnStatus.BREAK)
        self.turnManager.stopTimer()
    
    def testCurrentTurn(self):
        """
        Test if the turnManager's status switches from Break to CurrentTurn when counter is 0
        """
        self.assertEqual(self.turnManager.status, TurnStatus.BREAK)
        self.turnManager.startTimer()
        
        time.sleep(Settings.TIMER_BREAKTIME + 2)
        
        self.assertEqual(self.turnManager.status, TurnStatus.CURRENTTURN)
        self.turnManager.stopTimer()
        
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