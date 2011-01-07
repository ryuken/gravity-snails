from scene import Scene
from settings import Settings
class Menu(Scene):
    def __init__(self):
        self.options = []
        self.selectedOption = None

    def addOption(self, optionValue):
        option_width = 128
        option_height = 32
        option_space = 16
        
        optionValue.rect.width = option_width
        optionValue.rect.height = option_height
        optionValue.rect.centerx = (Settings.SCREEN_WIDTH / 2)
        
        self.options.append(optionValue)
        
        menu_height = option_height * len(self.options)
        print menu_height
        for i in range(0, len(self.options)):
            screen_center = Settings.SCREEN_HEIGHT / 2
            menu_top = (screen_center - (menu_height / 2))
            option_y = (option_height * i)
            self.options[i].rect.top = menu_top + option_y

    def update(self, input):
        for option in self.options:
            option.update(input)

    def draw(self, surface):
        for option in self.options:
            option.draw(surface)