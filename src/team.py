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
    
    def update(self, *args):
        pygame.sprite.Group.update(self,*args)
        self.active_weapon.update(*args)
        
    def draw(self, surface):
        pygame.sprite.Group.draw(self, surface)
        if self.hasTurn:
            self.active_weapon.snail_rect = self.currentSnailWithTurn.rect
            self.active_weapon.draw(surface)
                        
    def addSnails(self, numberOfSnails):
        for i in range(0, numberOfSnails):
            snail = Snail(self)
            self.add(snail)
            self.orderedSnailList.append(snail)
            
            # give the first snail in the team the turn
            if i == 0:
                self.currentSnailWithTurn = snail
                snail.hasTurn = True
    
    def nextSnailTurn(self):
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
                    nextSnail = self.orderedSnailList[0]
                    nextSnail.hasTurn = True
                    self.currentSnailWithTurn = nextSnail
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