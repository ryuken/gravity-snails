import pygame
import sys
from pygame.locals import *
from utils import load_image

class Snail(pygame.sprite.Sprite):

    def __init__(self, terrain):
        pygame.sprite.Sprite.__init__(self)
        self.image_down_right = load_image('snailRight.png')
        self.image_down_left = load_image('snailLeft.png')
        self.image_up_left = pygame.transform.rotate(self.image_down_right, 180)
        self.image_up_right = pygame.transform.rotate(self.image_down_left, 180)
        self.image_left_up = pygame.transform.rotate(self.image_down_left, 270)
        self.image_left_down = pygame.transform.rotate(self.image_down_right, 270)
        self.image_right_up = pygame.transform.rotate(self.image_down_right, 90)
        self.image_right_down = pygame.transform.rotate(self.image_down_left, 90)
        self.speed = {'movement' : 2, 'jump' : 10, 'fall' : 0.2}
        self.direction = {'movement' : 0.0, 'jump' : 0.0}#Don't touch this!!!
        self.FALL_UP = 0
        self.FALL_DOWN = 1
        self.FALL_LEFT = 2
        self.FALL_RIGHT = 3
        self.gravity_direction = self.FALL_RIGHT
        if self.gravity_direction == self.FALL_DOWN:
            self.image = self.image_down_right
        if self.gravity_direction == self.FALL_UP:
            self.image = self.image_up_right
        if self.gravity_direction == self.FALL_LEFT:
            self.image = self.image_right_up
        if self.gravity_direction == self.FALL_RIGHT:
            self.image = self.image_right_up
        self.rect = self.image.get_rect()  
        self.terrain = terrain
        
        self.hitpoints = 100

    def update(self):
        #E Event
        self.updateMove()
        self.updateGravity()

        self.updateCollisionHorizontal()
        self.updateCollisionVertical()

    def updateMove(self):
        self.direction['movement'] = 0
        left_pressed = pygame.key.get_pressed()[K_LEFT]
        right_pressed = pygame.key.get_pressed()[K_RIGHT]
        up_pressed = pygame.key.get_pressed()[K_UP]
        down_pressed = pygame.key.get_pressed()[K_DOWN]
        if(self.gravity_direction == self.FALL_RIGHT or self.gravity_direction == self.FALL_LEFT):
            left_pressed, right_pressed = up_pressed, down_pressed
        if (left_pressed):
            self.direction['movement'] = -self.speed['movement']
            if(self.gravity_direction == self.FALL_DOWN):
                self.image = self.image_down_left
            elif(self.gravity_direction == self.FALL_UP):
                self.image = self.image_up_left
            elif(self.gravity_direction == self.FALL_LEFT):
                self.image = self.image_left_up
            elif(self.gravity_direction == self.FALL_RIGHT):
                self.image = self.image_right_up
        if (right_pressed):
            self.direction['movement'] = self.speed['movement']
            if(self.gravity_direction == self.FALL_DOWN):
                self.image = self.image_down_right
            elif(self.gravity_direction == self.FALL_UP):
                self.image = self.image_up_right
            elif(self.gravity_direction == self.FALL_LEFT):
                self.image = self.image_left_down
            elif(self.gravity_direction == self.FALL_RIGHT):
                self.image = self.image_right_down
                
    def updateGravity(self):
        self.direction['jump'] += self.speed['fall']
        if self.direction['jump'] > 5:
            self.direction['jump'] = 5

    def updateCollisionVertical(self):
        if(self.gravity_direction == self.FALL_DOWN):
            self.rect = self.rect.move(0, self.direction['jump'])
        if(self.gravity_direction == self.FALL_UP):
            self.rect = self.rect.move(0, -self.direction['jump'])
        if(self.gravity_direction == self.FALL_LEFT):
            self.rect = self.rect.move(-self.direction['jump'], 0)
        if(self.gravity_direction == self.FALL_RIGHT):
            self.rect = self.rect.move(self.direction['jump'], 0)
        list = pygame.sprite.spritecollide(self, self.terrain, False)
        if(len(list) > 0):
            if(self.gravity_direction == self.FALL_UP):
                self.rect = self.rect.move(0, self.direction['jump'])
            if(self.gravity_direction == self.FALL_DOWN):
                self.rect = self.rect.move(0, -self.direction['jump'])
            if(self.gravity_direction == self.FALL_LEFT):
                self.rect = self.rect.move(self.direction['jump'], 0)
            if(self.gravity_direction == self.FALL_RIGHT):
                self.rect = self.rect.move(-self.direction['jump'], 0)
            self.direction['jump'] = 0
            if (pygame.key.get_pressed()[K_RETURN]):
                self.direction['jump'] = -self.speed['jump']

    def updateCollisionHorizontal(self):
        if(self.gravity_direction == self.FALL_DOWN or self.gravity_direction == self.FALL_UP):
            self.rect = self.rect.move(self.direction['movement'], 0)
        else:
            self.rect = self.rect.move(0, self.direction['movement'])
        list = pygame.sprite.spritecollide(self, self.terrain, False)
        if(len(list) > 0):
            if(self.gravity_direction == self.FALL_DOWN or self.gravity_direction == self.FALL_UP):
                self.rect = self.rect.move(-self.direction['movement'], 0)
            else:
                self.rect = self.rect.move(0, -self.direction['movement'])