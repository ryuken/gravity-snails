import pygame
from settings import Settings
from utils import load_image
from math import ceil

class Salt(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_v = load_image('salt.png')
        self.image_h = pygame.transform.rotate(self.image_v, 90)
        
    def draw(self, surface):
        # Draw the salt
        h = int(ceil(Settings.SCREEN_HEIGHT / 315.0))
        w = int(ceil(Settings.SCREEN_WIDTH / 315.0))
        y = 0
        x = 0
        
        for i in range(0, h):
            surface.blit(self.image_v, (0,y))
            surface.blit(self.image_v, ((Settings.SCREEN_WIDTH - 31),y))
            y += 315
        
        for i in range(0, w):
            surface.blit(self.image_h, (x,0))
            surface.blit(self.image_h, (x,(Settings.SCREEN_HEIGHT - 31)))
            x += 315