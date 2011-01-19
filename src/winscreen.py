import pygame
from scenemanager import SceneManager
from gui.button import Button
from gui.label import Label
from gui.frame import Frame
from scene import Scene
from settingsmenu import SettingsMenu

class WinScreen(Scene):
    def __init__(self, nextScene, teamColor):
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

    def draw(self, surface):
        self.frame.draw(surface)
        
    def update(self, input):
        self.frame.update(input)
    
    def runNextScene(self):
        SceneManager().setScene(self.nextScene)