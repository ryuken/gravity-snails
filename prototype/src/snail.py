import pygame
import sys
from pygame.locals import *

from utils import load_image

class Snail(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('snail.png')
        self.rect = self.image.get_rect()
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
    def update(self):
        #E Event
        if (pygame.key.get_pressed()[K_LEFT]):
            self.rect = self.rect.move(-1,0)
        if (pygame.key.get_pressed()[K_RIGHT]):
            self.rect = self.rect.move(1,0)
