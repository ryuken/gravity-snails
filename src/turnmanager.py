import pygame
from enums import TurnStatus
from settings import Settings
from threading import Timer

class TurnManager(object):
    """
    The TurnManager is used to change the turns of the teams
    and of the snails. TurnManager has a timer, which automatically
    changes the turn of the teams/snails when the time is up.
    It also draws a timer.
    """
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
            print("Created new instance")
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
            """ self.rect is a rectangle at the specified pos and size """
            self.rect = pygame.Rect(self.position, self.size)
            self.status = TurnStatus.CURRENTTURN
            self.teams = None
            self.timer = None
            self.currentTeam = None
            print("Init turnmanager")
            TurnManager._count += 1

    def startTimer(self):
        """
        Create a timer and start it
        """
        if self.teams is not None:
            self.timer = Timer(1.0, self.updateTime)
            self.timer.start()
        else:
            raise ValueError("Teams must be assigned use TurnManager.setTeams(teams).")

    def setTeams(self, teams):
        """
        Set the teams and give team 1 the turn

        @param teams The teams to set
        """
        self.teams = teams
        self.teams[0].hasTurn = True
        self.currentTeam = self.teams[0]

    def stopTimer(self):
        """
        Stop the timer when the timer is not None
        """
        if(not None == self.timer):
            self.timer.cancel()

    def draw(self, surface):
        """
        Draw the timer in the game

        @param surface The surface to draw on
        """
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
        """
        Decrease the time every second
        """
        self.updateStatus()
        self.currentTime -= 1
        self.timer = Timer(1.0, self.updateTime)
        self.timer.start()

    def updateStatus(self):
        """
        When the time is at 0
        Stop the turn of the current team/snail
        """
        if self.currentTime == 0:
            self.stopTurn()

    def changeTurn(self):
        """
        Change the turn of the team
        """
        someoneHasTurn = []

        teamIterator = iter(self.teams)
        for team in teamIterator:
            if team.hasTurn == True:
                someoneHasTurn.append(True)

        if len(someoneHasTurn) > 0:
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
                                print(nextTeam.name +" is alive")

                                # when the team is alive give it the turn
                                nextTeam.hasTurn = True
                                print(nextTeam.name + " got turn")

                                self.currentTeam = nextTeam
                        except StopIteration:
                            if len(self.teams) > 0:
                                # set the first team of the list of teams as the next team
                                nextTeam = self.teams[0]
                                # check if this team is alive
                                if nextTeam.isAlive == True:
                                    print(nextTeam.name + " from StopIteration is alive")

                                    # give it the turn
                                    nextTeam.hasTurn = True
                                    print(nextTeam.name + " from StopIteration got the turn")

                                    self.currentTeam = nextTeam
        else:
            # give a team the turn who is alive
            livingTeam = []
            teamIterator = iter(self.teams)
            for team in teamIterator:
                if team.isAlive == True:
                    livingTeam.append(team)

            if len(livingTeam) > 0:
                livingTeam[0].hasTurn = True
                self.currentTeam = livingTeam[0]
                print(livingTeam[0].name + " got turn")
            else:
                print("All teams's are dead")

    def changeTurnSnail(self, team):
        """
        Change the turn of the snail

        @param team The team to change the snail from
        """
        someoneHasTurn = []

        snailIterator = iter(team.orderedSnailList)
        for snail in snailIterator:
            # check if the snail has the turn
            if snail.hasTurn == True:
                someoneHasTurn.append(True)

        if len(someoneHasTurn) > 0:
            snailIterator = iter(team.orderedSnailList)
            for snail in snailIterator:
                if snail.hasTurn == True:
                    print(str(snail.id) + " had turn")
                    snail.hasTurn = False

                    if len(team.orderedSnailList) > 0:
                        nextSnail = None
                        # try to get the next snail
                        try:
                            nextSnail = snailIterator.next()
                            # check if the snail is alive
                            if nextSnail.isAlive == True:
                                print(str(snail.id) + " is alive")
                                # give it the turn
                                nextSnail.hasTurn = True
                                print(str(snail.id) + " got turn")
                        except StopIteration:
                            # set the first team of the list of teams as the next team
                            nextSnail = team.orderedSnailList[0]
                            # check if this team is alive
                            if nextSnail.isAlive == True:
                                print(str(snail.id) + " is alive")
                                # give it the turn
                                nextSnail.hasTurn = True
                                print(str(snail.id) + " got turn")
                    else:
                        print(team.name + " has no snails")
        else:
            # give a snail the turn who is alive
            livingSnail = []

            snailIterator = iter(team.orderedSnailList)
            for snail in snailIterator:
                if snail.isAlive == True:
                    livingSnail.append(snail)

            if len(livingSnail) > 0:
                livingSnail[0].hasTurn = True
                print(str(livingSnail[0].id) + " got turn")
            else:
                print("All snail's of " + team.name + " are dead")
                self.changeTurn()

    def stopTurn(self):
        """
        Stop the turn, means when the status is
        BREAK change it to CURRENTTURN and when
        it is on CURRENTTURN change it to BREAK
        """
        if self.status == TurnStatus.BREAK:
            self.status = TurnStatus.CURRENTTURN
            self.currentTime = self.startTime
            self.changeTurn()
            self.changeTurnSnail(self.currentTeam)
        elif self.status == TurnStatus.CURRENTTURN:
            self.status = TurnStatus.BREAK
            self.currentTime = self.breakTime
