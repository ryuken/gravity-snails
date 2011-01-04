import pygame

from snail import Snail

class Team(pygame.sprite.Group):

    def __init__(self, name):
        pygame.sprite.Group.__init__(self)
        self.name = name
        self.hasTurn = False

        self.orderedSnailList = []
        self.currentSnailTurn = None

        self.gravity_direction = None
        
    def draw(self, surface):
        pygame.sprite.Group.draw(self, surface)
        for s in self.sprites():
            s.draw(surface)
                        
    def addSnails(self, numberOfSnails):
        for i in range(0, numberOfSnails):
            snail = Snail(self)
            self.add(snail)
            
            self.orderedSnailList.append(snail)
            
            snail.id = i
            if i == 0:
                self.currentSnailTurn = 0
                snail.hasTurn = True
    
    def nextSnailTurn(self):
        currentSnail = self.orderedSnailList[self.currentSnailTurn]
        if currentSnail.hasTurn == True:
            currentSnail.hasTurn = False
            nextSnailID = self.currentSnailTurn + 1
            if nextSnailID < len(self.sprites()):    
                self.currentSnailTurn = nextSnailID
                self.orderedSnailList[nextSnailID].hasTurn = True
            else:
                self.currentSnailTurn = 0
                self.orderedSnailList[0].hasTurn = True
        else:
            raise ValueError("Current snail should be true, but it wasn't!")
    
    def setGravity(self, direction):
        self.gravity_direction = direction
        for s in self.sprites():
            s.gravity_direction = direction
            
    def isAlive(self):
        # Check if all the snails are dead
        for s in self.orderedSnailList:
            if s.hitpoints > 0 and s.alive():
                return True
        return False