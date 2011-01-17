import unittest
import pygame
from gui.label import Label
from gui.menu import Menu

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


if __name__ == '__main__':
    unittest.main()