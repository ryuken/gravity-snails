import unittest
import sys
import pygame
sys.path.append("..\\") 
from snail import Snail
from team import Team
from settings import Settings
from terrain import Terrain
from input import Input
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
        pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT])

        self.input = Input()
        self.terrain = Terrain()
        self.teamName = "EJteam"
        self.team = Team(self.teamName)
        self.snail = Snail(self.team)


    def testInitialized(self):
        self.assertEqual(self.snail.team.name, self.teamName)
        self.assertEqual(self.snail.hasTurn, False)

    def testFollowMouse(self):
        self.input.mouse_x = 100
        self.input.mouse_y = 100
        self.snail.update(self.input, self.terrain)
        self.assertEqual(self.snail.rect.centerx, 100)
        self.assertEqual(self.snail.rect.centery, 100)
        
        self.input.mouse_x = 150
        self.input.mouse_y = 150
        self.terrain.addBlock(150, 150)
        self.snail.update(self.input, self.terrain)
        
        self.assertNotEqual(self.snail.rect.centerx, pygame.mouse.get_pos()[0])
        self.assertNotEqual(self.snail.rect.centery, pygame.mouse.get_pos()[1])
        
    def testSnailPlaceSnailCorrect(self):
        self.input.mouse_x = 100
        self.input.mouse_y = 100
        self.input.mouse_left = True
        self.snail.update(self.input, self.terrain)
        self.assertTrue(self.snail.isPlaced)
        
    def testSnailPlaceSnailWrong(self):
        self.input.mouse_x = 150
        self.input.mouse_y = 150
        self.terrain.addBlock(150, 150)
        self.input.mouse_left = True
        self.snail.update(self.input, self.terrain)
        self.assertFalse(self.snail.isPlaced)
        
    def testGravity(self):
        self.testSnailPlaceSnailCorrect()
        
        
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
