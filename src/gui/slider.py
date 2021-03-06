import pygame
from pygame.locals import *
from input import Input
class Slider(object):
    """
    The slider class makes it possible to let the user set a value through a slider
    """
    def __init__(self, min, max, value, text = "", step = 1):
        """
        Initializes the slider
        @param min: The minimum value of the slider
        @param max: The maximum value of the slider
        @param value: The default value of the slider
        @param text: The text that should be showed on the slider
        @param step: The steps the slider should take. For example if step=10, the slider would only go 10, 20, 30, etc
        """
        self.font_size = 25
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = pygame.Rect(0,0,1,1)
        self.text = text
        self.min = min
        self.max = max
        self.value = value
        self.step = step
        self.pressed = False
        
    def update(self, input):
        """
        Updates the slider
        @param input: The input class
        """
        if input.get_mouse_left_click(self.rect):
            self.pressed = True
        if self.pressed:
            if input.mouse_left:
                self.value = int(float(input.mouse_x - self.rect.left) / self.rect.width * (self.max - self.min) + 0.5) + self.min
                self.value = int(self.value / self.step) * self.step
                self.value = max([min([self.value, self.max]), self.min])
            else:
                self.pressed = False
    
    def draw(self, surface):
        """
        Draws the slider on the surface
        @param surface: The surface the slider should be drawed on
        """
        # Draw the red rectangle on the game surface
        #self.rect = surface.fill((0,0,0), self.rect)
        pygame.draw.rect(surface, (0,0,255), pygame.Rect(self.rect.left, self.rect.top + 8,self.rect.width, 16))
        position = ((self.rect.width / float(self.max - self.min)) * (self.value - self.min)) + self.rect.left
        pygame.draw.rect(surface, (0,255,255), pygame.Rect(position - 4, self.rect.top, 8, self.rect.height))
        surface.blit(surface, (0,0))
        # Create a new surface at the position of the red rectangle and draw the text
        text = self.font.render(self.text + str(self.value), 1, (10, 10, 10))
        surface.blit(text, (self.rect.left, self.rect.centery - (text.get_height() / 2)))
    