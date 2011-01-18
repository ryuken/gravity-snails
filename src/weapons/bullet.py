import pygame, math
from utils import load_image
from settings import Settings
from turnmanager import TurnManager
from weapons.shootableobject import ShootableObject

class Bullet(ShootableObject):
    """
    @ivar image: The image that represents the bullet
    @ivar gravity_direction: The gravity direction which should be used for this balloon
    @ivar angle: The angle which is used to calculate speed in x and y directions
    @ivar rect: The rect which should be used to draw the image
    """

    def __init__(self, snail, angle):
        """
        @param snail: The snail which has shooted this balloon
        @param angle: The angle which is used to calculate speed in x and y directions
        @summary: Initializes a bullet
        """
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
