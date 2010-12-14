import pygame
import random

from utils import load_image

class Terrain(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

        # create a terrain sprite

        for int in range(0,5):
            terrainSprite = pygame.sprite.Sprite()
            terrainSprite.image = load_image("ground.png")
            terrainSprite.rect = terrainSprite.image.get_rect()
            terrainSprite.rect.move_ip(random.randint(0,100), random.randint(0,640))
            # add it to the terrain group
            self.add(terrainSprite)
            
        for i in range(0,5):
            terrainSprite = pygame.sprite.Sprite()
            terrainSprite.image = load_image("ground.png")
            terrainSprite.rect = terrainSprite.image.get_rect()
            terrainSprite.rect.move_ip(random.randint(0,640), random.randint(0,100))
            # add it to the terrain group
            self.add(terrainSprite)
            
        for i in range(0,5):
            terrainSprite = pygame.sprite.Sprite()
            terrainSprite.image = load_image("ground.png")
            terrainSprite.rect = terrainSprite.image.get_rect()
            terrainSprite.rect.move_ip(random.randint(540,640), random.randint(0,640))
            # add it to the terrain group
            self.add(terrainSprite)
            
        for i in range(0,5):
            terrainSprite = pygame.sprite.Sprite()
            terrainSprite.image = load_image("ground.png")
            terrainSprite.rect = terrainSprite.image.get_rect()
            terrainSprite.rect.move_ip(random.randint(0,640), random.randint(540,640))
            # add it to the terrain group
            self.add(terrainSprite)
