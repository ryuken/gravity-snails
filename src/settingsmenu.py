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
        self.sliderPlayers = Slider(2, 4, Settings.GAME_PLAYERS)
        self.sliderStartTime = Slider(10, 90, Settings.TIMER_STARTTIME)
        self.sliderBreakTime = Slider(0,10, Settings.TIMER_BREAKTIME)
        
        self.addOption(self.sliderPlayers)
        self.addOption(self.sliderStartTime)
        self.addOption(self.sliderBreakTime)
        self.addOption(Button("Ok",self.applySettings))

    def applySettings(self):
        Settings.GAME_PLAYERS = self.sliderPlayers.value
        Settings.TIMER_STARTTIME = self.sliderStartTime.value
        Settings.TIMER_BREAKTIME = self.sliderBreakTime.value
        SceneManager().setScene(self.parentScene)
