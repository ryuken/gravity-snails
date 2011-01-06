from scene import Scene
class Menu(Scene):
    def __init__(self):
        self.options = []
        self.selectedOption = None

    def addOption(self, optionValue):
        self.options.append(optionValue)

    def update(self, input):
        for option in self.options:
            option.update(input)

    def draw(self, surface):
        for option in self.options:
            option.draw(surface)