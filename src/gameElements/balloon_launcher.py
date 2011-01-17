import pygame, math
from utils import load_image
from turnmanager import TurnManager
from gameElements.balloon import Balloon
from gameElements.weapon import Weapon

class BalloonLauncher(Weapon):

    def __init__(self, name, power):
        Weapon.__init__(self, name, power)

    """
    Shoot the ammo from the launcher
    """
    def shoot(self, gravity_direction = None):
        if self.ammo > 0:
            if(self.snail):
                self.shootableObject = Balloon(self.snail, gravity_direction)
            #self.ammo -= 1, this weapon can be shooted infinitely!
        else:
            raise ValueError("You can't shoot anymore, you don't have any ammo.")

    def draw(self, surface):
        #surface.blit(self.image, self.rect)

        if self.shootableObject <> None:
            surface.blit(self.shootableObject.image, self.shootableObject.rect)