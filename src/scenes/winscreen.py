import pygame
from scenes.scenemanager import SceneManager
from gui.button import Button
from gui.label import Label
from gui.frame import Frame
from scenes.scene import Scene
from scenes.settingsmenu import SettingsMenu
from utils import load_sound
class WinScreen(Scene):
    """
    @ivar nextScene: The scene which should come after this screen
    """
    def __init__(self, nextScene, teamColor):
        """
        @param nextScene: The scene which should come after this win screen
        @param teamColor: The color of the winning team
        @summary: Initializes win screen for the winning team
        """
        Scene.__init__(self)
        self.nextScene = nextScene
        self.frame = Frame()
        text = "!!! Congratulations !!!\n"
        text += "\n"
        text += "The " + teamColor + " team has won"
        labelText = Label(text)
        labelText.rect.center = (self.frame.rect.width / 2, self.frame.rect.height / 2)

        buttonBack = Button("Back", self.runNextScene)
        buttonBack.rect.size = (128, 32)
        buttonBack.rect.centerx = self.frame.rect.width / 2
        buttonBack.rect.bottom = self.frame.rect.height - 32

        self.frame.addWidget(labelText)
        self.frame.addWidget(buttonBack)

        self.victory_sound = load_sound("victory.ogg")
        self.victory_sound.play()

    def draw(self, surface):
        """
        @param surface: The surface which the win screen should be drawed on
        @summary: draws the win screen on a specified surface
        """
        self.frame.draw(surface)

    def update(self, input):
        """
        @param input: The user input
        @summary: updates the status of the win screen based on the user input
        """
        self.frame.update(input)

    def runNextScene(self):
        """
        @summary: closes the help frame and tells sceneManager to go to next scene
        """
        self.victory_sound.stop()
        SceneManager().setScene(self.nextScene)
