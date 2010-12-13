import pygame

class Team(pygame.sprite.Group):

    def __init__(self, name, inventory=None):
        pygame.sprite.Group.__init__(self)
        self.name = name
        self.inventory = inventory
    def draw(self, surface):
        pygame.sprite.Group.draw(self, surface)
        for s in self.sprites():
            s.draw(surface)            
        
    