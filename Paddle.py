import pygame
from GameObject import GameObject

class Paddle(GameObject):
    def __init__(self,x,w,h, gameDisplay):
        super().__init__(gameDisplay)
        self.w = w
        self.h = h
        self.x = x
        self.y = self.screenheight // 2 - self.h //2 
        self.score = 0
        self.change = 0

    #EFFECTS: renders the 
    def render(self):
        pygame.draw.rect(self.gameDisplay,(255,255,255),(self.x,self.y,self.w,self.h))

    #EFFECTS: updates the paddle's position, can't go outside of screen
    #USAGE: use this at every tick of game
    def update(self):
        self.y +=self.change
        self.y = self.clamp(self.y, 0,self.screenheight-self.h)
    
    #EFFECTS: moves the paddle to yafter, can't go outside of screen
    def moveTo(self, yafter:int):
        self.y = yafter
        self.y = self.clamp (self.y, 0, self.screenheight - self.h)

    #EFFECTS: resets the y position to the middle of the screen
    def reset(self):
        self.y = self.screenheight//2 - self.h//2

    #EFFECTS: return true if paddle is in the middle of the screen
    def isReset(self) -> bool:
        return self.y == self.screenheight//2 - self.h//2

    #EFFECTS: stops the paddle in place
    def stop(self):
        self.change = 0
    
    #EFFECTS: change the change to changeafter
    def setChange(self, changeafter):
        self.change = changeafter