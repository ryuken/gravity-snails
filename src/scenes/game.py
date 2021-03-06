import pygame
from terrain import Terrain

from team import Team
from turnmanager import TurnManager
from settings import Settings

from enums import GameModes

from scenes.scenemanager import SceneManager

from scenes.scene import Scene
from scenes.winscreen import WinScreen

class Game(Scene):
    """
    This is the game class, this is the most important scene, and keeps track of the whole game
    """
    def __init__(self):
        """ Initializes the game scene """
        self.mainmenu = None
        self.winscreen = None
        self.initEvents()
        self.initTerrain()
        self.initTeams()

        self.createGameObjects()

        self.startNewGame()

    def initEvents(self):
        """ Initializes the eventreader """
        SceneManager().registerEventReader(self.do_action)

    def do_action(self, event):
        """
        Check the events, and do something when needed
        @param event: The event
        """
        
        # check events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for snail in TurnManager().currentTeam.orderedSnailList:
                    if snail.hasTurn:
                        snail.shoot()
            if event.key == pygame.K_ESCAPE:
                SceneManager().setScene(self.mainmenu)
    def clean(self):
        """ Clean everything up, so that application doesn't crash """
        self.turnManager.stopTimer()
        SceneManager().unregisterEventReader(self.do_action)

    def initTeams(self):
        """ Initializes the team """
        self.teams = []
        self.teamsAlive = 0

    def initTerrain(self):
        """ Initializes the terrain """
        self.terrain = Terrain()

    def createGameObjects(self):
        """ Create the terrain """
        self.terrain.create(15)

    def addTeam(self, name, numberOfSnails, gravity_direction):
        """
        Add a team to the game
        @param name: The name of the team
        @param numberOfSnails: The amount of snails the team has
        @param gravity_direction: The gravity direction of the team
        """
        team = Team(name)
        team.setGravity(gravity_direction)
        team.addSnails(numberOfSnails)
        team.setTeamImage((gravity_direction+1))
        self.teams.append(team)
        
    def startNewGame(self):
        """ Start a new game """
        for i in range(0, Settings.GAME_PLAYERS):
            self.addTeam('team '+str(i+1), Settings.GAME_SNAILS, i)
        self.turnManager = TurnManager()
        self.turnManager.setTeams(self.teams)

        self.gamemode = GameModes.GAME_PLACING_SNAILS

    def stopGame(self):
        """ Stop the game """
        self.turnManager.timer.cancel()
        teamColors = {1:'green', 2:'red', 3:'yellow', 4:'blue'}
        livingTeamColor = str(teamColors[self.teams[0].colorIndex])
        SceneManager().setScene(WinScreen(self.mainmenu, livingTeamColor))
        #SceneManager().scene = self.mainmenu

    def update(self, input):
        """
        Update the game
        @param input: The input class
        """
        self.terrain.update()
        self.updateTeams(input)

        self.updateGameMode()

    def updateTeams(self, input):
        """
        Update every team
        @param input: The input class
        """
        self.teamsAlive = 0
        for team in self.teams:
            team.update(input, self.terrain)
            self.teamsAlive += 1

    def updateGameMode(self):
        """ Update the gamemodes """
        if self.gamemode == GameModes.GAME_PLACING_SNAILS:
            for team in self.teams:
                for snail in team.sprites():
                    if snail.isPlaced == False:
                        return
            self.turnManager.startTimer()
            self.gamemode = GameModes.GAME_PLAYING
        if self.gamemode == GameModes.GAME_PLAYING:
            if self.teamsAlive <= 1:
                self.stopGame()

    def draw(self, surface):
        """
        Draw the game on a surface
        @param surface: The surface the game should be drawed on
        """
        self.terrain.draw(surface)
        for team in self.teams:
            team.draw(surface)

        #self.bullets.draw(surface)
        if self.gamemode == GameModes.GAME_PLAYING:
            self.turnManager.draw(surface)