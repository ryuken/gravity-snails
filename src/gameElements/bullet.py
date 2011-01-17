import pygame, math
from utils import load_image
from settings import Settings
from turnmanager import TurnManager
from gameElements.shootableobject import ShootableObject

class Bullet(ShootableObject):
    def __init__(self, snail, angle):
        ShootableObject.__init__(self, snail)

        self.image = load_image("bullet.png")
        self.rect = self.image.get_rect()
        self.angle = angle

        # Calculate the x and y speed of the bullet
        self.speed[0] = math.cos(math.radians(angle)) * 10.0 #(self.rect.width)
        self.speed[1] = math.sin(math.radians(angle)) * 10.0 #(self.rect.height)

        position = [0,0]
        position[0] = snail.rect.centerx
        position[1] = snail.rect.centery

        self.rect.center = position
