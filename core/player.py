class Player:
    def __init__(self, name):
        self.health = 2
        self.name = name
        self.position = (2, 2)
    
    def isDead(self):
        return self.health <= 2
    
