import pygame
from terrain import Terrain
from snail import Snail
from team import Team
from timer import Timer
from settings import Settings
from salt import Salt
from input import Input
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
        #snail.rect.move_ip(400, surface.get_height() - snail.rect.height - 100)
#        self.team1.add(self.snail)

        self.bullets = pygame.sprite.Group()

    def addTeam(self, name, countSnails):
        team = Team(name)
        for i in range(0, countSnails):
            snail = Snail(team)
            snail.id = i
            if i == 1:
                snail.hasTurn = True
            team.add(snail)
        self.teams.append(team)

    def addBullet(self, bullet):
        self.bullets.add(bullet)

    def run(self):
        self.timer = Timer(position=(0,0), size=(20,20), startTime="5", teams=self.teams)

        while 1:
            #T Timer (framerate)
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                self.timer.update(event)
                for team in self.teams:
                    team.updateEvent(event)
                if event.type == pygame.QUIT:
                    return
#                if event.type == pygame.MOUSEBUTTONUP:
#                    if (self.snail.isPlaced):
#                        self.snail = Snail(self.terrain)
#                        self.team1.add(self.snail)

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
            #self.salt.draw(self.surface)
            self.timer.draw(self.surface)
            
            pygame.display.flip()

game = Game()
game.addTeam('test', 2)
game.addTeam('test2', 2)
game.run()