import random

class Map:
    def __init__(self, width = 5, height = 5):
        self.grid = [[None for i in range(width)] for i in range(height)]
        self.emptyCoordinates = [(i,j) for i in range(width) for j in range(height)]
        

    def autogenerate(self, numGens, numPallets):
        # No (2, 2), preexisting position
        randPosition = (random.randint(0, width))
    
