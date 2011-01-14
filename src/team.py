import pygame

from inventory import Inventory
from weapon import Weapon
from balloon_launcher import BalloonLauncher
from snail import Snail
from turnmanager import TurnManager

class Team(pygame.sprite.Group):

    def __init__(self, name):
        pygame.sprite.Group.__init__(self)
        self.name = name
        self.hasTurn = False
        
        self.isAlive = True

        self.orderedSnailList = []

        self.gravity_direction = None

        self.inventory = Inventory()
        cannon = Weapon("Canon", 20)
        balloonLauncher = BalloonLauncher("Balloon launcher", 30)
        
        self.inventory.addWeapon(balloonLauncher)
        self.inventory.addWeapon(cannon)

        self.active_weapon = cannon

        self.colorIndex = None

    def update(self, *args):
        pygame.sprite.Group.update(self,*args)
        self.active_weapon.update(*args)
        self.checkAlive()

    def draw(self, surface):
        for sprite in self:
            sprite.draw(surface)

        if self.hasTurn:
            for snail in self.orderedSnailList:
                if snail.hasTurn == True:
                    self.active_weapon.snail_rect = snail.rect
                    self.active_weapon.draw(surface)

    def addSnails(self, numberOfSnails):
        for i in range(0, numberOfSnails):
            snail = Snail(self)
            self.add(snail)
            self.orderedSnailList.append(snail)

        self.orderedSnailList[len(self.orderedSnailList) - 1].hasTurn = True

    def setGravity(self, direction):
        self.gravity_direction = direction
        for s in self.sprites():
            s.gravity_direction = direction

    def setTeamImage(self, imageNumber):
        """
        sets the image of the team using a number
        the sprite's folder contains snails with 4 different colors
        the number given will be used to select a different snail
        """
        
        self.colorIndex = imageNumber
        rightAndLeftImages=['snail', 'snail']
        rightAndLeftImages[0] += str(imageNumber) + 'Right.png'
        rightAndLeftImages[1] += str(imageNumber) + 'Left.png'
        for s in self.sprites():
            s.setImages(rightAndLeftImages)

    def checkAlive(self):
        # Loop thru snail's
        for snail in self.orderedSnailList:
            # Check if the snail is alive
            if snail.isAlive == False:
                if self.hasTurn == True and snail.hasTurn == True:
                    TurnManager().stopTurn()
                elif self.hasTurn == False and snail.hasTurn == True:
                    TurnManager().changeTurnSnail(self)
                      
        # Check if all the snails are dead
        if len(self.orderedSnailList) > 0:
            self.isAlive = True
        else:
            self.isAlive = False
            TurnManager().teams.remove(self)