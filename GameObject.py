class GameObject:

    def __init__(self, gameDisplay):
        tup = gameDisplay.get_size()
        self.gameDisplay = gameDisplay
        self.screenwidth = tup[0]
        self.screenheight = tup[1]

    
    def clamp(self, n, minn, maxn):
        return max(min(maxn, n), minn)
