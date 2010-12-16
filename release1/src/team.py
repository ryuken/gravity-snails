import pygame
from enums import *
from snail import Snail

class Team(pygame.sprite.Group):

    def __init__(self, name, gravity_direction):
        pygame.sprite.Group.__init__(self)
        self.name = name
        self.hasTurn = False
        self.gravity_direction = gravity_direction
        
    def draw(self, surface):
        pygame.sprite.Group.draw(self, surface)
        for s in self.sprites():
            s.draw(surface)
                        
    def updateEvent(self, event):
        pass
    
    def setGravity(self, direction):
        self.gravity_direction = direction
        for s in self.sprites():
            s.gravity_direction = direction