from scenes.scenemanager import SceneManager
from gui.button import Button
from scenes.scene import Scene
from gui.menu import Menu
from scenes.game import Game
from scenes.settingsmenu import SettingsMenu
from scenes.help import HelpMenu

class MainMenu(Scene):
    def __init__(self):
        """
        @summary: Initializes a main menu
        """
        Scene.__init__(self)
        self.helpMenu = HelpMenu(self)

        self.menu = Menu()
        self.menu.addWidget(Button("Start", self.runGame))
        self.menu.addWidget(Button("Settings", self.runSettingsMenu))
        self.menu.addWidget(Button("Help", self.runHelpMenu))
        self.menu.addWidget(Button("Quit", self.quitGame))

    def draw(self, surface):
        """
        @param surface: The surface which the main menu should be drawed on
        @summary: draws the main menu on a specified surface
        """
        self.menu.draw(surface)

    def update(self, input):
        """
        @param input: The user input
        @summary: updates the status of the main menu based on the user input
        """
        self.menu.update(input)

    def runGame(self):
        """
        @summary: runs a new game
        """
        game = Game()
        game.mainmenu = self
        SceneManager().setScene(game)

    def runSettingsMenu(self):
        """
        @summary: shows the settings menu
        """
        SceneManager().setScene(SettingsMenu(self))

    def runHelpMenu(self):
        """
        @summary: shows the help screen
        """
        SceneManager().setScene(self.helpMenu)

    def quitGame(self):
        """
        @summary: quits the game
        """
        SceneManager().setScene(None) #No scene, means quit game!