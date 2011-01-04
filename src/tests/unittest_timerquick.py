import unittest

import sys
sys.path.append("../")
import pygame
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
        pygame.init()
        self.team1.addSnails(2)
        self.team2.addSnails(3)

        self.teams.append(self.team1)
        self.teams.append(self.team2)

        self.turnManager = TurnManager()
        self.turnManager.setTeams(self.teams)

#    def testInitialized(self):
#        """
#        Test if init goes good
#        """
#        self.assertEqual(self.turnManager.teams, self.teams)
#        self.assertEqual(self.turnManager.teams[0], self.team1)
#        self.assertEqual(self.turnManager.teams[1], self.team2)
#
#        self.assertEqual(self.turnManager.status, TurnStatus.BREAK)
#        self.assertEqual(self.turnManager.startTime, Settings.TIMER_STARTTIME)
#        self.assertEqual(self.turnManager.size, Settings.TIMER_SIZE)
#        self.assertEqual(self.turnManager.position, Settings.TIMER_POSITION)
#        self.assertEqual(self.turnManager.font_size, Settings.TIMER_FONT_SIZE)

    def testSingleton(self):
        """
        Test if the singleton works
        """
        turnmanager2 = TurnManager()
        self.assertEqual(id(self.turnManager), id(turnmanager2))




if __name__ == '__main__':
    unittest.main()