import pygame

from utils import load_image

class Snail(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('sprites/snail.png')
        self.rect = self.image.get_rect()