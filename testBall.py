import unittest
import pygame
import math
from Ball import Ball

class testBall(unittest.TestCase):
    
    def setUp(self):
        self.gameDisplay = pygame.display.set_mode((400, 400))
        self.testball1 = Ball(100,200,3,4,0,self.gameDisplay)
        self.testball2 = Ball(200, 390, 5, 5, -math.pi / 2, self.gameDisplay) # bottom border
        self.testball3 = Ball(200, 10, 5, 5, math.pi/2, self.gameDisplay)

    def testConstructor(self):
        self.assertEqual(self.testball1.screenwidth, 400)
        self.assertEqual(self.testball1.screenheight, 400)
        self.assertEqual(self.testball1.x, 100)
        self.assertEqual(self.testball1.y, 200)
        self.assertEqual(self.testball1.r, 3)
        self.assertEqual(self.testball1.speed, 4)
        self.assertEqual(self.testball1.a, 0)

        self.assertEqual(self.testball2.x, 200)
        self.assertEqual(self.testball2.y, 390)
        self.assertEqual(self.testball2.r, 5)
        self.assertEqual(self.testball2.speed, 5)
        self.assertEqual(self.testball2.a, -math.pi/2)
        self.assertAlmostEqual(self.testball2.xspeed, 0)
        self.assertEqual(self.testball2.yspeed, 5)

    def testUpdate(self):
        self.testball1.update()
        self.assertEqual(self.testball1.x, 104)
        self.assertEqual(self.testball1.y, 200)
        self.assertEqual(self.testball1.yspeed, 0)
        self.assertEqual(self.testball1.xspeed, 4)
    
    def testUpdateBottomBorder(self):
        self.testball2.update()
        self.assertEqual(self.testball2.y, 400)
        self.assertEqual(self.testball2.x, 200)
        self.assertEqual(self.testball2.yspeed, -5)
    
    def testUpdateTopBorder(self):
        self.testball3.update()
        self.assertEqual(self.testball3.y, 5)
        self.assertEqual(self.testball3.x, 200)
        self.assertEqual(self.testball3.yspeed, 5)
    
    def testReset(self):
        self.testball1.reset()
        self.assertEqual(self.testball1.x, 200)
        self.assertEqual(self.testball1.y, 200)
        self.assertTrue(self.testball1.speed >= 3 and self.testball1.speed <= 5)
        cond1 = self.testball1.a >= -math.pi/3 and self.testball1.a <= math.pi/3
        cond2 = self.testball1.a >= math.pi*2/3 and self.testball1.a <= math.pi*4/3
        self.assertTrue(cond1 or cond2)

        


if __name__ == "__main__":
    unittest.main()
