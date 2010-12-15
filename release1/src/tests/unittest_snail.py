import unittest
import sys
import pygame
sys.path.append("..\\") 
from snail import Snail
from team import Team
from settings import Settings
from terrain import Terrain

class testSnail(unittest.TestCase):

    """

    A test class for the Blogger module.

    """



    def setUp(self):

        """

        set up data used in the tests.

        setUp is called before each test function execution.

        """

        pygame.init()
        pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT], pygame.FULLSCREEN)
        pygame.time.wait(1000)
        
        self.terrain = Terrain()
        self.teamName = "EJteam"
        self.team = Team(self.teamName)
        self.snail = Snail(self.team)



    def testInitialized(self):
        self.assertEqual(self.snail.team.name, self.teamName)
        self.assertEqual(self.snail.hasTurn, False)

    def testFollowMouse(self):
        pygame.mouse.set_pos([100,100])
        pygame.display.flip()
        pygame.display.flip()
            
        self.snail.update(self.terrain)
        self.assertEqual(self.snail.rect.centerx, 100)
        self.assertEqual(self.snail.rect.centery, 100)
        
        self.terrain.addBlock(150, 150)
        #pygame.time.Clock().tick()
        pygame.mouse.set_pos([300,300])
        pygame.display.flip()
        pygame.time.wait(1000)
        pygame.display.flip()
        
        self.snail.update(self.terrain)
        self.assertNotEqual(self.snail.rect.centerx, pygame.mouse.get_pos()[0])
        self.assertNotEqual(self.snail.rect.centery, pygame.mouse.get_pos()[1])
        pass    
        
    def testSnailPlaced(self):
        
        pass
    
    def testGravity(self):
        pass

    def testAiming(self):
        pass
        
    def testShooting(self):
        pass
        
    def testMoving(self):
        pass
        
    def testJumping(self):
        pass
    
    def testDie(self):
        pass
    
    def testCollision(self):
        pass

    def testTouchingSalt(self):
        pass
        
    
def suite():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(testSnail))

    return suite



if __name__ == '__main__':

    #unittest.main()



    suiteFew = unittest.TestSuite()

    #suiteFew.addTest(testSnail("testPostNewEntry"))

    #suiteFew.addTest(testSnail("testDeleteAllEntries"))

    #unittest.TextTestRunner(verbosity=2).run(suiteFew)

    unittest.TextTestRunner(verbosity=2).run(suite())
