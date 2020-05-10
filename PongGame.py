import pygame
import constant
import random
import math
from Paddle import Paddle
from Ball import Ball
from Player import Player

class PongGame(object):

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.gameDisplay = pygame.display.set_mode((constant.WIDTH,constant.HEIGHT))

        self.text, self.text2, self.font, self.font2, self.textRect, self.text2Rect = None,None,None,None,None,None
        self.ball, self.paddle1, self.paddle2, self.player1, self.player2 = None,None,None,None,None

        self.initializeFont()
        self.initializeObject()
        
        self.paddlespeed = 5
        self.terminate = False

        while not self.terminate:
            self.checkEvent()
            self.collisionCheck()
            self.checkScore()
            self.updateObject()
            self.updateText()
            self.renderText()
            self.renderObject()

            pygame.display.update()
            self.clock.tick(120)
        
        pygame.quit()



    def initializeFont(self):
        self.font = pygame.font.Font("freesansbold.ttf",32)
        self.font2 = pygame.font.Font("freesansbold.ttf",15)
        self.text = self.font.render("PONG",True,(255,255,255))
        self.text2 = self.font2.render("press r to reset game",True,(255,255,255))
        self.textRect = self.text.get_rect()
        self.text2Rect = self.text2.get_rect()
        self.text2Rect.center = (constant.WIDTH//2, 80)
        self.textRect.center = (constant.WIDTH//2, 40)
    
    def initializeObject(self):
        self.ball = Ball(constant.WIDTH//2,constant.HEIGHT//2,10,5,random.uniform(0,math.pi), self.gameDisplay)
        self.paddle1 = Paddle(30,20,150, self.gameDisplay)
        self.paddle2 = Paddle(constant.WIDTH-50,20,150, self.gameDisplay)
        self.player1 = Player(self.paddle1)
        self.player2 = Player(self.paddle2)

    def resetGame(self):
        self.ball.reset()
        self.player1.reset()
        self.player2.reset()
    
    def checkEvent(self):
        for event in pygame.event.get():                                    # check events
            if event.type == pygame.QUIT:
                self.terminate = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.resetGame()
                if event.key == pygame.K_UP:
                    if self.paddle2.y>0:
                        self.paddle2.setChange(-self.paddlespeed)
                        
                if event.key == pygame.K_DOWN:
                    if self.paddle2.y < constant.HEIGHT - self.paddle2.h:
                        self.paddle2.setChange(self.paddlespeed)
                        
                if event.key == pygame.K_w:
                    if self.paddle1.y > 0:
                        self.paddle1.setChange(-self.paddlespeed)
                if event.key == pygame.K_s:
                    if self.paddle1.y < constant.HEIGHT - self.paddle1.h:
                        self.paddle1.setChange(self.paddlespeed)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.paddle2.stop()
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    self.paddle1.stop()
            print(event)
    
    def collisionCheck(self):
        if (self.ball.x >= self.paddle1.x + self.ball.r and self.ball.x <= self.paddle1.x + self.paddle1.w + self.ball.r) and (self.ball.y >= self.paddle1.y and self.ball.y <= self.paddle1.y + self.paddle1.h):
            self.ball.a = random.uniform(math.pi*7/4 , math.pi*9/4)
            self.ball.speed = random.randint(4,8)
            #print(ball.a)
            self.ball.updateSpeeds()
        if (self.ball.x >= self.paddle2.x - self.ball.r and self.ball.x <= self.paddle2.x + self.paddle2.w - self.ball.r) and (self.ball.y >= self.paddle2.y and self.ball.y <= self.paddle2.y + self.paddle2.h):
            self.ball.a = random.uniform(math.pi*3/4 , math.pi*5/4)
            self.ball.speed = random.randint(4,8)
            #print(ball.a)
            self.ball.updateSpeeds()

    def renderText(self):
        self.gameDisplay.fill((0,0,0))                        
        self.gameDisplay.blit(self.text,self.textRect) 
        self.gameDisplay.blit(self.text2,self.text2Rect)
        self.gameDisplay.blit(self.score1text , self.score1Rect)
        self.gameDisplay.blit(self.score2text , self.score2Rect)
    
    def updateText(self):
        self.score1text = self.font.render(str(self.player1.score),True,(255,255,255))
        self.score2text = self.font.render(str(self.player2.score),True,(255,255,255))
        self.score1Rect = self.score1text.get_rect()
        self.score1Rect.center = (40,40)
        self.score2Rect = self.score2text.get_rect()
        self.score2Rect.center = (constant.WIDTH - 40,40)
    
    def updateObject(self):
        self.paddle1.update()
        self.paddle2.update()
        self.ball.update()
    
    def checkScore(self):
        if self.ball.x <= self.ball.r:
            self.player2.winRound()
            self.ball.reset()
            self.paddle1.reset()
        elif self.ball.x >= constant.WIDTH - self.ball.r:
            self.player1.winRound()
            self.ball.reset()
            self.paddle2.reset()

    def renderObject(self):
        self.ball.render()
        self.paddle1.render()
        self.paddle2.render()
    
if __name__ == "__main__":
    PongGame()