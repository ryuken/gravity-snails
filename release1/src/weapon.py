import pygame
import sys
from pygame.locals import *
from utils import load_image

class Weapon(pygame.sprite.Sprite):

    def __init__(self, name, power):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.power = power
        self.image = load_image('crosshair.png')
        self.rect = self.image.get_rect()

