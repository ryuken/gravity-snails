import pygame
from pygame.locals import *

class Timer(object):
    def __init__(self, startTime=30):
        # Display some text
        self.font = pygame.font.Font(None, 16)
        self.startTime = startTime
        
        #Why +1???
        pygame.time.set_timer(USEREVENT+1, 1000)
    
    def drawTimeLeft(self, event, surface):
        if event.type == USEREVENT+1:
            text = self.font.render(self.startTime, 1, (10, 10, 10))
            text.fill((255,0,0))
            surface.blit(text, (0, 0))
            text = self.font.render(self.startTime, 1, (10, 10, 10))
            surface.blit(text, (0, 0))
            self.startTime -= 1