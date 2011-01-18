import pygame

from inventory import Inventory
from weapons.cannon import Cannon
from weapons.balloon_launcher import BalloonLauncher
from snail import Snail
from turnmanager import TurnManager

class Team(pygame.sprite.Group):
    """
    This is the team class, which is the owner of a group of snails.
    Several snails together form a team.
    """
    def __init__(self, name):
        """
        Constructor to create a team of snails
        @param name: The name of the team, which will displayed in various locations
        @return: Team object.
        """ 
        pygame.sprite.Group.__init__(self)
        
        self.name = name
        """ The name of the team"""
        
        self.hasTurn = False

        self.isAlive = True

        self.orderedSnailList = []

        self.gravity_direction = None

        self.inventory = Inventory(self.name)
        cannon = Cannon("Cannon", 20)
        balloonLauncher = BalloonLauncher("Balloon", 30)

        self.inventory.addWeapon(balloonLauncher)
        self.inventory.addWeapon(cannon)

        self.active_weapon = cannon

        self.colorIndex = None
    
    

    def update(self, *args):
        """
        Call the update of all the objects the team currently manages, this can include weapon, inventory and snails.
        @param *args: Pass all the arguments to the the update of the sprites. 
        """
        pygame.sprite.Group.update(self,*args)
        self.checkAlive()
        if(self.inventory.visible and self.hasTurn):
            tempWeapon = self.inventory.update(args[0])
            if(not None == tempWeapon):
                self.active_weapon = tempWeapon
        if(not None == self.active_weapon):
            self.active_weapon.update(*args)


    def draw(self, surface):
        """
        Draw all the objects the team currently manages, this can include weapon, inventory and snails.
        @param surface: This is the surface created in the game class 
        """
        for sprite in self:
            sprite.draw(surface)

        #draw the inventory if team has turn
        if(self.hasTurn):
            self.active_weapon.draw(surface)
            self.inventory.draw(surface)

        if self.hasTurn and not None == self.active_weapon:
            for snail in self.orderedSnailList:
                if snail.hasTurn == True:
                    self.active_weapon.snail_rect = snail.rect

    def addSnails(self, numberOfSnails):
        """
        Add a number of snails to the teams, this creates snails objects.
        """
        for i in range(0, numberOfSnails):
            snail = Snail(self)
            snail.id = i
            self.add(snail)
            self.orderedSnailList.append(snail)

        self.orderedSnailList[len(self.orderedSnailList) - 1].hasTurn = True
    
    
    def setGravity(self, direction):
        """
        Set the gravity direction for the team
        @param direction: An integer representing a value. Use enums.Direction.
        """
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
        """
        Check if the team is alive and if every snail of the team is still alive
        Remove the dead snails from the orderedlist and change the turn if a snail died while having the turn.
        @return: True if the team still has snails at least 1, which means alive else False
        """
        # Loop thru snail's
        for snail in self.orderedSnailList:
            # Check if the snail is alive
            if snail.isAlive == False:
                # remove the snail from the ordered list of snails
                self.orderedSnailList.remove(snail)
                snail.kill()

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
            print "removed " + self.name