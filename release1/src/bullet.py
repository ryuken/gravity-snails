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

    def update(self):
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]
        if self.rect.x < 0 or self.rect.x > Settings.SCREEN_WIDTH:
            self.kill()
        if self.rect.y < 0 or self.rect.y > Settings.SCREEN_HEIGHT:
            self.kill()