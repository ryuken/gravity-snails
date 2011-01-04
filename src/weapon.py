import pygame, math
from bullet import Bullet
from utils import load_image

class Weapon(pygame.sprite.Sprite):

    def __init__(self, name, power):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.power = power
        
        # Set the aiming direction
        self.weaponAngle = 45
        
        self.ammo = 5
        self.bullet = None
        
        self.image = load_image('crosshair.png')
        self.rect = self.image.get_rect()
    
#    def update(self, teams):
#        if self.bullet <> None:
#            self.bullet.update(teams)
    
    def shoot(self, snail_rect):
        if self.ammo > 0:
            self.bullet = Bullet(snail_rect, self.weaponAngle)
            self.ammo -= 1
            print "created bullet"
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
                
    def draw(self, surface, snail_rect, bool):        
        if bool:
            x_margin = 0
            y_margin = 0
            #if(self.gravity_direction == Direction.DOWN or self.gravity_direction == Direction.UP):
            x_margin = math.cos(math.radians(self.weaponAngle)) * (snail_rect.width * 2)
            #if(self.gravity_direction == Direction.LEFT or self.gravity_direction == Direction.RIGHT):
            y_margin = math.sin(math.radians(self.weaponAngle)) * (snail_rect.height * 2)
            #if(self.image == self.im)
            self.rect.centerx = snail_rect.centerx + x_margin
            self.rect.centery = snail_rect.centery + y_margin
            #self.weapon.rect.move_ip(self.rect.centerx, self.rect.centery)
            surface.blit(self.image, self.rect)
    
        if self.bullet <> None:
            surface.blit(self.bullet.image, self.bullet.rect)