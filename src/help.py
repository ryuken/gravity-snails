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
        text += "Use the left mouse button to place snails in the screen\n"
        text += "Use the arrow keys to move and to target\n"
        text += "Use the space bar to fire the weapon\n"
        text += "\n"
        text += "You can shoot the snail's and the terrain beneath them\n"
        text += "Snails die if they touch the salt or when they'r hitpoint's are 0\n"
        text += "So shoot the ground under them away!\n"
        labelText = Label(text)
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