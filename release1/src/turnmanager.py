import pygame
from pygame.locals import *
from enums import TurnStatus
from settings import Settings
from threading import Timer

class TurnManager(object):
    def __init__(self, teams):
        # Display some text
        pygame.font.init()
        self.font_size = Settings.TIMER_FONT_SIZE
        self.font = pygame.font.Font(None, self.font_size)
        self.startTime = Settings.TIMER_STARTTIME
        self.breakTime = Settings.TIMER_BREAKTIME
        self.currentTime = self.breakTime
        self.position = Settings.TIMER_POSITION
        self.size = Settings.TIMER_SIZE
        self.rect = pygame.Rect(self.position, self.size)
        self.status = TurnStatus.BREAK
        self.teams = teams
        self.currentTeamTurn = 0
        self.teams[0].hasTurn = True
        self.timer = Timer(1.0, self.updateTime)
        
    def startTimer(self):
        self.timer.start()
        
    def stopTimer(self):
        self.timer.cancel()
    
    def draw(self, surface):
        # Draw the red rectangle on the game surface
        self.rect = surface.fill((255,0,0), self.rect)
        surface.blit(surface, self.position)
        # Create a new surface at the position of the red rectangle and draw the text
        text = self.font.render(str(self.currentTime), 1, (10, 10, 10)) #returns surface
        surface.blit(text, (Settings.TIMER_SIZE[0] / 2 - 7, Settings.TIMER_SIZE[1] / 2 - 7))
           
    def updateTime(self):
        self.updateStatus()
        self.currentTime -= 1
    
    def updateStatus(self):
        if self.currentTime == 0:
            if self.status == TurnStatus.BREAK:
                self.status = TurnStatus.CURRENTTURN
                self.currentTime = self.startTime
            elif self.status == TurnStatus.CURRENTTURN:
                self.status = TurnStatus.BREAK
                self.currentTime = self.breakTime
                self.changeTurn()
        self.timer = Timer(1.0, self.updateTime)
        self.timer.start()
                
    def changeTurn(self):
        #give the turn to the next team and set the current team on false
        if self.teams[self.currentTeamTurn].hasTurn == True:
            self.teams[self.currentTeamTurn].hasTurn = False
            
            nextTeam = self.currentTeamTurn + 1
            if nextTeam < len(self.teams):
                self.currentTeamTurn = nextTeam
                self.teams[nextTeam].hasTurn = True
                self.teams[nextTeam].nextSnailTurn()
            else:
                self.currentTeamTurn = 0
                self.teams[0].hasTurn = True
                self.teams[0].nextSnailTurn()