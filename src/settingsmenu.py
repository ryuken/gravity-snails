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
        self.sliderPlayers = Slider(2, 4, Settings.GAME_PLAYERS, "Players: ")
        self.sliderSnails = Slider(2, 10, Settings.GAME_SNAILS, "Snails: ")
        self.sliderStartTime = Slider(10, 90, Settings.TIMER_STARTTIME, "Turntime: ")
        self.sliderBreakTime = Slider(0,10, Settings.TIMER_BREAKTIME, "Breaktime: ")

        self.addOption(self.sliderPlayers)
        self.addOption(self.sliderSnails)
        self.addOption(self.sliderStartTime)
        self.addOption(self.sliderBreakTime)
        self.addOption(Button("Ok",self.applySettings))

    def applySettings(self):
        Settings.GAME_PLAYERS = self.sliderPlayers.value
        Settings.GAME_SNAILS = self.sliderSnails.value
        Settings.TIMER_STARTTIME = self.sliderStartTime.value
        Settings.TIMER_BREAKTIME = self.sliderBreakTime.value
        SceneManager().setScene(self.parentScene)
