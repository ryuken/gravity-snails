import pygame
from pygame.locals import *
from gui.menu import Menu
from gui.button import Button
from settings import Settings
from gui.label import Label

class Inventory(Menu):
    """
    @ivar title: The title of the inventory
    @ivar max_weapons: The maximum weapons the inventory can hold
    @ivar visible: Represents wether this inventory is visible or not
    @ivar selectedItemIndex: The index of the selected item/weapon inside the inventory
    """

    def __init__(self, title):
        """
        @param title: The title of the inventory
        @summary: Initializes an inventory
        """
        Menu.__init__(self)
        self.max_weapons = 20
        self.weapons = []
        self.visible = True
        self.selectedItemIndex = None
        size = []
        size.append(Settings.SCREEN_WIDTH/4)
        size.append(Settings.SCREEN_HEIGHT/4)
        location = []
        location.append(Settings.SCREEN_WIDTH/2 - size[0]/2)
        location.append(Settings.SCREEN_HEIGHT/2 - size[1]/2)
        self.rect = Rect(location[0], location[1], size[0], size[1])
        self.title = title
        myTitleLable = Label(title)
        self.addWidget(myTitleLable)
        self.addWidget(Label(" "))

    def addWeapon(self, weapon):
        """
        @param weapon: The weapon to be added to the inventory
        @summary: Adds a weapon to the inventory if the inventory still has room for it
        """
        self.selectedItemIndex = 0
        if len(self.weapons) < self.max_weapons:
            self.weapons.append(weapon)
            weaponButton = Button(weapon.name, self.selectItem, len(self.weapons)-1)
            self.addWidget(weaponButton)
        else:
            print("Weapons full")

    def update(self, input):
        """
        @param input: The user input
        @summary: updates the inventory status based on the user input
        """
        Menu.update(self, input)
        if(not None == self.selectedItemIndex):
            self.visible = False
            returnWeapon = self.weapons[self.selectedItemIndex]
            self.selectedItemIndex = None
            return returnWeapon
        else:
            return None

    def selectItem(self, args):
        """
        @param args: The argumens array
        @summary: selects an item based on the arguments inside the "args" array
        """
        self.selectedItemIndex = args[0]
        self.visible = False
