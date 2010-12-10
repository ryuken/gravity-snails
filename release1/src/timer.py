import pygame
from pygame.locals import *

class TimerStatus(object):
    BREAK = 1
    CURRENTTURN = 2

class Timer(object):
    def __init__(self, position, size, startTime="30", breakTime="3"):
        # Display some text
        self.font = pygame.font.Font(None, 16)
        self.startTime = startTime
        self.breakTime = breakTime
        self.currentTime = breakTime
        self.position = position
        self.size = size
        self.rect = pygame.Rect(self.position, self.size )
        self.status = TimerStatus.BREAK
        
        #Why +1???
        pygame.time.set_timer(USEREVENT+1, 1000)
    
    def draw(self, surface):
        self.rect = surface.fill((255,0,0), self.rect)
        surface.blit(surface, self.position)
        text = self.font.render(self.currentTime, 1, (10, 10, 10))
        surface.blit(text, self.position)
    
    def update(self, event):
        if event.type == USEREVENT+1:
            if self.status == TimerStatus.CURRENTTURN:
                self.currentTime = str(int(self.currentTime) - 1)
                print "Go to next turn"
                if self.currentTime == "0":
                    self.status = TimerStatus.BREAK
                    self.currentTime = self.breakTime
            # Check the status
            if self.status == TimerStatus.BREAK:
                self.currentTime = str(int(self.currentTime) - 1)
                if self.currentTime == "0":
                    self.status = TimerStatus.CURRENTTURN
                    self.currentTime = self.startTime
                