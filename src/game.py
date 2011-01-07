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
        self.mainmenu = None
        self.initTerrain()
        self.initTeams()

        self.createGameObjects()

        self.startNewGame()
    
    def do_action(self, event):
        # check events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for team in self.teams:
                    for snail in team.sprites():
                        if team.hasTurn and snail.hasTurn and TurnManager().status == TurnStatus.CURRENTTURN:
                            team.active_weapon.shoot()
        
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
            self.addTeam('test', Settings.GAME_SNAILS, i)
        self.turnManager = TurnManager()
        self.turnManager.setTeams(self.teams)
        self.turnManager.startTimer()
        
        self.gamemode = GameModes.GAME_PLACING_SNAILS

    def stopGame(self):
        self.turnManager.timer.cancel()
        SceneManager().scene = self.mainmenu

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
        if self.gamemode == GameModes.GAME_PLACING_SNAILS:
            for team in self.teams:
                for snail in team.sprites():
                    if snail.isPlaced == False:
                        return
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