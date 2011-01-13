import pygame, math
from bullet import Bullet
from utils import load_image
from turnmanager import TurnManager

class Weapon(pygame.sprite.Sprite):

    def __init__(self, name, power):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.power = power

        # Set the aiming direction
        self.weaponAngle = 45

        self.ammo = 6 * 5
        self.bullet = None

        self.image = load_image('crosshair.png')
        self.rect = self.image.get_rect()

        # this rect got the rect of
        self.snail_rect = None

    def shoot(self, gravity_direction = None):
        if self.ammo > 0:
            if(self.snail_rect):
                self.bullet = Bullet(self.snail_rect, self.weaponAngle)
            self.ammo -= 1
        else:
            raise ValueError("You can't shoot anymore, you don't have any ammo.")

    def adjustAngle(self, direction):
        if direction == 0:
            self.weaponAngle += 1
            if self.weaponAngle > 360:
                self.weaponAngle = self.weaponAngle - 360
        elif direction == 1:
            self.weaponAngle -= 1
            if self.weaponAngle < 0:
                self.weaponAngle = 360 + self.weaponAngle

    def update(self, input, terrain):
        if self.snail_rect:
            x_margin = 0
            y_margin = 0

            x_margin = math.cos(math.radians(self.weaponAngle)) * (self.snail_rect.width * 2)
            y_margin = math.sin(math.radians(self.weaponAngle)) * (self.snail_rect.height * 2)

            self.rect.centerx = self.snail_rect.centerx + x_margin
            self.rect.centery = self.snail_rect.centery + y_margin

            if self.bullet:
                if self.bullet.isAlive == False:
                    self.bullet = None
                    TurnManager().stopTurn()
                else:
                    self.bullet.update(terrain)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        if self.bullet <> None:
            surface.blit(self.bullet.image, self.bullet.rect)