import pygame
import random

import utils

class Terrain(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

        # create a terrain sprite

        for i in range(0,5):
            terrainSprite = pygame.sprite.Sprite()
            terrainSprite.image = utils.load_image("ground.png")
            terrainSprite.rect = terrainSprite.image.get_rect()
            terrainSprite.rect.move_ip(random.randint(0,640), random.randint(0,640))
            # add it to the terrain group
            self.add(terrainSprite)
        terrainSprite = pygame.sprite.Sprite()
        terrainSprite.image = utils.load_image("ground.png")
        terrainSprite.rect = terrainSprite.image.get_rect()
        terrainSprite.rect.move_ip(0, 640 - 100)
        self.add(terrainSprite)

        terrainSprite = pygame.sprite.Sprite()
        terrainSprite.image = utils.load_image("ground.png")
        terrainSprite.rect = terrainSprite.image.get_rect()
        terrainSprite.rect.move_ip(0, 0)
        self.add(terrainSprite)
