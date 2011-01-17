import pygame, math
from utils import load_image
from settings import Settings
from turnmanager import TurnManager
from enums import Direction
from gameElements.shootableobject import ShootableObject

class Balloon(ShootableObject):
    def __init__(self, snail, gravity_direction):
        ShootableObject.__init__(self, snail)
        self._exploded = False
        self.image = load_image("balloon.png")
        self.rect = self.image.get_rect()
        self.gravity_direction = gravity_direction

        # Calculate the x and y speed of the bullet
        if(gravity_direction == Direction.UP):
            self.speed[1]= 10
            bullet_margin_y = self.rect.height / 2
            bullet_margin_x = 0
            self.image = pygame.transform.rotate(self.image, 180)
        if(gravity_direction == Direction.DOWN):
            self.speed[1]= -10
            bullet_margin_y = -self.rect.height / 2
            bullet_margin_x = 0
            self.image = pygame.transform.rotate(self.image, 0)
        if(gravity_direction == Direction.LEFT):
            self.speed[0]= 10
            bullet_margin_y = 0
            bullet_margin_x = self.rect.width / 2
            self.image = pygame.transform.rotate(self.image, 180+90)
        if(gravity_direction == Direction.RIGHT):
            self.speed[0]= -10
            bullet_margin_y = 0
            bullet_margin_x = -self.rect.width / 2
            self.image = pygame.transform.rotate(self.image, 90)

        self.rect.centerx = snail.rect.centerx + bullet_margin_x
        self.rect.centery = snail.rect.centery + bullet_margin_y
