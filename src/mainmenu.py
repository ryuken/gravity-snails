from scenemanager import SceneManager
from gui.button import Button
from menu import Menu
from game import Game
from settingsmenu import SettingsMenu
from help import HelpMenu

class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.helpMenu = HelpMenu(self)

        self.addOption(Button("Start", self.runGame))
        self.addOption(Button("Settings", self.runSettingsMenu))
        self.addOption(Button("Help", self.runHelpMenu))
        self.addOption(Button("Quit", self.quitGame))
        
    def runGame(self):
        game = Game()
        game.mainmenu = self
        SceneManager().setScene(game)

    def runSettingsMenu(self):
        SceneManager().setScene(SettingsMenu(self))

    def runHelpMenu(self):
        SceneManager().setScene(self.helpMenu)

    def quitGame(self):
        SceneManager().setScene(None) #No scene, means quit game!