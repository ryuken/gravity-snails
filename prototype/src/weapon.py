import pygame
import sys
from pygame.locals import *
from utils import load_image

class Weapon(pygame.sprite.Sprite):

    def __init__(self):
        self.power = 20
    
    def shoot(self, target):
        target.getHit(self)
    
    def getPower(self):
        return self.power