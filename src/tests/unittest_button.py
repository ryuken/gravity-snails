import unittest
import pygame
from button import Button
from input import Input
class TestButton(unittest.TestCase):
    """
    A test class for the Button module.
    """

    def setUp(self):
        """
        set up data used in the tests.
        setUp is called before each test function execution.
        """
        pygame.init()        
        self.button = Button(pygame.Rect(0,0,64,64), "Test")
        self.button.register_action(self.callback)
        self.got_clicked = False
        self.input = Input()
        
    def testClickedButton(self):
        self.input.mouse_x = 32
        self.input.mouse_y = 32
        self.input.mouse_left = True
        
        self.button.update(self.input)
        self.assertTrue(self.got_clicked)
        
    def testClickedSomethingElse(self):
        self.input.mouse_x = 128
        self.input.mouse_y = 128
        self.input.mouse_left = True
        
        self.button.update(self.input)
        self.assertFalse(self.got_clicked)
        
    def callback(self):
        self.got_clicked = True
        
        
if __name__ == '__main__':
    unittest.main()