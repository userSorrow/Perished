import random
from core.generator import Generator
from core.pallet import Pallet

class Map:
    def __init__(self, width = 5, height = 5, numGens = 3, numPallets = 3):
        self.width = width
        self.height = height
        self.grid = [[None for i in range(width)] for i in range(height)]
        self.positions = [(i, j) for i in range(width) for j in range(height)]        
        self.emptyCoordinates = self.positions
        self.autogenerate(numGens, numPallets)

    def autogenerate(self, numGens, numPallets):
        # No (2, 2), preexisting position
        self.emptyCoordinates.remove((2, 2)) # for player

        for i in range(numGens):
            coordinate = random.choice(self.positions)
            x, y = coordinate
            self.grid[y][x] = Generator()
            self.emptyCoordinates.remove(coordinate)
        
        for i in range(numPallets):
            coordinate = random.choice(self.positions)
            x, y = coordinate
            self.grid[y][x] = Pallet()
            self.emptyCoordinates.remove(coordinate)

    def addPlayer(self, player):
        self.grid[2][2] = player
    
    def updatePlayerPosition(self, player):
        if not (player.positionY > self.height or player.positionX > self.width):
            self.grid[player.positionY][player.positionX] = player

    def __str__(self) -> str:
        gridStr = ""
        gridStr += "\n"
        for i in range(self.height):
            gridStr += "|"
            for j in range(self.width):
                if self.grid[i][j] is None:
                    gridStr += " "
                else:
                    gridStr += str(self.grid[i][j])
            gridStr += "| \n"
        return gridStr

