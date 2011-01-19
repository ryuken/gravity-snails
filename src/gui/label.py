import pygame
from pygame.locals import *
from input import Input
class Label(object):
    """
    The label class displays some text on the screen
    """
    def __init__(self, text):
        """
        Initializes a label
        @param text: The text that should be showed on the label
        """
        self.font_size = 25
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = None #pygame.Rect(0,0,1,1)
        self.text = text
        textSurface = self.font.render(str(self.text), 1, (10, 10, 10)) #returns surface
        #print 'label size before resizing: ('+str(self.rect.width)+', ' +str(self.rect.height)+ ')'
        self.rect = pygame.Rect(0,0,1,1)
        self.rect.width, self.rect.height = self.calc_size()
        self.centerLines = True

    def calc_size(self):
        """
        Calculates the size of the label
        """
        lines = self.text.split("\n")
        width = 0
        height = 0
        for line in lines:
            lineSurface = self.font.render(line, 1, (255, 255, 255)) #returns surface
            height += lineSurface.get_height()
            if lineSurface.get_width() > width:
                width = lineSurface.get_width()
        return (width, height)

    def update(self, input):
        """
        Updates the label
        @param input: The input class
        """
        pass

    def draw(self, surface):
        """
        Draws the label
        @param surface: The surface the label should be drawed on
        """
        # Create a new surface at the position of the red rectangle and draw the text
        lines = self.text.split("\n")
        y = self.rect.top
        for line in lines:
            lineSurface = self.font.render(line, 1, (255, 255, 255)) #returns surface
            if self.centerLines:
                surface.blit(lineSurface, (self.rect.centerx - (lineSurface.get_width() / 2), y))
            else:
                surface.blit(lineSurface, (self.rect.centerx - (lineSurface.get_width() / 2), y))
            y += lineSurface.get_height()