import pygame
from enums import TeamStatus
from snail import Snail

class Team(pygame.sprite.Group):

    def __init__(self, name):
        pygame.sprite.Group.__init__(self)
        self.name = name
        self.hasTurn = False
        
    def draw(self, surface):
        pygame.sprite.Group.draw(self, surface)
        for s in self.sprites():
            s.draw(surface)
                        
    def updateEvent(self, event):
        pass