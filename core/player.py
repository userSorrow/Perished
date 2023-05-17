class Player:
    def __init__(self, name, map):
        self.health = 2
        self.name = name
        self.positionX = 2
        self.positionY = 2
        map.addPlayer(self)
    
    def isDead(self):
        return self.health <= 2
    
    def getAvailableOptions(self):
        options = {
            "Move": [],
            "Generator": [],
            "Pallet": [],
            "Stay": ["stay"]
        }
    
    def move(self, direction):
        if direction == "up":
            self.positionY -= 1
        if direction == "down":
            self.positionY += 1
        if direction == "left":
            self.positionX -= 1
        if direction == "right":
            self.positionX += 1
    
    def __str__(self) -> str:
        return "*"
