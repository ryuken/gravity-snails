import pygame
from pygame.locals import *

class Input:
    def __init__(self):
        self.mouse_left = False
        self.mouse_left_click = False
        self.mouse_left_clicked = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.keyboard_left = False
        self.keyboard_right = False
        self.keyboard_up = False
        self.keyboard_down = False
        self.keyboard_return = False
        self.keyboard_space = False
    def update(self):
        self.mouse_left = pygame.mouse.get_pressed()[0]
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
            
        self.mouse_x = pygame.mouse.get_pos()[0]
        self.mouse_y = pygame.mouse.get_pos()[1]
        self.keyboard_left = pygame.key.get_pressed()[K_LEFT]
        self.keyboard_right = pygame.key.get_pressed()[K_RIGHT]
        self.keyboard_up = pygame.key.get_pressed()[K_UP]
        self.keyboard_down = pygame.key.get_pressed()[K_DOWN]
        self.keyboard_return = pygame.key.get_pressed()[K_RETURN]
        self.keyboard_space = pygame.key.get_pressed()[K_SPACE]
        
    def get_mouse_left_click(self):
        result = self.mouse_left_click
        if result:
            self.mouse_left_click = False
            self.mouse_left_clicked = True
        return result