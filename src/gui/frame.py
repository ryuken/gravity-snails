import pygame
from pygame.locals import *
from settings import Settings
class Frame(object):
    def __init__(self):
        self.widgets = []
        # should always be "fullscreen" otherwise, input acts weird
        self.rect = Rect(0, 0, Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
        
    def addWidget(self, widget):
        self.widgets.append(widget)
        
    def update(self, input):
        for widget in self.widgets:
            widget.update(input)
            
    def draw(self, surface):
        frameSurface = pygame.Surface((self.rect.width,self.rect.height))
        frameSurface.fill((0,255,0))
        for widget in self.widgets:
            widget.draw(frameSurface)
        surface.blit(frameSurface, self.rect)