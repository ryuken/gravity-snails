import pygame

class Inventory(object):

    def __init__(self):
        self.max_items = 5
        self.max_weapons = 20
        self.weapons = list()
        self.items = list()
        
    def addWeapon(self, weapon):
        if len(self.weapons) < self.max_weapons:
                self.weapons.add(weapon)
        else:
            print "Weapons full"
        
    def addItem(self, item):
        if len(self.items < self.max_items):
            self.items.add(item)
        else:
            print "Item's full"