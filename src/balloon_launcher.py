import pygame, math
from bullet import Bullet
from utils import load_image
from turnmanager import TurnManager
from balloon import Balloon
from weapon import Weapon

class BalloonLauncher(Weapon):

    def __init__(self, name, power):
        Weapon.__init__(self, name, power)
        self.balloon = None

    """
    Shoot the ammo from the launcher
    """
    def shoot(self, gravity_direction = None):
        if self.ammo > 0:
            if(self.snail):
                self.balloon = Balloon(self.snail, self.weaponAngle, gravity_direction)
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
        if self.snail:
            x_margin = 0
            y_margin = 0

            x_margin = math.cos(math.radians(self.weaponAngle)) * (self.snail.rect.width * 2)
            y_margin = math.sin(math.radians(self.weaponAngle)) * (self.snail.rect.height * 2)

            self.rect.centerx = self.snail.rect.centerx + x_margin
            self.rect.centery = self.snail.rect.centery + y_margin

            if self.balloon:
                if self.balloon.isAlive == False:
                    self.balloon = None
                    TurnManager().stopTurn()
                else:
                    self.balloon.update(terrain)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        if self.balloon <> None:
            surface.blit(self.balloon.image, self.balloon.rect)