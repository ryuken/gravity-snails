from scene import Scene
from settings import Settings
class Menu(Scene):
    def __init__(self):
        self.options = []
        self.selectedOption = None
        self.size = {'width':128, 'height':32}

    def addOption(self, optionValue):
        option_width = self.size['width']
        option_height = self.size['height']
        option_space = 2

        #(re-)calcluate rectangle size
        for i in range(0, len(self.options)):
            #print 'option_width: ' + str(option_width)
            #print "width of rectange [" + str(i) + "] = " + str(self.options[i].rect.width)
            if(option_width < self.options[i].rect.width):
                option_width = self.options[i].rect.width
            if(option_height < self.options[i].rect.height):
                option_height = self.options[i].rect.height

        self.size['width'] = option_width
        self.size['height'] = option_height

        optionValue.rect.width = option_width
        optionValue.rect.height = option_height
        optionValue.rect.centerx = (Settings.SCREEN_WIDTH / 2)

        self.options.append(optionValue)

        menu_height = option_height * len(self.options)

        for i in range(0, len(self.options)):
            screen_center = Settings.SCREEN_HEIGHT / 2
            menu_top = (screen_center - (menu_height / 2))
            option_y = ((option_height + option_space) * i)
            self.options[i].rect.width = option_width
            self.options[i].rect.height = option_height
            self.options[i].rect.top = menu_top + option_y

    def update(self, input):
        for option in self.options:
            option.update(input)

    def draw(self, surface):
        for option in self.options:
            option.draw(surface)