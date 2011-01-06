import pygame
from enums import GameModes

from gui.button import Button
from gui.slider import Slider
from settings import Settings
from menu import Menu

from scenemanager import SceneManager
class SettingsMenu(Menu):
    def __init__(self, parentScene):
        Menu.__init__(self)
        self.parentScene = parentScene
        self.slider = Slider((32,32), 2, 4, Settings.GAME_PLAYERS)
        self.buttonOk = Button(pygame.Rect(32, 96, 128, 32), "Ok")
        self.buttonOk.register_action(self.applySettings)
        self.addOption(self.slider)
        self.addOption(self.buttonOk)

    def applySettings(self):
        Settings.GAME_PLAYERS = self.slider.value
        SceneManager().setScene(self.parentScene)
