import pygame, math
from utils import load_image
from turnmanager import TurnManager
from weapons.shootableobject import ShootableObject

class Weapon(pygame.sprite.Sprite):

    def __init__(self, name, power):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.power = power

        self.ammo = 6 * 5
        self.shootableObject = None

        self.image = load_image('crosshair.png')
        self.rect = self.image.get_rect()

        # this rect got the rect of
        self.snail = None

    def shoot(self, gravity_direction = None):
        raise ValueError("Weapon.shoot is abstract, please extend to implement shoot method!")

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
            if self.shootableObject:
                if self.shootableObject.isAlive == False:
                    self.shootableObject = None
                    TurnManager().stopTurn()
                else:
                    self.shootableObject.update(terrain)

    """
    Draws the shooter and also the shooted object when it has been shot
    """
    def draw(self, surface):
        surface.blit(self.image, self.rect)

        if self.shootableObject <> None:
            self.shootableObject.draw(surface)