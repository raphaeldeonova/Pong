import unittest
from Player import Player
from Paddle import Paddle
import pygame

class testPlayer(unittest.TestCase):

    def setUp(self):
        display = pygame.display.set_mode((400, 400))
        self.testpaddle = Paddle(20, 100, 100, display)
        self.testPlayer = Player(self.testpaddle)
    
    def testConstructor(self):
        self.assertEquals(self.testPlayer.paddle, self.testpaddle)
    
    def testWinRound(self):
        self.testPlayer.winRound()
        self.assertEqual(self.testPlayer.score, 1)
        self.assertTrue(self.testPlayer.paddle.isReset)

if __name__ == "__main__":
    unittest.main()