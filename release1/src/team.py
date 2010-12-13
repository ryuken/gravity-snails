import pygame
from enums import TeamStatus
from snail import Snail

class Team(pygame.sprite.Group):

    def __init__(self, name, inventory=None):
        pygame.sprite.Group.__init__(self)
        self.name = name
        self.inventory = inventory
        self.status = TeamStatus.PLACESNAIL
        
    def draw(self, surface):
        pygame.sprite.Group.draw(self, surface)
        for s in self.sprites():
            s.draw(surface)
                        
    def updateEvent(self, event):
        #if self.status == TeamStatus.PLACESNAIL:
        self.status = TeamStatus.PLAY
        #elif self.status == TeamStatus.PLAY
            