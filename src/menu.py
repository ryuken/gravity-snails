from gui.frame import Frame
from settings import Settings
class Menu(Frame):
    def __init__(self):
        Frame.__init__(self)

    def addWidget(self, optionValue):
        widget_width = 128
        widget_height = 32
        widget_space = 2

        #(re-)calcluate rectangle size
        for i in range(0, len(self.widgets)):
            #print 'option_width: ' + str(option_width)
            #print "width of rectange [" + str(i) + "] = " + str(self.options[i].rect.width)
            if(widget_width < self.widgets[i].rect.width):
                widget_width = self.widgets[i].rect.width
            if(widget_height < self.widgets[i].rect.height):
                widget_height = self.widgets[i].rect.height

        optionValue.rect.width = widget_width
        optionValue.rect.height = widget_height
        optionValue.rect.centerx = (self.rect.width / 2)

        Frame.addWidget(self, optionValue)

        menu_height = widget_height * len(self.widgets)

        for i in range(0, len(self.widgets)):
            screen_center = self.rect.height / 2
            menu_top = (screen_center - (menu_height / 2))
            option_y = ((widget_height + widget_space) * i)
            self.widgets[i].rect.width = widget_width
            self.widgets[i].rect.height = widget_height
            self.widgets[i].rect.top = menu_top + option_y