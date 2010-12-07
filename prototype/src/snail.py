import pygame
import sys
from pygame.locals import *

from utils import load_image

class Snail(pygame.sprite.Sprite):
    def __init__(self, terrain):
        pygame.sprite.Sprite.__init__(self)
        self.image_right = load_image('snailRight.png')
        self.image_left = load_image('snailLeft.png')
        self.image_down_left = pygame.transform.rotate(self.image_right, 180)
        self.image_down_right = pygame.transform.rotate(self.image_left, 180)
        self.image = self.image_down_left
        self.rect = self.image.get_rect()
        self.speed = {'movement' : 2, 'jump' : 10, 'fall' : 0.2}
        self.direction = {'movement' : 0.0, 'jump' : 0.0}#Don't touch this!!!
        self.gravity_direction = 'fall_up'
        self.terrain = terrain
    def update(self):
        #E Event
        self.updateMove()
        self.updateGravity()

        self.updateCollisionHorizontal()
        self.updateCollisionVertical()

    def updateMove(self):
        self.direction['movement'] = 0
        if (pygame.key.get_pressed()[K_LEFT]):
            self.direction['movement'] = -self.speed['movement']
            if(self.gravity_direction == 'fall_down'):
                self.image = self.image_left
            else:
                self.image = self.image_down_left
        if (pygame.key.get_pressed()[K_RIGHT]):
            self.direction['movement'] = self.speed['movement']
            if(self.gravity_direction == 'fall_down'):
                self.image = self.image_right
            else:
                self.image = self.image_down_right

    def updateGravity(self):
        self.direction['jump'] += self.speed['fall']
        if self.direction['jump'] > 5:
            self.direction['jump'] = 5

    def updateCollisionVertical(self):
        if(self.gravity_direction == 'fall_down'):
            self.rect = self.rect.move(0, self.direction['jump'])
        if(self.gravity_direction == 'fall_up'):
            self.rect = self.rect.move(0, -self.direction['jump'])
        list = pygame.sprite.spritecollide(self, self.terrain, False)
        if(len(list) > 0):
            if(self.gravity_direction == 'fall_up'):
                self.rect = self.rect.move(0, self.direction['jump'])
            if(self.gravity_direction == 'fall_down'):
                self.rect = self.rect.move(0, -self.direction['jump'])
            self.direction['jump'] = 0
            if (pygame.key.get_pressed()[K_RETURN]):
                self.direction['jump'] = -self.speed['jump']

    def updateCollisionHorizontal(self):
        self.rect = self.rect.move(self.direction['movement'], 0)
        list = pygame.sprite.spritecollide(self, self.terrain, False)
        if(len(list) > 0):
            self.rect = self.rect.move(-self.direction['movement'], 0)