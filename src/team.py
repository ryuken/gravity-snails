import pygame

from inventory import Inventory
from weapon import Weapon
from snail import Snail

class Team(pygame.sprite.Group):

    def __init__(self, name):
        pygame.sprite.Group.__init__(self)
        self.name = name
        self.hasTurn = False

        self.orderedSnailList = []
        self.currentSnailWithTurn = None

        self.gravity_direction = None
        
        self.inventory = Inventory()
        cannon = Weapon("Canon", 20)
        self.inventory.addWeapon(cannon)
        
        self.active_weapon = cannon
        
    def draw(self, surface):
        pygame.sprite.Group.draw(self, surface)
        if self.hasTurn and self.currentSnailWithTurn.hasTurn:
            bool = True
        else:
            bool = False
        self.active_weapon.draw(surface, self.currentSnailWithTurn.rect, bool)
                        
    def addSnails(self, numberOfSnails):
        for i in range(0, numberOfSnails):
            snail = Snail(self)
            self.add(snail)
            self.orderedSnailList.append(snail)
            if i == 0:
                self.currentSnailWithTurn = snail
                snail.hasTurn = True
    
    def nextSnailTurn(self):
#        currentSnail = self.orderedSnailList[self.currentSnailTurn]
#        if currentSnail.hasTurn == True:
#            currentSnail.hasTurn = False
#            nextSnailID = self.currentSnailTurn + 1
#            if nextSnailID < len(self.sprites()):    
#                self.currentSnailTurn = nextSnailID
#                self.orderedSnailList[nextSnailID].hasTurn = True
#            else:
#                self.currentSnailTurn = 0
#                self.orderedSnailList[0].hasTurn = True
#        else:
#            raise ValueError("Current snail should be true, but it wasn't!")
#        stillNeedToGiveTurn = True
        snailIterator = iter(self.orderedSnailList)
        for snail in snailIterator:
            if snail.hasTurn:
                snail.hasTurn = False
                nextSnail = None
                try:
                    nextSnail = snailIterator.next()
                    if nextSnail:
                        nextSnail.hasTurn = True
                        self.currentSnailWithTurn = nextSnail
                except StopIteration:
                    self.orderedSnailList[0].hasTurn = True
                    return
                        
                    

                        
    
    def setGravity(self, direction):
        self.gravity_direction = direction
        for s in self.sprites():
            s.gravity_direction = direction
            
    def isAlive(self):
        # Check if all the snails are dead
        for s in self.orderedSnailList:                
            if s.isAlive:
                return True
        return False