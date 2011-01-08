import unittest
import pygame
from gui.label import Label
from menu import Menu

class TestMenu(unittest.TestCase):
    """
    A test class for the Label module.
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        pygame.init()
        self.menu = Menu()
        self.menu.size['width'] = 1
        self.menu.size['height'] = 1
        self.initialMenuSize = self.menu.size

    def testAutoResize(self):
        mySmallLabel = Label("Some very really really tiny small nonsense")
        self.menu.addOption(mySmallLabel)
        self.assertTrue(self.initialMenuSize['width'] < self.menu.size['width'])


if __name__ == '__main__':
    unittest.main()