import pygame

class Team(pygame.sprite.Group):
    
    def __init__(self, name, inventory=None):
        pygame.sprite.Group.__init__(self)
        self.name = name        
        self.inventory = inventory
        
    