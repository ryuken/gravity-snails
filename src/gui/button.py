import pygame
from pygame.locals import *
from input import Input
from utils import load_sound
class Button(object):
    """
    @ivar font_size: The font size
    @ivar font: The font
    @ivar rect: The size of the button
    @ivar text: The text that should be showed on the button
    @ivar callback: This function will be called when someone clicks the button
    """

    def __init__(self, text, callback, *args):
        """
        @param text: The text that should be showed on the button
        @param callback: This function will be called when someone clicks the button
        @param args: The parameters for the callback
        @summary: Initializes a button
        """
        self.font_size = 25
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = pygame.Rect(0,0,1,1)
        self.text = text
        self.callback = callback
        self.pressed = False
        self.args = None
        self.button_sound = load_sound("button.ogg")
        argSize = len(args)
        if(0 < argSize):
            self.args = args
        self.button_sound = load_sound("button.ogg")
    def update(self, input):
        """
        @param input: The input class
        @summary: Updates the button
        """
        if input.get_mouse_left_click(self.rect):
            self.pressed = True
            self.button_sound.play()
        if self.pressed:
            if not input.mouse_left:
                self.pressed = False
                if(not None == self.args):
                    self.callback(self.args)
                else:
                    self.callback()

    def draw(self, surface):
        """
        @param surface: The surface the button should be drawed on
        @summary: Draws the button
        """
        if self.pressed:
            self.rect = surface.fill((128,0,0), self.rect)
        else:
            self.rect = surface.fill((255,0,0), self.rect)
        surface.blit(surface, (0,0))
        # Create a new surface at the position of the red rectangle and draw the text
        text = self.font.render(str(self.text), 1, (10, 10, 10)) #returns surface
        surface.blit(text, (self.rect.centerx - (text.get_width() / 2), self.rect.centery - (text.get_height() / 2)))
