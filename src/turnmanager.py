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
            self.font_timer = pygame.font.Font(None, self.font_size)
            self.font_break = pygame.font.Font(None, 50)
            self.startTime = Settings.TIMER_STARTTIME
            self.breakTime = Settings.TIMER_BREAKTIME
            self.currentTime = self.breakTime
            self.position = Settings.TIMER_POSITION
            self.size = Settings.TIMER_SIZE
            self.rect = pygame.Rect(self.position, self.size)
            self.status = TurnStatus.CURRENTTURN
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
        #self.currentTeam = self.teams[0]

    def stopTimer(self):
        self.timer.cancel()

    def draw(self, surface):
        # Draw the red rectangle on the game surface
        self.rect = surface.fill((255,0,0), self.rect)
        surface.blit(surface, self.position)
        # Create a new surface at the position of the red rectangle and draw the text
        text_timer = self.font_timer.render(str(self.currentTime), 1, (10, 10, 10)) #returns surface
        surface.blit(text_timer, (Settings.TIMER_SIZE[0] / 2 - 7, Settings.TIMER_SIZE[1] / 2 - 7))

        if self.status == TurnStatus.BREAK:
            # Create a new surface in the middle of the screen and draw the text: Breaktime
            text_break = self.font_break.render("Next player, be ready!", 1, (255, 0, 0)) #returns surface
            surface.blit(text_break, (Settings.SCREEN_WIDTH / 2 - text_break.get_width()/2, Settings.SCREEN_HEIGHT / 2 - 50))

    def updateTime(self):
        self.updateStatus()
        self.currentTime -= 1
        self.timer = Timer(1.0, self.updateTime)
        self.timer.start()

    def updateStatus(self):
        if self.currentTime == 0:
            self.stopTurn()

    def changeTurn(self):
        teamIterator = iter(self.teams)
        for team in teamIterator:
            # check if the team has the turn
            if team.hasTurn == True:
                team.hasTurn = False
                
                if len(self.teams) > 0:
                    nextTeam = None
                    # try to get the next team
                    try:
                        nextTeam = teamIterator.next()
                        # check if the team is alive
                        if nextTeam.isAlive == True:
                            print nextTeam.name +" is alive"
                            
                            # when the team is alive give it the turn
                            nextTeam.hasTurn = True
                            print nextTeam.name + " got turn"
                            
                            self.currentTeam = nextTeam
                        else:
                            # recursion
                            self.changeTurn()
                    except StopIteration:
                        if len(self.teams) > 0:
                            # set the first team of the list of teams as the next team 
                            nextTeam = self.teams[0]
                            # check if this team is alive
                            if nextTeam.isAlive == True:
                                print nextTeam.name + " from StopIteration is alive"
                                
                                # give it the turn
                                nextTeam.hasTurn = True
                                print nextTeam.name + " from StopIteration got the turn"
                                
                                self.currentTeam = nextTeam
                            else:
                                # recursion
                                self.changeTurn()

    def changeTurnSnail(self, team):
        snailIterator = iter(team.orderedSnailList)

        for snail in snailIterator:
            # check if the snail has the turn
            if snail.hasTurn == True:
                snail.hasTurn = False
                
                if len(team.orderedSnailList) > 0:        
                    if snail.isAlive == False:
                        team.orderedSnailList.remove(snail)
                        snail.kill()
                    
                    nextSnail = None
                    # try to get the next snail
                    try:
                        nextSnail = snailIterator.next()
                        # check if the snail is alive
                        if nextSnail.isAlive == True:
                            # give it the turn
                            nextSnail.hasTurn = True
                        else:
                            # remove the snail from the ordered list of snails
                            team.orderedSnailList.remove(nextSnail)
                            nextSnail.kill()
                            # recursion
                            self.changeTurnSnail(team)
                    except StopIteration:
                        if len(team.orderedSnailList) > 0:
                            # set the first team of the list of teams as the next team 
                            nextSnail = team.orderedSnailList[0]
                            # check if this team is alive
                            if nextSnail.isAlive == True:
                                # give it the turn
                                nextSnail.hasTurn = True
                            else:
                                # remove it from the list of teams
                                team.orderedSnailList.remove(nextSnail)
                                nextSnail.kill()
                                # recursion
                                self.changeTurnSnail(team)
                    
    def stopTurn(self):
        if self.status == TurnStatus.BREAK:
            self.status = TurnStatus.CURRENTTURN
            self.currentTime = self.startTime
            self.changeTurn()
            self.changeTurnSnail(self.currentTeam)
        elif self.status == TurnStatus.CURRENTTURN:
            self.status = TurnStatus.BREAK
            self.currentTime = self.breakTime