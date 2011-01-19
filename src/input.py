import pygame
import copy
from pygame.locals import *

class Input:
    """
    The input class
    """
    def __init__(self):
        """
        Initializes the input class
        """
        self.mouse_left = False
        """ Is true when the left mouse button is down """
        self.mouse_left_click = False
        """ Is only true when the left mouse button goes down """
        self.mouse_left_clicked = False
        """ Is only true after the left mouse did go down """
        self.mouse_right = False
        """ Is true when the right mouse button is down """
        self.mouse_right_click = False
        """ Is only true when the right mouse button goes down """
        self.mouse_right_clicked = False
        """ Is only true after the right mouse did go down """
        self.mouse_x = 0
        """ The x position of the mouse """
        self.mouse_y = 0
        """ The y position of the mouse """
        self.keyboard_left = False
        """ Is only true when the left arrow key is down """
        self.keyboard_right = False
        """ Is only true when the right arrow key is down """
        self.keyboard_up = False
        """ Is only true when the up arrow key is down """
        self.keyboard_down = False
        """ Is only true when the down arrow key is down """
        self.keyboard_return = False
        """ Is only true when the return key is down """
        self.keyboard_space = False
        """ Is only true when the spacebar is down """
    def update(self):
        """
        Updates the keyboard class
        """
        self.mouse_left = pygame.mouse.get_pressed()[0]
        self.mouse_right = pygame.mouse.get_pressed()[2]
        if self.mouse_left:
            if self.mouse_left_click == False and self.mouse_left_clicked == False:
                # First time leftbutton got pressed
                self.mouse_left_click = True
            else:
                # Button has been pressed before, and is still being pressed
                self.mouse_left_click = False
                self.mouse_left_clicked = True
        else:
            # Left mouse button isnt clicked at all
            self.mouse_left_click = False
            self.mouse_left_clicked = False

        if self.mouse_right:
            if self.mouse_right_click == False and self.mouse_right_clicked == False:
                # First time right button got pressed
                self.mouse_right_click = True
            else:
                # Button has been pressed before, and is still being pressed
                self.mouse_right_click = False
                self.mouse_right_clicked = True
        else:
            # Right mouse button isnt clicked at all
            self.mouse_right_click = False
            self.mouse_right_clicked = False


        self.mouse_x = pygame.mouse.get_pos()[0]
        self.mouse_y = pygame.mouse.get_pos()[1]
        self.keyboard_left = pygame.key.get_pressed()[K_LEFT]
        self.keyboard_right = pygame.key.get_pressed()[K_RIGHT]
        self.keyboard_up = pygame.key.get_pressed()[K_UP]
        self.keyboard_down = pygame.key.get_pressed()[K_DOWN]
        self.keyboard_return = pygame.key.get_pressed()[K_RETURN]

        self.keyboard_space = pygame.key.get_pressed()[K_SPACE]

    def get_mouse_left_click(self, rect=None):
        """
        Check if the user clicks on something
        if he does make sure it returns a false until the mouse gets released again
        @param rect: The rect the mouse should be in, default value is None (whole screen)
        """
        result = self.mouse_left_click
        if rect:
            if not rect.collidepoint(self.mouse_x, self.mouse_y):
                result = False

        if result:
            self.mouse_left_click = False
            self.mouse_left_clicked = True
        return result

    def copy(self):
        """ Copies the input instance """
        return copy.copy(self)