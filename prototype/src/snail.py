import pygame
import sys
from pygame.locals import *

from utils import load_image

class Snail(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_right = load_image('snailRight.png')
        self.image_left = load_image('snailLeft.png')
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.movingLeft = False
    def update(self):
        #E Event
        if (pygame.key.get_pressed()[K_LEFT]):
            self.rect = self.rect.move(-1,0)
            self.image = self.image_left
        if (pygame.key.get_pressed()[K_RIGHT]):
            self.rect = self.rect.move(1,0)
            self.image = self.image_right
