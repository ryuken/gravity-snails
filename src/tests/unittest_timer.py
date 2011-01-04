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
        self.teams= []
        self.team1 = Team("team1")
        self.team2 = Team("team2")

        self.team1.addSnails(2)
        self.team2.addSnails(3)

        self.teams.append(self.team1)
        self.teams.append(self.team2)

        self.turnManager = TurnManager()
        self.turnManager.setTeams(self.teams)

    def testInitialized(self):
        """
        Test if init goes good
        """
        self.assertEqual(self.turnManager.teams, self.teams)
        self.assertEqual(self.turnManager.teams[0], self.team1)
        self.assertEqual(self.turnManager.teams[1], self.team2)

        self.assertEqual(self.turnManager.status, TurnStatus.BREAK)
        self.assertEqual(self.turnManager.startTime, Settings.TIMER_STARTTIME)
        self.assertEqual(self.turnManager.size, Settings.TIMER_SIZE)
        self.assertEqual(self.turnManager.position, Settings.TIMER_POSITION)
        self.assertEqual(self.turnManager.font_size, Settings.TIMER_FONT_SIZE)

    def testSingleton(self):
        """
        Test if the singleton works
        """
        turnmanager2 = TurnManager()
        turnmanager3 = TurnManager()
        self.assertEqual(id(self.turnManager), id(turnmanager2))


    def testBreak(self):
        """
        Test if the turnManager's status switches from CurrentTurn to Break when counter is 0
        """
        self.assertEqual(self.turnManager.status, TurnStatus.BREAK)
        self.turnManager.startTimer()

        time.sleep(Settings.TIMER_BREAKTIME + 2)

        self.assertEqual(self.turnManager.status, TurnStatus.CURRENTTURN)

        time.sleep(Settings.TIMER_STARTTIME + 2)
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
        self.turnManager.startTimer()
        self.assertEqual(self.turnManager.teams[0].hasTurn, True)

        time.sleep(Settings.TIMER_BREAKTIME + Settings.TIMER_STARTTIME + 5)

        self.assertEqual(self.turnManager.teams[0].hasTurn, False)
        self.assertEqual(self.turnManager.teams[1].hasTurn, True)

    def testChangeTurnSnail(self):
        """
        Test if the next snail get's the turn
        """
        a = 1

    def testFirstTurnTeam(self):
        """
        Test if the first team in the team list got the turn when the turnManager starts
        """
        self.turnManager.startTimer()
        time.sleep(2)
        self.assertEqual(self.turnManager.teams[0].hasTurn, True)
        self.assertEqual(self.turnManager.teams[1].hasTurn, False)
        self.turnManager.stopTimer()

    def testFirstTurnSnail(self):
        """
        Test if the first snail of the team who got the turn has the turn
        """
        # the first snail who gets the turn is the first snail of team 1
        firstSnailID = self.turnManager.teams[0].currentSnailTurn
        # the 2nd snail who gets the turn is the first snail of team 2
        secondSnailID = self.turnManager.teams[1].currentSnailTurn

        self.turnManager.startTimer()
        self.assertEqual(self.turnManager.teams[0].hasTurn, True)
        self.assertEqual(self.turnManager.teams[0].currentSnailTurn, firstSnailID)

#        time.sleep(Settings.TIMER_BREAKTIME + Settings.TIMER_STARTTIME + 5)
#
#        self.assertEqual(self.turnManager.teams[0].hasTurn, False)
#        self.assertEqual(self.turnManager.teams[1].hasTurn, True)
#        self.assertEqual(self.turnManager.teams[1].currentSnailTurn, secondSnailID)

        self.turnManager.stopTimer()

if __name__ == '__main__':
    unittest.main()