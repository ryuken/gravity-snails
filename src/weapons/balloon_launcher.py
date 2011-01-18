import pygame, math
from utils import load_image
from turnmanager import TurnManager
from weapons.balloon import Balloon
from weapons.weapon import Weapon

class BalloonLauncher(Weapon):

    def __init__(self, name, power):
        """
        @param name: The name of this weapon
        @param power: Amount of hitpoints this weapon will damage
        @summary: Initializes a balloon launcher
        """
        Weapon.__init__(self, name, power)

    def shoot(self, gravity_direction = None):
        """
        @param gravity_direction: The gravity direction which should be used to create a balloon
        @summary: Shoot the ammo from the launcher
        """
        if self.ammo > 0:
            if(self.snail):
                self.shootableObject = Balloon(self.snail, gravity_direction)
            #self.ammo -= 1, this weapon can be shooted infinitely!
        else:
            raise ValueError("You can't shoot anymore, you don't have any ammo.")
