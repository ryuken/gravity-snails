import pygame
import sys
from pygame.locals import *

from utils import load_image

class Snail(pygame.sprite.Sprite):
    def __init__(self, terrain):
        pygame.sprite.Sprite.__init__(self)
        self.image_right = load_image('snailRight.png')
        self.image_left = load_image('snailLeft.png')
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.speed = {'x' : 2, 'y' : 5}
        self.direction = {'x' : 0.0, 'y' : 0.0}#Don't touch this!!!
        self.terrain = terrain
    def update(self):
        #E Event
        self.updateMove()
        self.updateGravity()

        self.rect = self.rect.move(self.direction['x'], self.direction['y'])

        self.updateCollision()

    def updateMove(self):
        self.direction['x'] = 0
        if (pygame.key.get_pressed()[K_LEFT]):
            self.direction['x'] = -self.speed['x']
            self.image = self.image_left
        if (pygame.key.get_pressed()[K_RIGHT]):
            self.direction['x'] = self.speed['x']
            self.image = self.image_right

    def updateGravity(self):
        self.direction['y'] += 0.2
        if self.direction['y'] > 5:
            self.direction['y'] = 5

    def updateCollision(self):
        list = pygame.sprite.spritecollide(self, self.terrain, False)
        if(len(list) > 0):
            self.rect = self.rect.move(-self.direction['x'], -self.direction['y'])
            self.direction['y'] = 0
            if (pygame.key.get_pressed()[K_RETURN]):
                self.direction['y'] = -self.speed['y']