import pygame
from scenemanager import SceneManager
from gui.button import Button
from gui.label import Label
from gui.slider import Slider
from settings import Settings
from menu import Menu
from game import Game
from settingsmenu import SettingsMenu

class HelpMenu(Menu):
    def __init__(self, previousScene):
        Menu.__init__(self)
        self.previousScene = previousScene
        self.addOption(Label("Welcome to gravity snails"))
        self.addOption(Label("=================="))
        self.addOption(Label(" "))
        self.addOption(Label("Use mouse to place snails in screen"))
        self.addOption(Label("Use arrow keys to move and to target"))
        self.addOption(Label("Use SPACE to shoot"))
        self.addOption(Label(" "))
        self.addOption(Label("You can't shoot the snails themself"))
        self.addOption(Label("A snail only dies if it falls into the salt"))
        self.addOption(Label("So you need shoot away the ground it stands on!"))
        self.addOption(Label(" "))
        self.addOption(Button("BACK", self.runPreviousScene))

    def runPreviousScene(self):
        SceneManager().setScene(self.previousScene)