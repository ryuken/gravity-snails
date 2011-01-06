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
        button_amount = 2
        button_width = 128
        button_height = 32
        button_space = 32

        position_x = (Settings.SCREEN_WIDTH / 2) - (button_width / 2)
        menu_height = ((button_height + button_space) * button_amount) - button_space
        position_y = (Settings.SCREEN_HEIGHT / 2) - (menu_height / 2)

        self.buttonStart = Button(pygame.Rect(position_x,position_y,button_width,button_height), "Start")
        self.buttonStart.register_action(self.runGame)
        self.buttonSettings = Button(pygame.Rect(position_x,position_y + ((button_height + button_space) * 1),button_width,button_height), "Settings")
        self.buttonSettings.register_action(self.runSettingsMenu)

        self.addOption(self.buttonStart)
        self.addOption(self.buttonSettings)

    def runGame(self):
        SceneManager().setScene(Game())

    def runSettingsMenu(self):
        SceneManager().setScene(SettingsMenu(self))