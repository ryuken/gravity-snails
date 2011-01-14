import pygame
from enums import GameModes

from gui.button import Button
from gui.slider import Slider
from settings import Settings
from scene import Scene
from menu import Menu

from scenemanager import SceneManager
class SettingsMenu(Scene):
    def __init__(self, parentScene):
        Scene.__init__(self)
        self.parentScene = parentScene
        self.frame = Menu()
        self.sliderPlayers = Slider(2, 4, Settings.GAME_PLAYERS, "Players: ")
        self.sliderSnails = Slider(2, 10, Settings.GAME_SNAILS, "Snails: ")
        self.sliderSnailsHp = Slider(1, 150, Settings.GAME_SNAILS_HP, "Hitpoints: ")
        self.sliderStartTime = Slider(10, 90, Settings.TIMER_STARTTIME, "Turntime: ")
        self.sliderBreakTime = Slider(0,10, Settings.TIMER_BREAKTIME, "Breaktime: ")

        self.frame.addWidget(self.sliderPlayers)
        self.frame.addWidget(self.sliderSnails)
        self.frame.addWidget(self.sliderSnailsHp)
        self.frame.addWidget(self.sliderStartTime)
        self.frame.addWidget(self.sliderBreakTime)
        self.frame.addWidget(Button("Ok",self.applySettings))
        
    def update(self, input):
        self.frame.update(input)
        
    def draw(self, surface):
        self.frame.draw(surface)
        
    def applySettings(self):
        Settings.GAME_PLAYERS = self.sliderPlayers.value
        Settings.GAME_SNAILS = self.sliderSnails.value
        Settings.GAME_SNAILS_HP = self.sliderSnailsHp.value
        Settings.TIMER_STARTTIME = self.sliderStartTime.value
        Settings.TIMER_BREAKTIME = self.sliderBreakTime.value
        SceneManager().setScene(self.parentScene)
