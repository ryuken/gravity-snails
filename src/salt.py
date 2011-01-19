import pygame
from settings import Settings
from utils import load_image
from math import ceil

class Salt(pygame.sprite.Group):

    def __init__(self):
        pygame.sprite.Group.__init__(self)

        h = int(ceil(Settings.SCREEN_HEIGHT / 315.0))
        w = int(ceil(Settings.SCREEN_WIDTH / 315.0))
        y = 0
        x = 0
            
        for i in range(0, h):
            self.saltSprite = pygame.sprite.Sprite()
            self.saltSprite.image = load_image('salt.png')
            self.saltSprite.rect = self.saltSprite.image.get_rect()
            self.saltSprite.rect.move_ip(0, y)
            
            self.add(self.saltSprite)
            
            self.saltSprite = pygame.sprite.Sprite()
            self.saltSprite.image = load_image('salt.png')
            self.saltSprite.rect = self.saltSprite.image.get_rect()
            self.saltSprite.rect.move_ip((Settings.SCREEN_WIDTH - 31),y)
            self.add(self.saltSprite)
            #surface.blit(self.saltSprite.image, (0,y))
            #surface.blit(self.saltSprite.image, ((Settings.SCREEN_WIDTH - 31),y))
            y += 315
        
        for i in range(0, w):
            self.saltSprite = pygame.sprite.Sprite()
            self.saltSprite.image = load_image('salt.png')
            self.saltSprite.image = pygame.transform.rotate(self.saltSprite.image, 90)
            self.saltSprite.rect =  self.saltSprite.image.get_rect()
            
            self.saltSprite.rect.move_ip(x,0)
            self.add(self.saltSprite)
            
            self.saltSprite = pygame.sprite.Sprite()
            self.saltSprite.image = load_image('salt.png')
            self.saltSprite.image = pygame.transform.rotate(self.saltSprite.image, 90)
            self.saltSprite.rect =  self.saltSprite.image.get_rect()
            self.saltSprite.rect.move_ip(x,(Settings.SCREEN_HEIGHT - 31))
            self.add(self.saltSprite)
            
            #surface.blit(self.saltSprite.image, (x,0))
            #surface.blit(self.saltSprite.image, (x,(Settings.SCREEN_HEIGHT - 31)))
            x += 315