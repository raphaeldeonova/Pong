import pygame
import constant
import random
import math
from Paddle import Paddle
from Ball import Ball
from Player import Player

pygame.init()
clock = pygame.time.Clock()

#initialize display
gameDisplay = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT))

#initialize fonts
font = pygame.font.Font("freesansbold.ttf",32)
font2 = pygame.font.Font("freesansbold.ttf",15)
text = font.render("PONG",True,(255,255,255))
text2 = font2.render("press r to reset game",True,(255,255,255))
textRect = text.get_rect()
text2Rect = text2.get_rect()
text2Rect.center = (constant.WIDTH//2, 80)
textRect.center = (constant.WIDTH//2, 40)

#initialize objects
ball = Ball(constant.WIDTH//2,constant.HEIGHT//2,10,5,random.uniform(0,math.pi), gameDisplay)
paddle1 = Paddle(50, 50, 100, gameDisplay)
paddle2 = Paddle(constant.WIDTH - 50, 50, 100, gameDisplay)

player1 = Player(paddle1)
player2 = Player(paddle2)
