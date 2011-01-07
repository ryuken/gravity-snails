import pygame
from scenemanager import SceneManager
from gui.button import Button
from gui.slider import Slider
from settings import Settings
from menu import Menu
from game import Game
from settingsmenu import SettingsMenu

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.addOption(Button("Start", self.runGame))
        self.addOption(Button("Settings", self.runSettingsMenu))
        self.addOption(Button("Help", self.runSettingsMenu))
        self.addOption(Button("Quit", self.runSettingsMenu))
    def runGame(self):
        game = Game()
        game.mainmenu = self
        SceneManager().setScene(game)

    def runSettingsMenu(self):
        SceneManager().setScene(SettingsMenu(self))