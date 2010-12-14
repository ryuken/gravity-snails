import pygame
import sys
import math
from pygame.locals import *
from utils import load_image
from weapon import Weapon
from enums import Direction
from bullet import Bullet

class Snail(pygame.sprite.Sprite):

    def __init__(self, game):
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
        self.gravity_direction = Direction.LEFT
        if self.gravity_direction == Direction.DOWN:
            self.image = self.image_down_right
        if self.gravity_direction == Direction.UP:
            self.image = self.image_up_right
        if self.gravity_direction == Direction.LEFT:
            self.image = self.image_left_up
        if self.gravity_direction == Direction.RIGHT:
            self.image = self.image_right_up
        self.rect = self.image.get_rect()
        self.game = game

        self.hitpoints = 100
        self.isPlaced = False
        self.weapon = Weapon("laser", 100)
        self.weaponAngle = 45
        self.has_shooted = False

    def update(self):
        #E Event
        if(not self.isPlaced):
            prev_x = self.rect.centerx
            prev_y = self.rect.centery
            self.rect.centerx = pygame.mouse.get_pos()[0]
            self.rect.centery = pygame.mouse.get_pos()[1]
            list = pygame.sprite.spritecollide(self, self.game.terrain, False)
            if(len(list) > 0):
                self.rect.centerx = prev_x
                self.rect.centery = prev_y
            else:
                if pygame.mouse.get_pressed()[0]:
                    self.isPlaced = True

        if self.isPlaced:
            self.updateMove()
            self.updateGravity()

        self.updateImage()
        self.updateCollisionHorizontal()
        self.updateCollisionVertical()
    def updateImage(self):
        left_pressed = self.direction['movement'] == -self.speed['movement']
        right_pressed = self.direction['movement'] == self.speed['movement']
        if (left_pressed):
            self.direction['movement'] = -self.speed['movement']
            if(self.gravity_direction == Direction.DOWN):
                self.image = self.image_down_left
            elif(self.gravity_direction == Direction.UP):
                self.image = self.image_up_left
            elif(self.gravity_direction == Direction.LEFT):
                self.image = self.image_left_up
            elif(self.gravity_direction == Direction.RIGHT):
                self.image = self.image_right_up
        if (right_pressed):
            self.direction['movement'] = self.speed['movement']
            if(self.gravity_direction == Direction.DOWN):
                self.image = self.image_down_right
            elif(self.gravity_direction == Direction.UP):
                self.image = self.image_up_right
            elif(self.gravity_direction == Direction.LEFT):
                self.image = self.image_left_down
            elif(self.gravity_direction == Direction.RIGHT):
                self.image = self.image_right_down

    def updateMove(self):
        self.direction['movement'] = 0
        left_pressed = pygame.key.get_pressed()[K_LEFT]
        right_pressed = pygame.key.get_pressed()[K_RIGHT]
        up_pressed = pygame.key.get_pressed()[K_UP]
        down_pressed = pygame.key.get_pressed()[K_DOWN]
        space_pressed = pygame.key.get_pressed()[K_SPACE]
        if(self.gravity_direction == Direction.LEFT or self.gravity_direction == Direction.RIGHT):
            temp_left, temp_right = left_pressed, right_pressed
            left_pressed, right_pressed = up_pressed, down_pressed
            up_pressed, down_pressed = temp_left, temp_right
        if (left_pressed):
            self.direction['movement'] = -self.speed['movement']
        if (right_pressed):
            self.direction['movement'] = self.speed['movement']
        if (up_pressed):
            self.weaponAngle += 1
            if self.weaponAngle > 360:
                self.weaponAngle = self.weaponAngle - 360
        if (down_pressed):
            self.weaponAngle -= 1
            if self.weaponAngle < 0:
                self.weaponAngle = 360 + self.weaponAngle
        if (space_pressed and not self.has_shooted):
            self.has_shooted = True
            bullet_speed_x = math.cos(math.radians(self.weaponAngle)) * 10.0 #(self.rect.width)
            bullet_speed_y = math.sin(math.radians(self.weaponAngle)) * 10.0 #(self.rect.height)
            bullet_margin_x = math.cos(math.radians(self.weaponAngle)) * (self.rect.width)
            bullet_margin_y = math.sin(math.radians(self.weaponAngle)) * (self.rect.height)
            bullet_position = [0,0]
            bullet_position[0] = self.rect.centerx
            bullet_position[1] = self.rect.centery
            bullet_position[0] += bullet_margin_x
            bullet_position[1] += bullet_margin_y
            self.game.addBullet(Bullet(self.game, bullet_position, [bullet_speed_x, bullet_speed_y]))
        self.updateImage()

    def updateGravity(self):
        self.direction['jump'] += self.speed['fall']
        if self.direction['jump'] > 5:
            self.direction['jump'] = 5

    def updateCollisionVertical(self):
        if(self.gravity_direction == Direction.DOWN):
            self.rect = self.rect.move(0, self.direction['jump'])
        if(self.gravity_direction == Direction.UP):
            self.rect = self.rect.move(0, -self.direction['jump'])
        if(self.gravity_direction == Direction.LEFT):
            self.rect = self.rect.move(-self.direction['jump'], 0)
        if(self.gravity_direction == Direction.RIGHT):
            self.rect = self.rect.move(self.direction['jump'], 0)
        list = pygame.sprite.spritecollide(self, self.game.terrain, False)
        if(len(list) > 0):
            if(self.gravity_direction == Direction.DOWN):
                self.rect = self.rect.move(0, -self.direction['jump'])
            if(self.gravity_direction == Direction.UP):
                self.rect = self.rect.move(0, self.direction['jump'])
            if(self.gravity_direction == Direction.LEFT):
                self.rect = self.rect.move(self.direction['jump'], 0)
            if(self.gravity_direction == Direction.RIGHT):
                self.rect = self.rect.move(-self.direction['jump'], 0)
            self.direction['jump'] = 0
            if (pygame.key.get_pressed()[K_RETURN]):
                self.direction['jump'] = -self.speed['jump']

    def updateCollisionHorizontal(self):
        if(self.gravity_direction == Direction.DOWN or self.gravity_direction == Direction.UP):
            self.rect = self.rect.move(self.direction['movement'], 0)
        else:
            self.rect = self.rect.move(0, self.direction['movement'])
        list = pygame.sprite.spritecollide(self, self.game.terrain, False)
        if(len(list) > 0):
            if(self.gravity_direction == Direction.DOWN or self.gravity_direction == Direction.UP):
                self.rect = self.rect.move(-self.direction['movement'], 0)
            else:
                self.rect = self.rect.move(0, -self.direction['movement'])

    def draw(self, surface):
        x_margin = 0
        y_margin = 0
        #if(self.gravity_direction == Direction.DOWN or self.gravity_direction == Direction.UP):
        x_margin = math.cos(math.radians(self.weaponAngle)) * (self.rect.width * 2)
        #if(self.gravity_direction == Direction.LEFT or self.gravity_direction == Direction.RIGHT):
        y_margin = math.sin(math.radians(self.weaponAngle)) * (self.rect.height * 2)
        #if(self.image == self.im)
        self.weapon.rect.centerx = self.rect.centerx + x_margin
        self.weapon.rect.centery = self.rect.centery + y_margin
        #self.weapon.rect.move_ip(self.rect.centerx, self.rect.centery)
        surface.blit(self.weapon.image, self.weapon.rect)
