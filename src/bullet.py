import pygame
from utils import load_image
from settings import Settings

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = speed
        self.alive = True

    def update(self, terrain):
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]
        if self.rect.x < 0 or self.rect.x > Settings.SCREEN_WIDTH:
            self.alive = False
        if self.rect.y < 0 or self.rect.y > Settings.SCREEN_HEIGHT:
            self.alive = False
        list = pygame.sprite.spritecollide(self, terrain, True)
        if(len(list) > 0):
            #list[0].kill()
            self.alive = False
            #self.kill()
            #self = None