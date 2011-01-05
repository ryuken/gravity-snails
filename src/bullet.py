import pygame, math
from utils import load_image
from settings import Settings

class Bullet(pygame.sprite.Sprite):
    def __init__(self, snail_rect, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bullet.png")
        self.rect = self.image.get_rect()
        
        # Calculate the x and y speed of the bullet
        self.speed = [0,0]
        self.speed[0] = math.cos(math.radians(angle)) * 10.0 #(self.rect.width)
        self.speed[1] = math.sin(math.radians(angle)) * 10.0 #(self.rect.height)
        
        # Calculate the start position of the bullet
        bullet_margin_x = math.cos(math.radians(angle)) * (snail_rect.width)
        bullet_margin_y = math.sin(math.radians(angle)) * (snail_rect.height)
        position = [0,0]
        position[0] = snail_rect.centerx
        position[1] = snail_rect.centery
        position[0] += bullet_margin_x
        position[1] += bullet_margin_y
        
        self.rect.center = position
        
        self.alive = True

    def update(self, terrain):
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]
        if (self.rect.x < 0 or self.rect.x > Settings.SCREEN_WIDTH
            or self.rect.y < 0 or self.rect.y > Settings.SCREEN_HEIGHT):
            self.alive = False
            #TurnManager().changeTurn()
        list = pygame.sprite.spritecollide(self, terrain, True)
        if(len(list) > 0):
            self.kill()
            self.alive = False