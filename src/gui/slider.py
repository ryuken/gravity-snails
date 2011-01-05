import pygame
from pygame.locals import *
from input import Input
class Slider(object):
    
    def __init__(self, position, min, max, value):
        self.font_size = 25
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = pygame.Rect(position[0], position[1], 128, 32)
        self.min = min
        self.max = max
        self.value = value
    def update(self, input):
        if input.mouse_left:
            if self.rect.collidepoint(input.mouse_x, input.mouse_y):
                self.value = int(float(input.mouse_x - self.rect.left) / self.rect.width * (self.max - self.min) + 0.5) + self.min
    
    def draw(self, surface):
        # Draw the red rectangle on the game surface
        #self.rect = surface.fill((0,0,0), self.rect)
        pygame.draw.rect(surface, (0,0,255), pygame.Rect(self.rect.left, self.rect.top + 8,self.rect.width, 16))
        position = ((self.rect.width / float(self.max - self.min)) * (self.value - self.min)) + self.rect.left
        pygame.draw.rect(surface, (0,255,255), pygame.Rect(position - 4, self.rect.top, 8, self.rect.height))
        surface.blit(surface, (0,0))
        # Create a new surface at the position of the red rectangle and draw the text
        text = self.font.render(str(self.value), 1, (10, 10, 10)) #returns surface
        surface.blit(text, (self.rect.left, self.rect.centery - (text.get_height() / 2)))
    