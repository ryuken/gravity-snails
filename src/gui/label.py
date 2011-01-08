import pygame
from pygame.locals import *
from input import Input
class Label(object):

    def __init__(self, text):
        self.font_size = 25
        self.font = pygame.font.Font(None, self.font_size)
        self.rect = None #pygame.Rect(0,0,1,1)
        self.text = text
        textSurface = self.font.render(str(self.text), 1, (10, 10, 10)) #returns surface
        #print 'label size before resizing: ('+str(self.rect.width)+', ' +str(self.rect.height)+ ')'
        self.rect = pygame.Rect(0,0,1,1)
        self.rect.width = textSurface.get_width()
        self.rect.height = textSurface.get_height()

    def update(self, input):
        pass

    def draw(self, surface):
        # Draw the red rectangle on the game surface
        #surface.fill((255,0,0), self.rect)
        surface.blit(surface, (0,0))
        # Create a new surface at the position of the red rectangle and draw the text
        textSurface = self.font.render(str(self.text), 1, (255, 255, 255)) #returns surface
        surface.blit(textSurface, (self.rect.centerx - (textSurface.get_width() / 2), self.rect.centery - (textSurface.get_height() / 2)))

    def do_action(self):
        pass