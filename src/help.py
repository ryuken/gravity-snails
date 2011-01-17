from scenemanager import SceneManager
from gui.button import Button
from gui.label import Label
from scene import Scene
from gui.frame import Frame

class HelpMenu(Scene):
    def __init__(self, previousScene):
        Scene.__init__(self)
        self.previousScene = previousScene
        self.frame = Frame()
        text  = "Welcome to gravity snails\n"
        text += "=========================\n"
        text += "\n"
        text += "You can shoot the snails and the terrain beneath them\n"
        text += "Snails die if they touch the salt\nor when they are out of hitpoints\n"
        text += "\nCONTROLS\n=========================\n\n"
        text += "LEFT MOUSE BUTTON:\nplace snails in the screen\n\n"
        text += "ARROW KEYS:\nmove and target\n\n"
        text += "SPACE BAR:\nfire the active weapon\n\n"
        text += "RIGHT MOUSE BUTTON:\nswitch weapon\n\n"
        text += "\n"
        labelText = Label(text)
        labelText.centerLines = False
        labelText.rect.center = (self.frame.rect.width / 2, self.frame.rect.height / 2)
        self.frame.addWidget(labelText)

        buttonBack = Button("Back", self.runPreviousScene)
        buttonBack.rect.size = (128, 32)
        buttonBack.rect.centerx = self.frame.rect.width / 2
        buttonBack.rect.bottom = self.frame.rect.height - 32
        self.frame.addWidget(buttonBack)

    def update(self, input):
        self.frame.update(input)

    def draw(self, surface):
        self.frame.draw(surface)

    def runPreviousScene(self):
        SceneManager().setScene(self.previousScene)