import pygame
from terrain import Terrain
from snail import Snail
from team import Team
from timer import Timer

class Game(object):
    def __init__(self):
        #Init
        pygame.init()
        pygame.font.init()
        #D Display
        self.surface = pygame.display.set_mode([640,640]) #retourneert Surface
        pygame.display.set_caption("Gravity Snails")
        self.teams = []

        #A Assign
        self.terrain = Terrain()
        #snail.rect.move_ip(400, surface.get_height() - snail.rect.height - 100)
#        self.team1.add(self.snail)
        self.timer = Timer(position=(0,0), size=(20,20), startTime="30")
        
        self.blue     = 0, 0, 128
        self.clock     = pygame.time.Clock()
    
    def addTeam(self, name, countSnails):
        team = Team(name)
        for i in range(0, countSnails):
            snail = Snail()
            team.add(snail)
        self.teams.append(team)
    
    def run(self):
        while 1:
            #T Timer (framerate)
            self.clock.tick(90)
        
            #E Event
            for event in pygame.event.get():
                self.timer.update(event)
                if event.type == pygame.QUIT:
                    return
#                if event.type == pygame.MOUSEBUTTONUP:
#                    if (self.snail.isPlaced):
#                        self.snail = Snail(self.terrain)
#                        self.team1.add(self.snail)
                
            self.terrain.update()
            for team in self.teams:
                team.update(self.terrain)
        
            #R refresh
            self.surface.fill(self.blue)
            self.terrain.draw(self.surface)
            for team in self.teams:
                team.draw(self.surface)
            self.timer.draw(self.surface)
            pygame.display.flip()


game = Game()
game.addTeam('test', 3)
game.addTeam('test2', 2)
game.run()