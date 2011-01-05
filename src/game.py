import pygame
from terrain import Terrain

from team import Team
from turnmanager import TurnManager
from settings import Settings

from input import Input
from enums import GameModes, TurnStatus

from gui.button import Button
from gui.slider import Slider

class Game(object):

    def __init__(self):
        self.gamemode = GameModes.INIT
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
        self.clock = pygame.time.Clock()

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
        self.runMainMenu()
        self.turnManager.timer.cancel()
            
    def runMainMenu(self):
        self.gamemode = GameModes.MENU_MAIN
        
        self.buttonStart = Button(pygame.Rect(32,32,128,32), "Start")
        self.buttonStart.register_action(self.runGame)
        self.buttonSettings = Button(pygame.Rect(32,96,128,32), "Settings")
        self.buttonSettings.register_action(self.runSettingsMenu)
        
        while self.gamemode == GameModes.MENU_MAIN:
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            self.buttonStart.update(self.input)
            self.buttonSettings.update(self.input)
            
            self.surface.fill(Settings.SCREEN_COLOR)
            self.buttonStart.draw(self.surface)
            self.buttonSettings.draw(self.surface)
            pygame.display.flip()
    
    def applySettings(self):
        Settings.GAME_PLAYERS = self.slider.value
        self.gamemode = GameModes.MENU_MAIN
        
    def runSettingsMenu(self):
        self.gamemode = GameModes.MENU_SETTINGS
        self.slider = Slider((32,32), 2, 4, Settings.GAME_PLAYERS)
        self.buttonOk = Button(pygame.Rect(32, 96, 128, 32), "Ok")
        self.buttonOk.register_action(self.applySettings)
        while self.gamemode == GameModes.MENU_SETTINGS:
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            self.slider.update(self.input)
            self.buttonOk.update(self.input)
            self.surface.fill(Settings.SCREEN_COLOR)
            self.slider.draw(self.surface)
            self.buttonOk.draw(self.surface)
            pygame.display.flip()
    def runGame(self):
        self.gamemode = GameModes.GAME_PLACING_SNAILS
        
        for i in range(0, Settings.GAME_PLAYERS):
            self.addTeam('test', 2, i)

        self.turnManager = TurnManager()
        self.turnManager.setTeams(self.teams)
        self.turnManager.startTimer()

        self.running = True
        while self.running:
            #T Timer (framerate)
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for team in self.teams:
                            for snail in team.sprites():
                                if team.hasTurn and snail.hasTurn and TurnManager().status == TurnStatus.CURRENTTURN:
                                    snail.useWeapon()
                if event.type == pygame.QUIT:
                    return

            self.update()
            #R refresh
            self.surface.fill(Settings.SCREEN_COLOR)
            self.drawGame()
            pygame.display.flip()
            
    def update(self):
        self.terrain.update()
        self.updateTeams()

        self.bullets.update()

        self.updateGameMode()

    def updateTeams(self):
        self.teamsAlive = 0
        for team in self.teams:
            if team.isAlive():
                team.update(self.input, self.terrain)
                bullet = team.active_weapon.bullet
                if bullet <> None:
                    bullet.update(self.terrain)
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
                self.running = False

    def drawGame(self):
        self.terrain.draw(self.surface)
        for team in self.teams:
            team.draw(self.surface)

        self.bullets.draw(self.surface)
        if self.gamemode == GameModes.GAME_PLAYING:
            self.drawTimer()
        
    def drawTimer(self):
        self.turnManager.draw(self.surface)