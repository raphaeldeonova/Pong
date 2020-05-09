import unittest
import pygame
from Paddle import Paddle

class testPaddle(unittest.TestCase):

    def setUp(self):
        display = pygame.display.set_mode((400, 400))
        self.testpaddle = Paddle(20, 50, 100, display)
    
    def testConstructor(self):
        self.assertEqual(self.testpaddle.x, 20)
        self.assertEqual(self.testpaddle.w, 50)
        self.assertEqual(self.testpaddle.h, 100)
        self.assertEqual(self.testpaddle.y, 400 // 2 - 100 //2 )
    
    def testMoveTo(self):
        self.testpaddle.moveTo(0)
        self.assertEqual(self.testpaddle.y, 0)
        self.testpaddle.moveTo(400)
        self.assertEqual(self.testpaddle.y, 300)
    
    def testSetChange(self):
        self.testpaddle.setChange(5)
        self.assertEqual(self.testpaddle.change, 5)
    
    def testUpdate(self):
        self.testpaddle.setChange(5)
        self.testpaddle.update()
        self.assertEqual(self.testpaddle.y, 155)
        self.testpaddle.moveTo(400)
        self.testpaddle.update()
        self.assertEqual(self.testpaddle.y, 300)
    
    def testReset(self):
        self.testpaddle.reset()
        self.assertTrue(self.testpaddle.isReset())

if __name__ == "__main__":
    unittest.main()
