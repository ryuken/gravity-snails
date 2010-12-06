import pygame
class Team(pygame.sprite.Group):
    def __init__(self, name):
        pygame.sprite.Group.__init__(self)
        self.name = name