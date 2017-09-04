import pygame
from enums import GameModes

from gui.button import Button
from gui.slider import Slider
from settings import Settings
from scenes.scene import Scene
from gui.menu import Menu

from scenes.scenemanager import SceneManager
class SettingsMenu(Scene):
    def __init__(self, parentScene):
        """
        Initialize the Settingsmenu
        @param parentScene: The scene he should go back to when the settings are adjusted
        """

        Scene.__init__(self)
        self.parentScene = parentScene
        self.frame = Menu()
        self.sliderPlayers = Slider(2, 4, Settings.GAME_PLAYERS, "Players: ")
        self.sliderSnails = Slider(2, 10, Settings.GAME_SNAILS, "Snails: ")
        self.sliderSnailsHp = Slider(1, 150, Settings.GAME_SNAILS_HP, "Hitpoints: ", 10)
        self.sliderStartTime = Slider(10, 90, Settings.TIMER_STARTTIME, "Turntime: ", 10)
        self.sliderBreakTime = Slider(1,10, Settings.TIMER_BREAKTIME, "Breaktime: ")

        self.frame.addWidget(self.sliderPlayers)
        self.frame.addWidget(self.sliderSnails)
        self.frame.addWidget(self.sliderSnailsHp)
        self.frame.addWidget(self.sliderStartTime)
        self.frame.addWidget(self.sliderBreakTime)
        self.frame.addWidget(Button("Ok",self.applySettings))

    def update(self, input):
        """
        Update the settingsmenu
        @param input: The input class
        """
        self.frame.update(input)

    def draw(self, surface):
        """
        Draw the settingsmenu on a surface
        @param surface: The surface the settingsmenu should be drawed on
        """
        self.frame.draw(surface)

    def applySettings(self):
        """
        Adjust the game settings
        """
        Settings.GAME_PLAYERS = self.sliderPlayers.value
        Settings.GAME_SNAILS = self.sliderSnails.value
        Settings.GAME_SNAILS_HP = self.sliderSnailsHp.value
        Settings.TIMER_STARTTIME = self.sliderStartTime.value
        Settings.TIMER_BREAKTIME = self.sliderBreakTime.value
        SceneManager().setScene(self.parentScene)
