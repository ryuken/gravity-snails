import pygame, math
from utils import load_image
from turnmanager import TurnManager
from weapons.shootableobject import ShootableObject

class Weapon(pygame.sprite.Sprite):
    """
    @ivar name: The name of this weapon
    @ivar power: Amount of hitpoints this weapon will damage
    @ivar ammo: The amount of ammo this weapon has
    @ivar snail: The snail which is the owner of this weapon
    @ivar rect: The rect which should be used to draw the image
    """

    def __init__(self, name, power):
        """
        @param name: The name of this weapon
        @param power: Amount of hitpoints this weapon will damage
        @summary: Initializes a weapon
        """
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.power = power

        self.ammo = 6 * 5
        self.shootableObject = None

        self.image = load_image('crosshair.png')
        self.rect = self.image.get_rect()

        self.snail = None

    def shoot(self):
        """
        @summary: Shoot the ammo from the weapon
        """
        raise ValueError("Weapon.shoot is abstract, please extend to implement shoot method!")

    def update(self, input, terrain):
        """
        @param input: The user input
        @param terrain: The terrain which should be used for collission detection
        @summary: updates the cannon based on user input
        """
        if self.snail:
            if self.shootableObject:
                if self.shootableObject.isAlive == False:
                    self.shootableObject = None
                    TurnManager().stopTurn()
                else:
                    self.shootableObject.update(terrain)

    def draw(self, surface):
        """
        @param surface: The surface on which the weapon should be drawn
        @summary: Draws the shooter and also the shooted object when it has been shot
        """
        surface.blit(self.image, self.rect)

        if self.shootableObject != None:
            self.shootableObject.draw(surface)
