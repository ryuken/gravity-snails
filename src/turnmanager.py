import pygame
from pygame.locals import *
from enums import TurnStatus
from settings import Settings
from threading import Timer

class TurnManager(object):
    _instance = None
    _count    = 0
    

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TurnManager, cls).__new__(
                                cls, *args, **kwargs)

#            _count += 1
            print "Created new instance"
        return cls._instance

    def __init__(self):
        # Display some text
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
            self.currentTeamTurn = 0
            self.timer = None
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

    def stopTimer(self):
        self.started = False
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
            elif self.status == TurnStatus.CURRENTTURN:
                self.changeTurn()


    def changeTurn(self):
        self.status = TurnStatus.BREAK
        self.currentTime = self.breakTime
        
        teamIterator = iter(self.teams)
        for team in teamIterator:
            if team.hasTurn:
                team.hasTurn = False
                nextTeam = None
                try:
                    nextTeam = teamIterator.next()
                    if nextTeam:
                        nextTeam.hasTurn = True
                        nextTeam.nextSnailTurn()
                except StopIteration:
                    self.teams[0].hasTurn = True
                    self.teams[0].nextSnailTurn()
                    return