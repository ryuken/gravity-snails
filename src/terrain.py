import pygame
import random

from utils import load_image
from salt import Salt
class Terrain(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.salt = Salt()
    
    def create(self, n):
        self.createWestBorder(n)
        self.createNorthBorder(n)
        self.createEastBorder(n)
        self.createSouthBorder(n)
        
    def createWestBorder(self, n):
        for i in range(0,n):
            self.addBlock(random.randint(0,100), random.randint(0,640))
            
    def createNorthBorder(self, n):
        for i in range(0,n):
            self.addBlock(random.randint(0,640), random.randint(0,100))
 
    def createEastBorder(self, n):
        for i in range(0,n):
            self.addBlock(random.randint(540,640), random.randint(0,640))
            
    def createSouthBorder(self, n):
        for i in range(0,n):
            self.addBlock(random.randint(0,640), random.randint(540,640))

    def addBlock(self, x, y):
        terrainSprite = pygame.sprite.Sprite()
        terrainSprite.image = load_image("ground.png")
        terrainSprite.rect = terrainSprite.image.get_rect()
        terrainSprite.rect.move_ip(x, y)
        # add it to the terrain group
        self.add(terrainSprite)
        
        
    def draw(self, surface):
        pygame.sprite.Group.draw(self, surface)  
        self.salt.draw(surface)
