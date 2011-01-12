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
        self.addWidget(Label("!!! Congratulations !!!"))
        self.addWidget(Label(" "))
        self.teamColor = teamColor
        self.addWidget(Label("The "+self.teamColor+" team has won"))
        self.addWidget(Label(" "))
        self.addWidget(Button("BACK", self.runNextScene))

    def runNextScene(self):
        SceneManager().setScene(self.nextScene)