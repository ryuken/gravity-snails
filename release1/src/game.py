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
        pygame.init()
        pygame.font.init()
        #D Display
        self.surface = pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT]) #retourneert Surface
        pygame.display.set_caption("Gravity Snails")

        self.input = Input()
        self.blue     = 0, 0, 128
        self.clock     = pygame.time.Clock()
        self.createGameObjects()

    def createGameObjects(self):
        self.teams = []
        #A Assign
        self.terrain = Terrain()
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
        
        while 1:
            #T Timer (framerate)
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.turnManager.timer.cancel()
                    return

            self.terrain.update()
            for team in self.teams:
                team.update(self.input, self.terrain)

            self.bullets.update()

            #R refresh
            self.surface.fill(self.blue)
            self.terrain.draw(self.surface)
            for team in self.teams:
                team.draw(self.surface)
            
            self.bullets.draw(self.surface)
            
            self.turnManager.draw(self.surface)
            
            pygame.display.flip()

game = Game()
game.addTeam('test', 2, Direction.UP)
game.addTeam('test2', 2, Direction.DOWN)
game.run()