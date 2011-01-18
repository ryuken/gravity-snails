import pygame, math
from utils import load_image
from settings import Settings
from utils import load_sound
from turnmanager import TurnManager

class ShootableObject(pygame.sprite.Sprite):
    """
    @ivar image: The image that represents this object
    """

    def __init__(self, snail):
        """
        @param snail: The snail which has shooted this object. This will also be used to calculate the position of this object
        @summary: Initializes a shootable object
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bullet.png")
        self.rect = self.image.get_rect()

        # Calculate the x and y speed of the bullet
        self.speed = [0,0]

        self.snail = snail
        position = [0,0]
        position[0] = snail.rect.centerx
        position[1] = snail.rect.centery

        self.rect.center = position
        self.isAlive = True
        self.isProtected = True
        self.explosionSound = load_sound("cannon.ogg")
        #self.explosionSound.play()

    def update(self, terrain):
        """
        @param terrain: The terrain which should be used for collission detection
        @summary: updates this object
        """
        if self.isAlive:
            self.rect.centerx += self.speed[0]
            self.rect.centery += self.speed[1]
            if (self.rect.x < 0 or self.rect.x > Settings.SCREEN_WIDTH):
                self.bounceOutScreen()
                self.isAlive = False
            if (self.rect.y < 0 or self.rect.y > Settings.SCREEN_HEIGHT):
                self.bounceOutScreen()
                self.isAlive = False
            if self.isProtected:
                list = pygame.sprite.spritecollide(self, self.snail.team, False)
                if len(list) <> 1:
                    self.isProtected = False
            else:
                # snail collision
                teams = TurnManager().teams
                for team in teams:
                    list = pygame.sprite.spritecollide(self, team, False)
                    if(len(list) > 0):
                        # iterate thru the sprite's which collided with the bullet
                        for sprite in list:
                            # when the sprite is not self ( a bullet), it's a snail
                            if sprite <> self:
                                # decrease the hitpoint's of the snail with the power of weapon which shot
                                sprite.hitpoints -= TurnManager().currentTeam.active_weapon.power

                        self.bounceOutScreen()
                        self.isAlive = False
            # terrain collision
            list = pygame.sprite.spritecollide(self, terrain, True)
            if(len(list) > 0):
                self.bounceOutScreen()
                self.isAlive = False

    def bounceOutScreen(self):
        """
        @summary: a very ugly method to remove a shootable object from the screen!
        """
        self.explosionSound.play()
        # bullet's need to go out of screen because
        # otherwise it will be in screen again
        self.rect.x = Settings.SCREEN_WIDTH + 1000
        self.rect.y = Settings.SCREEN_HEIGHT + 1000

    def draw(self, surface):
        """
        @param surface: The surface which the shootable object should be drawed on
        @summary: draws the shootable object on a specified surface
        """
        surface.blit(self.image, self.rect)