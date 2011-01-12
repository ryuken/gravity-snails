import pygame

from inventory import Inventory
from weapon import Weapon
from snail import Snail
from turnmanager import TurnManager

class Team(pygame.sprite.Group):

    def __init__(self, name):
        pygame.sprite.Group.__init__(self)
        self.name = name
        self.hasTurn = False
        # When initialized the list of snails is empty so not alive!
        self.isAlive = False

        self.orderedSnailList = []
        self.currentSnailWithTurn = None

        self.gravity_direction = None

        self.inventory = Inventory()
        cannon = Weapon("Canon", 20)
        self.inventory.addWeapon(cannon)

        self.active_weapon = cannon

        self.colorIndex = None

    def update(self, *args):
        pygame.sprite.Group.update(self,*args)
        self.active_weapon.update(*args)
        self.checkAlive()

    def draw(self, surface):
        #pygame.sprite.Group.draw(self, surface)
        for sprite in self:
            sprite.draw(surface)
            
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

#    def nextSnailTurn(self):
#        snailIterator = iter(self.orderedSnailList)
#
#        for snail in snailIterator:
#            if snail.hasTurn:
#                snail.hasTurn = False
#                nextSnail = None
#                try:
#                    nextSnail = snailIterator.next()
#                    if nextSnail:
#                        nextSnail.hasTurn = True
#                        self.currentSnailWithTurn = nextSnail
#                except StopIteration:
#                    nextSnail = self.orderedSnailList[0]
#                    nextSnail.hasTurn = True
#                    self.currentSnailWithTurn = nextSnail

    def setGravity(self, direction):
        self.gravity_direction = direction
        for s in self.sprites():
            s.gravity_direction = direction

    """
    sets the image of the team using a number
    the sprites folder contains snails with 4 different colors
    the number given will be used to select a different snail
    """
    def setTeamImage(self, imageNumber):
        self.colorIndex = imageNumber
        rightAndLeftImages=['snail', 'snail']
        rightAndLeftImages[0] += str(imageNumber) + 'Right.png'
        rightAndLeftImages[1] += str(imageNumber) + 'Left.png'
        for s in self.sprites():
            s.setImages(rightAndLeftImages)

    def checkAlive(self):
        for snail in self.orderedSnailList:
            if snail.isAlive == False:
                if self.hasTurn == True and snail.hasTurn == True:
                    TurnManager().stopTurn()
                    TurnManager().changeTurnSnail()
                if snail == self.currentSnailWithTurn:
                    TurnManager().changeTurnSnail(self)
                self.orderedSnailList.remove(snail)
                snail.kill()
        # Check if all the snails are dead
        if len(self.orderedSnailList) > 0:
            self.isAlive = True
        else:
            self.isAlive = False
            TurnManager().teams.remove(self)