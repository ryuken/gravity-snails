import pygame, math
from gameElements.bullet import Bullet
from gameElements.weapon import Weapon
from utils import load_image
from turnmanager import TurnManager
from enums import *

class Cannon(Weapon):

    def __init__(self, name, power):
        Weapon.__init__(self, name, power)


        # Set the aiming direction
        self.weaponAngle = 45
        self.ammo = 6 * 5

        self.image = load_image('crosshair.png')
        self.rect = self.image.get_rect()

    def shoot(self, gravity_direction = None):
        if self.ammo > 0:
            if(self.snail):
                self.shootableObject = Bullet(self.snail, self.weaponAngle)
            #self.ammo -= 1, this weapon can be shooted infinitely!
        else:
            raise ValueError("You can't shoot anymore, you don't have any ammo.")

    def update(self, input, terrain):
        if self.snail:
            if self.snail.hasTurn:
                self.updateAngle(input)

            x_margin = 0
            y_margin = 0

            x_margin = math.cos(math.radians(self.weaponAngle)) * (self.snail.rect.width * 2)
            y_margin = math.sin(math.radians(self.weaponAngle)) * (self.snail.rect.height * 2)

            self.rect.centerx = self.snail.rect.centerx + x_margin
            self.rect.centery = self.snail.rect.centery + y_margin
        Weapon.update(self, input, terrain)

    def updateAngle(self, input):

        gravity_direction = None
        if self.snail:
            gravity_direction = self.snail.gravity_direction

        left_pressed = input.keyboard_left
        right_pressed = input.keyboard_right
        up_pressed = input.keyboard_up
        down_pressed = input.keyboard_down

        if(gravity_direction == Direction.LEFT or gravity_direction == Direction.RIGHT):
            # switch the left/right arrowkey with up/down
            temp_left, temp_right = left_pressed, right_pressed
            left_pressed, right_pressed = up_pressed, down_pressed
            up_pressed, down_pressed = temp_left, temp_right
        if (up_pressed):
            self.weaponAngle += -1
        if (down_pressed):
            self.weaponAngle += 1


    def draw(self, surface):
        surface.blit(self.image, self.rect)

        if self.shootableObject <> None:
            surface.blit(self.shootableObject.image, self.shootableObject.rect)