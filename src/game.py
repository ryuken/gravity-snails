import pygame
from terrain import Terrain

from team import Team
from turnmanager import TurnManager
from settings import Settings

from input import Input
from enums import Direction

class Game(object):
    
    def __init__(self):
        #Init
        self.initPygame()
        #D Display
        self.initScreen()
        self.initInput()
        self.initClock()
        
        self.initTerrain()
        self.initTeams()
        
        self.createGameObjects()
    
        self.running = False

    def initPygame(self):
        result = pygame.init()
        return result[1]
        
    def initScreen(self):
        self.surface = pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT]) #retourneert Surface
        pygame.display.set_caption(Settings.GAME_TITLE)
    
    def initInput(self):
        self.input = Input()
        
    def initClock(self):
        self.clock     = pygame.time.Clock()
        
    def initTeams(self):
        self.teams = []
        self.teamsAlive = 0
        
    def initTerrain(self):
        self.terrain = Terrain()
        
    def createGameObjects(self):
        #A Assign
        self.terrain.create(5)
        self.bullets = pygame.sprite.Group()

    def addTeam(self, name, numberOfSnails, gravity_direction):
        team = Team(name)
        team.setGravity(gravity_direction)
        team.addSnails(numberOfSnails)
        self.teams.append(team)

    def addBullet(self, bullet):
        self.bullets.add(bullet)

    def run(self):
        self.turnManager = TurnManager(self.teams)
        self.turnManager.startTimer()
        
        self.running = True
        while self.running:
            #T Timer (framerate)
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.turnManager.timer.cancel()
                    return

            self.terrain.update()
            self.updateTeams()

            self.bullets.update()

            self.updateGameMode()
            #R refresh
            self.surface.fill(Settings.SCREEN_COLOR)
            self.terrain.draw(self.surface)
            for team in self.teams:
                team.draw(self.surface)
            
            self.bullets.draw(self.surface)
            
            self.turnManager.draw(self.surface)
            
            pygame.display.flip()
        self.turnManager.timer.cancel()
        
    def updateTeams(self):
        self.teamsAlive = 0
        for team in self.teams:
            if team.isAlive():
                team.update(self.input, self.terrain)
                self.teamsAlive += 1
    
    def updateGameMode(self):
        if self.teamsAlive <= 1:
            self.running = False