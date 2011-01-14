import pygame
from pygame.locals import *
from gui.menu import Menu
from gui.button import Button
from settings import Settings
from gui.label import Label

class Inventory(Menu):

    def __init__(self, title):
        Menu.__init__(self)
        self.max_items = 5
        self.max_weapons = 20
        self.weapons = []
        self.items = []
        self.visible = False
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
        if len(self.weapons) < self.max_weapons:
            self.weapons.append(weapon)
            weaponButton = Button(weapon.name, self.selectItem, len(self.weapons)-1)
            self.addWidget(weaponButton)
        else:
            print "Weapons full"

    def update(self, input):
        Menu.update(self, input)
        if(not None == self.selectedItemIndex):
            return self.weapons[self.selectedItemIndex]
        else:
            return None

    def addItem(self, item):
        if len(self.items < self.max_items):
            self.items.append(item)
        else:
            print "Item's full"
    def selectItem(self, args):
        self.selectedItemIndex = args[0]
        self.visible = False