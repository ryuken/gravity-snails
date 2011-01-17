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
            self.initEventReaders()
            self.initScreen()
            self.initClock()
            self.initInput()
            self.initGame()
            SceneManager._count2 += 1

    def initGame(self):
        self.gamemode = GameModes.MENU_MAIN
        self.scene = None
        self.running = True

    def initPygame(self):
        result = pygame.init()
        return result[1]
    
    def initEventReaders(self):
        self.eventReaders = []
        
    def initScreen(self):
        self.surface = pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT]) #retourneert Surface
        pygame.display.set_caption(Settings.GAME_TITLE)

    def initClock(self):
        self.clock = pygame.time.Clock()

    def initInput(self):
        self.input = Input()

    def run(self):
        while(self.running):
            self.clock.tick(90)
            self.input.update()
            #E Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    for eventReader in self.eventReaders:
                        eventReader(event)

            self.scene.update(self.input)
            self.surface.fill(Settings.SCREEN_COLOR)
            self.scene.draw(self.surface)

            pygame.display.flip()
        self.scene.clean()

    def setScene(self, scene):
        if self.scene:
            self.scene.clean()
        if not scene == None:
            self.scene = scene
        else:
            self.running = False
            
    def registerEventReader(self, callback):
        self.eventReaders.append(callback)
        
    def unregisterEventReader(self, callback):
        self.eventReaders.remove(callback)