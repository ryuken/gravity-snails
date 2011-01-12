import pygame
from terrain import Terrain

from team import Team
from turnmanager import TurnManager
from settings import Settings

from enums import GameModes

from scenemanager import SceneManager

from scene import Scene
from winscreen import WinScreen

class Game(Scene):

    def __init__(self):
        self.mainmenu = None
        self.winscreen = None
        self.initTerrain()
        self.initTeams()

        self.createGameObjects()

        self.startNewGame()

    def do_action(self, event):
        # check events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    TurnManager().currentTeam.currentSnailWithTurn.shoot()
                if event.key == pygame.K_ESCAPE:
                    SceneManager().setScene(self.mainmenu)

    def clean(self):
        self.turnManager.stopTimer()

    def initTeams(self):
        self.teams = []
        self.teamsAlive = 0

    def initTerrain(self):
        self.terrain = Terrain()

    def createGameObjects(self):
        #A Assign
        self.terrain.create(5)

    def addTeam(self, name, numberOfSnails, gravity_direction):
        team = Team(name)
        team.setGravity(gravity_direction)
        team.addSnails(numberOfSnails)
        team.setTeamImage((gravity_direction+1))
        self.teams.append(team)

    def run(self):
        self.runGame()

    def startNewGame(self):
        for i in range(0, Settings.GAME_PLAYERS):
            self.addTeam('test', Settings.GAME_SNAILS, i)
        self.turnManager = TurnManager()
        self.turnManager.setTeams(self.teams)

        self.gamemode = GameModes.GAME_PLACING_SNAILS

    def stopGame(self):
        self.turnManager.timer.cancel()
        teamColors = {1:'green', 2:'red', 3:'yellow', 4:'blue'}
        livingTeamColor = str(teamColors[self.teams[0].colorIndex])
        SceneManager().setScene(WinScreen(self.mainmenu, livingTeamColor))
        #SceneManager().scene = self.mainmenu

    def update(self, input):
        self.terrain.update()
        self.updateTeams(input)

        self.updateGameMode()

    def updateTeams(self, input):
        self.teamsAlive = 0
        for team in self.teams:
            team.update(input, self.terrain)
            self.teamsAlive += 1

    def updateGameMode(self):
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
        self.terrain.draw(surface)
        for team in self.teams:
            team.draw(surface)

        #self.bullets.draw(surface)
        if self.gamemode == GameModes.GAME_PLAYING:
            self.turnManager.draw(surface)