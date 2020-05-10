from Paddle import Paddle

class Player(object):

    def __init__(self, paddle: Paddle):
        self.paddle = paddle
        self.score = 0
    
    #MODIFIES: this
    #EFFECTS: adds score to by one and resets the paddle
    def winRound(self):
        self.score += 1
        self.paddle.reset()
    
    def reset(self):
        self.score = 0
        self.paddle.reset()
    
    
