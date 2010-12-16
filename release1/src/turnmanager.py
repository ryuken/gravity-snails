import pygame
from pygame.locals import *
from enums import TurnStatus
from settings import Settings
from threading import Timer

class TurnManager(object):
    def __init__(self, teams=None):
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
        maxTeamNumber = len(self.teams)
        #give the turn to the next team and set the current team on false
        for i in range(0, maxTeamNumber):
            #check which team has the turn
            if self.teams[i].hasTurn:

                # set the currentTeam on false
                self.teams[i].hasTurn = False
                if i+1 < maxTeamNumber:
                #    give the turn to the next Team
                    self.teams[(i+1)].hasTurn = True
                else:
                #    give the turn to the first Team in the list
                    self.teams[0].hasTurn = True
                    
                # set the next snail in the team to have the turn
                snails_iter = iter(self.teams[i])
                print [snail.hasTurn for snail in snails_iter]
                currentTurn = -1
                print currentTurn
                #loop through all the snails
                for snail in self.teams[i]: 
                    #check if the current snail has the turn
                    if snail.hasTurn == True:
                        snail.hasTurn = False
                        currentTurn = snail.id
                        if currentTurn + 1 < len(self.teams[i]):
                            currentTurn += 1
                        else:
                            currentTurn = 0
                
                for snail in self.teams[i]:
                    if snail.id == currentTurn:
                        snail.hasTurn = True
                
                print currentTurn