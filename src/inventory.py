import pygame

class Inventory(object):

    def __init__(self):
        self.max_items = 5
        self.max_weapons = 20
        self.weapons = []
        self.items = []
        
    def addWeapon(self, weapon):
        if len(self.weapons) < self.max_weapons:
                self.weapons.append(weapon)
        else:
            print "Weapons full"
        
    def addItem(self, item):
        if len(self.items < self.max_items):
            self.items.append(item)
        else:
            print "Item's full"