import pygame
from pygame.locals import *
from enums import TurnStatus


class Timer(object):
    def __init__(self, position, size, startTime="30", breakTime="3", teams=None):
        # Display some text
        self.font = pygame.font.Font(None, 16)
        self.startTime = startTime
        self.breakTime = breakTime
        self.currentTime = breakTime
        self.position = position
        self.size = size
        self.rect = pygame.Rect(self.position, self.size )
        self.status = TurnStatus.BREAK
        self.teams = teams
        self.teams[0].hasTurn = True
        
        #Why +1???
        pygame.time.set_timer(USEREVENT, 1000)
    
    def draw(self, surface):
        # Draw the red rectangle on the game surface
        self.rect = surface.fill((255,0,0), self.rect)
        surface.blit(surface, self.position)
        # Create a new surface at the position of the red rectangle and draw the text
        text = self.font.render(self.currentTime, 1, (10, 10, 10)) #returns surface
        surface.blit(text, self.position)
    
    def update(self, event):
        if event.type == USEREVENT:
            if self.status == TurnStatus.CURRENTTURN:
                self.currentTime = str(int(self.currentTime) - 1)
                # if the time hits 0 end the turn 
                # and give the turn to the next player
                # then start the break
                if self.currentTime == "0":
                    maxTeamNumber = len(self.teams)
                    # give the turn to the next team and set the current team on false
                    for i in range(0, maxTeamNumber):
                        # check which team hsa the turn
                        if self.teams[i].hasTurn:
                            # set the currentTeam on false
                            self.teams[i].hasTurn = False
                            if i+1 < maxTeamNumber:
                                # give the turn to the next Team
                                self.teams[(i+1)].hasTurn = True
                            else:
                                # give the turn to the first Team in the list
                                self.teams[0].hasTurn = True
                    self.status = TurnStatus.BREAK
                    self.currentTime = self.breakTime
            # Check the status
            if self.status == TurnStatus.BREAK:
                self.currentTime = str(int(self.currentTime) - 1)
                if self.currentTime == "0":
                    self.status = TurnStatus.CURRENTTURN
                    self.currentTime = self.startTime
                