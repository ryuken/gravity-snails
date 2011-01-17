from scenes.scenemanager import SceneManager
from gui.button import Button
from scenes.scene import Scene
from gui.menu import Menu
from scenes.game import Game
from scenes.settingsmenu import SettingsMenu
from scenes.help import HelpMenu

class MainMenu(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.helpMenu = HelpMenu(self)

        self.menu = Menu()
        self.menu.addWidget(Button("Start", self.runGame))
        self.menu.addWidget(Button("Settings", self.runSettingsMenu))
        self.menu.addWidget(Button("Help", self.runHelpMenu))
        self.menu.addWidget(Button("Quit", self.quitGame))

    def draw(self, surface):
        self.menu.draw(surface)

    def update(self, input):
        self.menu.update(input)

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