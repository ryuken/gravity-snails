from scenes.scenemanager import SceneManager
from gui.button import Button
from gui.label import Label
from scenes.scene import Scene
from gui.frame import Frame

class HelpMenu(Scene):
    """
    @ivar previousScene: The scene which should come after this help
    """
    def __init__(self, previousScene):
        """
        @param previousScene: The scene which should come after this help
        @summary: Initializes a help frame
        """
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
        """
        @param input: The user input
        @summary: updates the status of the help frame based on the user input
        """
        self.frame.update(input)

    def draw(self, surface):
        """
        @param surface: The surface which the help should be drawed on
        @summary: draws the help frame on a specified surface
        """
        self.frame.draw(surface)

    def runPreviousScene(self):
        """
        @summary: closes the help frame and tells sceneManager to go to previous scene
        """
        SceneManager().setScene(self.previousScene)