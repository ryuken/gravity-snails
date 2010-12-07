import pygame
import sys
from pygame.locals import *
from utils import load_image

class Weapon(pygame.sprite.Sprite):

    def __init__(self):
        self.power = 20
    
    def shoot(self, target):
        target.getHit(self)

class Bazooka(Weapon):
    
    def __init__(self):
        Weapon.__init__(self)
        self.image = load_image('bazooka_icon.png')
        self.rect = self.image.get_rect()
        
    