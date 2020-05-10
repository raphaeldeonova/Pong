import math
import pygame
import random
from GameObject import GameObject

class Ball(GameObject):

    #EFFECTS: makes a ball with its x, y, radius, speed, angle, and associated pygame.Surface
    def __init__(self,x,y,r,speed,a, gameDisplay):
        super().__init__(gameDisplay)
        self.x = int(x)
        self.y = int(y)
        self.r = int(r)
        self.a = a
        self.speed = speed
        self.xspeed = int(self.speed * math.cos(self.a))
        self.yspeed = int(-self.speed * math.sin(self.a)) # y-coordinate in pygame is reversed
    
    #EFFECTS: renders the white ball on the surface with x, y, and radius
    def render(self):
        pygame.draw.circle(self.gameDisplay,(255,255,255),(self.x, self.y),self.r)
    
    #MODIFIES: this
    #EFFECTS: bounces the ball from the top or bottom edge
    def __bounce(self):
        self.yspeed *= -1
        self.x += self.xspeed
    
    #MODIFIES: this
    #EFFECTS: moves the ball according to it's ypeed and xspeed. If the ball is on the top or bottom edges,
    #         place the ball on the edge, while flipping the speed.
    def update(self):
        if (self.y + self.yspeed <= self.r):
            self.y = self.r
            self.__bounce()
        elif (self.y + self.yspeed >= self.screenheight - self.r):
            self.y = self.screenheight - self.r
            self.__bounce()
        else:
            self.y += self.yspeed
            self.x += self.xspeed
    
    #EFFECTS: places the ball in the middle of the screen, and makes the ball go in
    #         a random direction and speed
    def reset(self):
        self.x = self.screenwidth //2
        self.y = self.screenheight //2

        a1 = random.uniform(-math.pi/3,math.pi/3)
        a2 = random.uniform(math.pi*2/3 , math.pi*4/3)

        self.speed = int(random.uniform(3,5))

        if random.randint(0,1) == 1:
            self.a = a1
            self.updateSpeeds()
        else:
            self.a = a2
            self.updateSpeeds()
        pygame.time.wait(2000)
    
    #REQUIRE: angle of type float
    #MODIFIES: this
    #EFFECTS: Updates the speeds when angle is changed
    def updateSpeeds(self):
        self.xspeed = int(self.speed * math.cos(self.a))
        self.yspeed = int(-self.speed * math.sin(self.a))

    
