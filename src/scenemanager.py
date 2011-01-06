import pygame
#from mainmenu import MainMenu
from input import Input
from settings import Settings
from enums import GameModes

class SceneManager(object):
    _instance2 = None
    _count2    = 0

    def __new__(cls, *args, **kwargs):
        if not cls._instance2:
            cls._instance2 = super(SceneManager, cls).__new__(
                                cls, *args, **kwargs)

#            _count += 1
            print "Created new instance of SceneManger"
        return cls._instance2

    def __init__(self):
        # Display some text
        if SceneManager._count2 == 0:
            #Init
            self.initPygame()
            self.initScreen()
            self.initClock()
            self.initInput()
            self.initGame()
            SceneManager._count2 += 1

    def initGame(self):
        self.gamemode = GameModes.MENU_MAIN
        self.scene = None

    def initPygame(self):
        result = pygame.init()
        return result[1]

    def initScreen(self):
        self.surface = pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT]) #retourneert Surface
        pygame.display.set_caption(Settings.GAME_TITLE)

    def initClock(self):
        self.clock = pygame.time.Clock()

    def initInput(self):
        self.input = Input()

    def run(self):
        running = True
        while(running):
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #game.addTeam('test', 2, Direction.LEFT)
            #game.addTeam('test2', 2, Direction.RIGHT)

            self.scene.update(self.input)
            self.surface.fill(Settings.SCREEN_COLOR)
            self.scene.draw(self.surface)

            pygame.display.flip()
        self.scene.clean()

    def setScene(self, scene):
        if self.scene:
            self.scene.clean()
        self.scene = scene
