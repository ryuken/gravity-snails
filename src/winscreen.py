import pygame
from scenemanager import SceneManager
from gui.button import Button
from gui.label import Label
from menu import Menu
from settingsmenu import SettingsMenu

class WinScreen(Menu):
    def __init__(self, nextScene, teamColor):
        Menu.__init__(self)
        self.nextScene = nextScene
        self.addOption(Label("!!! Congratulations !!!"))
        self.addOption(Label(" "))
        self.teamColor = teamColor
        self.addOption(Label("The "+self.teamColor+" team has won"))
        self.addOption(Label(" "))
        self.addOption(Button("BACK", self.runNextScene))

    def runNextScene(self):
        SceneManager().setScene(self.nextScene)