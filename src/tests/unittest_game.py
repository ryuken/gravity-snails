import unittest
import pygame
from game import Game
from settings import Settings
class testGame(unittest.TestCase):

    """

    A test class for the Blogger module.

    """



    def setUp(self):
        self.game = Game()
        """

        set up data used in the tests.

        setUp is called before each test function execution.

        """
        
    def testInitializedPygame(self):
        self.assertEquals(self.game.initPygame(), 0)
        
    def testInitializedScreen(self):
        self.assertEquals(pygame.display.get_caption()[0], Settings.GAME_TITLE)
        
    def testCreateObjects(self):
        self.game.createGameObjects()
        
def suite():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(testGame))

    return suite



if __name__ == '__main__':

    #unittest.main()



    suiteFew = unittest.TestSuite()

    #suiteFew.addTest(testSnail("testPostNewEntry"))

    #suiteFew.addTest(testSnail("testDeleteAllEntries"))

    #unittest.TextTestRunner(verbosity=2).run(suiteFew)

    unittest.TextTestRunner(verbosity=2).run(suite())
