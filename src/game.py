import pygame
from terrain import Terrain

from team import Team
from turnmanager import TurnManager
from settings import Settings

from enums import GameModes, TurnStatus

from gui.button import Button
from gui.slider import Slider

from scenemanager import SceneManager

from scene import Scene
class Game(Scene):

    def __init__(self):
        self.initTerrain()
        self.initTeams()

        self.createGameObjects()

        self.startNewGame()

    def clean(self):
        self.turnManager.timer.cancel()

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
            self.addTeam('test', 2, i)

        self.turnManager = TurnManager()
        self.turnManager.setTeams(self.teams)
        self.turnManager.startTimer()

    def stopGame(self):
        self.turnManager.timer.cancel()
        self.gamemode = GameModes.MENU_MAIN

    def update(self, input):
        self.terrain.update()
        self.updateTeams(input)

        self.updateGameMode()

    def updateTeams(self, input):
        self.teamsAlive = 0
        for team in self.teams:
            if team.isAlive():
                team.update(input, self.terrain)
                self.teamsAlive += 1

    def updateGameMode(self):
        if SceneManager().gamemode == GameModes.GAME_PLACING_SNAILS:
            for team in self.teams:
                for snail in team.sprites():
                    if snail.isPlaced == False:
                        return
            SceneManager().gamemode = GameModes.GAME_PLAYING
        if SceneManager().gamemode == GameModes.GAME_PLAYING:
            if self.teamsAlive <= 1:
                self.running = False

    def draw(self, surface):
        self.terrain.draw(surface)
        for team in self.teams:
            team.draw(surface)

        #self.bullets.draw(surface)
        if SceneManager().gamemode == GameModes.GAME_PLAYING:
            self.drawTimer(surface)

    def drawTimer(self):
        self.turnManager.draw(self.surface)