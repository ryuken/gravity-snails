import unittest
import sys
import pygame
sys.path.append("..\\") 
from terrain import Terrain
from settings import Settings
from salt import Salt

class testTerrain(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT])
        
        self.terrain = Terrain()
    def testAddTerrainBlock(self):
        self.terrain.addBlock(100, 150)
        self.assertEqual(len(self.terrain.sprites()), 1)
        self.assertEqual(self.terrain.sprites()[0].rect.x, 100)
        self.assertEqual(self.terrain.sprites()[0].rect.y, 150)
        
    def testCreateTerrain(self):
        self.terrain.createEastBorder(5)
        self.terrain.createNorthBorder(5)
        self.terrain.createSouthBorder(5)
        self.terrain.createWestBorder(5)
        self.assertEqual(len(self.terrain.sprites()), 5 * 4) 
               
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testTerrain))
    return suite

if __name__ == '__main__':
    suiteFew = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite())
