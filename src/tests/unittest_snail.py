import unittest
import sys
import pygame
sys.path.append("..\\") 
from snail import Snail
from team import Team
from settings import Settings
from terrain import Terrain
from input import Input
from enums import *
from utils import load_image
from turnmanager import TurnManager
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
        self.team.setGravity(Direction.DOWN)
        self.team.hasTurn = True
        
        TurnManager().status = TurnStatus.CURRENTTURN
        TurnManager().teams = [] 
        TurnManager().teams.append(self.team)
        self.snail = Snail(self.team)
        self.snail.hasTurn = True

    def testInitialized(self):
        self.assertEqual(self.snail.team.name, self.teamName)
        # self.assertEqual(self.snail.hasTurn, False)

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
        
        self.assertNotEqual(self.snail.rect.centerx, 150)
        self.assertNotEqual(self.snail.rect.centery, 150)
        
    def testSnailPlaceSnailCorrect(self):
        self.input.mouse_x = 100
        self.input.mouse_y = 100
        self.input.mouse_left = True
        self.input.mouse_left_click = True
        self.snail.update(self.input, self.terrain)
        self.assertTrue(self.snail.isPlaced)
        
    def testSnailPlaceSnailWrong(self):
        self.input.mouse_x = 150
        self.input.mouse_y = 150
        self.terrain.addBlock(150, 150)
        self.input.mouse_left = True
        self.snail.update(self.input, self.terrain)
        self.assertFalse(self.snail.isPlaced)
        
    def testGravityDown(self):
        self.testSnailPlaceSnailCorrect()
        self.team.setGravity(Direction.DOWN)
        old_y = self.snail.rect.centery
        for i in range(0,10):
            self.snail.update(self.input, self.terrain)
            
        self.assertTrue(self.snail.rect.centery > old_y)
    
    def testGravityDownSpeed(self):
        self.testSnailPlaceSnailCorrect()
        self.assertEqual(self.snail.direction['jump'], 0)
        self.snail.updateGravity()
        self.assertEqual(self.snail.direction['jump'], self.snail.speed['fall'])
        
        waitTurns = 5 / self.snail.speed['fall']
        for i in range(0, waitTurns + 5):
            self.snail.updateGravity()
            
        self.assertEqual(self.snail.direction['jump'], 5)
        
    def testGravityUp(self):
        self.testSnailPlaceSnailCorrect()
        self.snail.gravity_direction = Direction.UP
        old_y = self.snail.rect.centery
        for i in range(0,10):
            self.snail.update(self.input, self.terrain)
            
        self.assertTrue(self.snail.rect.centery < old_y)
        
    def testGravityRight(self):
        self.testSnailPlaceSnailCorrect()
        self.snail.gravity_direction = Direction.RIGHT
        old_x = self.snail.rect.centerx
        for i in range(0,10):
            self.snail.update(self.input, self.terrain)
            
        self.assertTrue(self.snail.rect.centerx > old_x)
    
    def testGravityLeft(self):
        self.testSnailPlaceSnailCorrect()
        self.snail.gravity_direction = Direction.LEFT
        old_x = self.snail.rect.centerx
        for i in range(0,10):
            self.snail.update(self.input, self.terrain)
            
        self.assertTrue(self.snail.rect.centerx < old_x)
            
    def testAiming(self):
        pass
        
    def testShooting(self):
        pass
        
    def testMoving(self):
        pass
        
    def testJumping(self):
        pass
    
    def testDie(self):
        self.assertEquals(self.snail.hitpoints, 100)
    
    def testCollision(self):
        pass

    def testTouchingSalt(self):
        pass
        
    #def testGravityImages(self):
    #    self.team.gravity_direction = Direction.UP
    #    self.snail = Snail(self.team)
    #    self.team.gravity_direction = Direction.DOWN
    #    self.snail.update(self.input, self.terrain)
    #    self.current_snail_image_down_right = self.snail.image_down_right
    #    self.supposed_snail_image_down_right = load_image('snail'+str(self.team.gravity_direction)+'Right.png')
    #    self.assertEqual(self.current_snail_image_down_right., self.supposed_snail_image_down_right.__name__)

    
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
