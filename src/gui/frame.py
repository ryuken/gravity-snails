import pygame
from pygame.locals import *
from settings import Settings
class Frame(object):
    def __init__(self):
        """
        Initializes a frame
        """
        self.widgets = []
        self.rect = Rect(32, 32, Settings.SCREEN_WIDTH - 64, Settings.SCREEN_HEIGHT - 64)
        self.visible = True

    def addWidget(self, widget):
        """
        Adds a widget to the frame
        @param widget: The widget that should be added
        """ 
        self.widgets.append(widget)

    def update(self, input):
        """
        Updates the frame
        @param input: The input class
        """
        if(not self.visible):
            return
        localInput = input.copy()
        localInput.mouse_x -= self.rect.left
        localInput.mouse_y -= self.rect.top
        for widget in self.widgets:
            widget.update(localInput)

    def draw(self, surface):
        """
        Draws the frame
        @param surface: The surface the frame should be drawed on
        """
        if(not self.visible):
            return
        frameSurface = pygame.Surface((self.rect.width,self.rect.height))
        frameSurface.fill((0,0,128))
        for widget in self.widgets:
            widget.draw(frameSurface)
        surface.blit(frameSurface, self.rect)