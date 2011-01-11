import pygame
from pygame.locals import *
from enums import TurnStatus
from settings import Settings
from threading import Timer

class TurnManager(object):
    _instance = None
    _count    = 0
    
    # forcing singleton to always return the instance of the static variable _instance
    def __new__(cls, *args, **kwargs):
        # Check if the instance exists
        if not cls._instance:
            # create a new instance if it didnt exist
            cls._instance = super(TurnManager, cls).__new__(
                                cls, *args, **kwargs)

#            _count += 1
            print "Created new instance"
        # return the class attribute _instance we just maked or we already had
        return cls._instance

    def __init__(self):
        if TurnManager._count == 0:
            self.font_size = Settings.TIMER_FONT_SIZE
            pygame.font.init()
            self.font = pygame.font.Font(None, self.font_size)
            self.startTime = Settings.TIMER_STARTTIME
            self.breakTime = Settings.TIMER_BREAKTIME
            self.currentTime = self.breakTime
            self.position = Settings.TIMER_POSITION
            self.size = Settings.TIMER_SIZE
            self.rect = pygame.Rect(self.position, self.size)
            self.status = TurnStatus.BREAK
            self.teams = None
            self.timer = None
            self.currentTeam = None
            print "Init turnmanager"
            TurnManager._count += 1
    

    def startTimer(self):
        if self.teams is not None:
            self.timer = Timer(1.0, self.updateTime)
            self.timer.start()
        else:
            raise ValueError("Teams must be assigned use TurnManager.setTeams(teams).")

    def setTeams(self, teams):
        self.teams = teams
        self.teams[0].hasTurn = True
        self.currentTeam = self.teams[0]

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
        self.timer = Timer(1.0, self.updateTime)
        self.timer.start()

    def updateStatus(self):
        if self.currentTime == 0:
            if self.status == TurnStatus.BREAK:
                self.status = TurnStatus.CURRENTTURN
                self.currentTime = self.startTime
                self.changeTurn()
            elif self.status == TurnStatus.CURRENTTURN:
                self.stopTurn()
                


    def changeTurn(self):
        
        teamIterator = iter(self.teams)
        for team in teamIterator:
            if team == self.currentTeam:
                team.hasTurn = False
                nextTeam = None
                try:
                    nextTeam = teamIterator.next()
                    if nextTeam:
                        nextTeam.hasTurn = True
                        self.currentTeam = nextTeam
                except StopIteration:
                    self.teams[0].hasTurn = True
                    self.currentTeam = self.teams[0]
                    
                self.changeTurnSnail()
    
    
    def changeTurnSnail(self):
        snailIterator = iter(self.currentTeam.orderedSnailList)

        for snail in snailIterator:
            if snail == self.currentTeam.currentSnailWithTurn:
                snail.hasTurn = False
                nextSnail = None
                try:
                    nextSnail = snailIterator.next()
                    if nextSnail:
                        nextSnail.hasTurn = True
                        self.currentTeam.currentSnailWithTurn = nextSnail
                except StopIteration:
                    nextSnail = self.currentTeam.orderedSnailList[0]
                    nextSnail.hasTurn = True
                    self.currentTeam.currentSnailWithTurn = nextSnail

    def stopTurn(self):
        self.status = TurnStatus.BREAK
        self.currentTime = self.breakTime
        
        self.currentTeam.hasTurn = False
        for team in self.teams:
            team.currentSnailWithTurn.hasTurn = False
            if team.hasTurn:
                raise ValueError('No team should have the turn. See TurnManager.stopturn')
        