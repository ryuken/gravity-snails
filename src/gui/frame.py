import pygame
from pygame.locals import *
from settings import Settings
class Frame(object):
    def __init__(self):
        self.widgets = []
        # should always be "fullscreen" otherwise, input acts weird
        self.rect = Rect(32, 32, Settings.SCREEN_WIDTH - 64, Settings.SCREEN_HEIGHT - 64)
        
    def addWidget(self, widget):
        self.widgets.append(widget)
        
    def update(self, input):
        localInput = input.copy();
        localInput.mouse_x -= self.rect.left
        localInput.mouse_y -= self.rect.top
        for widget in self.widgets:
            widget.update(localInput)
            
    def draw(self, surface):
        frameSurface = pygame.Surface((self.rect.width,self.rect.height))
        frameSurface.fill((0,0,128))
        for widget in self.widgets:
            widget.draw(frameSurface)
        surface.blit(frameSurface, self.rect)