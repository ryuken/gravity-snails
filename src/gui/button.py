import pygame
from pygame.locals import *
from input import Input
class Button(object):

    def __init__(self, text, callback, *args):
        self.font_size = 25
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = pygame.Rect(0,0,1,1)
        self.text = text
        self.callback = callback
        self.pressed = False
        self.args = None
        argSize = len(args)
        if(0 < argSize):
            self.args = args

    def update(self, input):
        if input.get_mouse_left_click(self.rect):
            self.pressed = True
        if self.pressed:
            if not input.mouse_left:
                self.pressed = False
                if(not None == self.args):
                    self.callback(self.args)
                else:
                    self.callback()

    def draw(self, surface):
        # Draw the red rectangle on the game surface
        if self.pressed:
            self.rect = surface.fill((128,0,0), self.rect)
        else:
            self.rect = surface.fill((255,0,0), self.rect)
        surface.blit(surface, (0,0))
        # Create a new surface at the position of the red rectangle and draw the text
        text = self.font.render(str(self.text), 1, (10, 10, 10)) #returns surface
        surface.blit(text, (self.rect.centerx - (text.get_width() / 2), self.rect.centery - (text.get_height() / 2)))
