import pygame
from enums import GameModes

from gui.button import Button
from gui.slider import Slider
from settings import Settings
from input import Input

from game import Game

class Menu(object):
    def __init__(self):
        #Init
        self.initPygame()
        self.initScreen()
        self.initClock()
        self.initInput()
    
    def initPygame(self):
        result = pygame.init()
        return result[1]

    def initScreen(self):
        self.surface = pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT]) #retourneert Surface
        pygame.display.set_caption(Settings.GAME_TITLE)
        
    def initClock(self):
        self.clock = pygame.time.Clock()
        
    def initInput(self):
        self.input = Input()
        
    def run(self):
        self.runMainMenu()
        
    def runMainMenu(self):
        self.gamemode = GameModes.MENU_MAIN
        
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
        
        while self.gamemode == GameModes.MENU_MAIN:
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            self.buttonStart.update(self.input)
            self.buttonSettings.update(self.input)
            
            self.surface.fill(Settings.SCREEN_COLOR)
            self.buttonStart.draw(self.surface)
            self.buttonSettings.draw(self.surface)
            pygame.display.flip()
    
    def applySettings(self):
        Settings.GAME_PLAYERS = self.slider.value
        self.gamemode = GameModes.MENU_MAIN
        
    def runSettingsMenu(self):
        self.gamemode = GameModes.MENU_SETTINGS
        self.slider = Slider((32,32), 2, 4, Settings.GAME_PLAYERS)
        self.buttonOk = Button(pygame.Rect(32, 96, 128, 32), "Ok")
        self.buttonOk.register_action(self.applySettings)
        while self.gamemode == GameModes.MENU_SETTINGS:
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            self.slider.update(self.input)
            self.buttonOk.update(self.input)
            self.surface.fill(Settings.SCREEN_COLOR)
            self.slider.draw(self.surface)
            self.buttonOk.draw(self.surface)
            pygame.display.flip()
            
    def runGame(self):
        Game().run()