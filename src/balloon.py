import pygame, math
from utils import load_image
from settings import Settings
from turnmanager import TurnManager
from enums import Direction

class Balloon(pygame.sprite.Sprite):
    def __init__(self, snail, angle, gravity_direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("balloon.png")
        self.rect = self.image.get_rect()
        self.gravity_direction = gravity_direction

        # Calculate the x and y speed of the bullet
        self.speed = [0,0]
        #self.speed[0] = math.cos(math.radians(angle)) * 10.0 #(self.rect.width)
        #self.speed[1] = math.sin(math.radians(angle)) * 10.0 #(self.rect.height)
        if(gravity_direction == Direction.UP):
            self.speed[1]= 10
        if(gravity_direction == Direction.DOWN):
            self.speed[1]= -10
        if(gravity_direction == Direction.LEFT):
            self.speed[0]= 10
        if(gravity_direction == Direction.RIGHT):
            self.speed[0]= -10

        # Calculate the start position of the bullet
        #bullet_margin_x = math.cos(math.radians(angle)) * (snail.rect.width * 3)
        #bullet_margin_y = math.sin(math.radians(angle)) * (snail.rect.height * 3)
        position = [0,0]
        position[0] = snail.rect.centerx
        position[1] = snail.rect.centery
        #position[0] += bullet_margin_x
        #position[1] += bullet_margin_y

        self.rect.center = position

        self.isAlive = True
        self.isProtected = True
    def update(self, terrain):
        if self.isAlive:
            self.rect.centerx += self.speed[0]
            self.rect.centery += self.speed[1]
            if (self.rect.x < 0 or self.rect.x > Settings.SCREEN_WIDTH):
                self.bounceOutScreen()
                self.isAlive = False
            if (self.rect.y < 0 or self.rect.y > Settings.SCREEN_HEIGHT):
                self.bounceOutScreen()
                self.isAlive = False

            # terrain collision
            list = pygame.sprite.spritecollide(self, terrain, True)
            if(len(list) > 0):
                self.bounceOutScreen()
                self.isAlive = False

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
                            for t in teams:
                                if t.hasTurn:
                                    sprite.hitpoints -= t.active_weapon.power

                    self.bounceOutScreen()
                    self.isAlive = False

    def bounceOutScreen(self):
        # bullet's need to go out of screen because
        # otherwise it will be in screen again
        self.rect.x = Settings.SCREEN_WIDTH + 1000
        self.rect.y = Settings.SCREEN_HEIGHT + 1000