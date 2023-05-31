import random
from core.generator import Generator
from core.pallet import Pallet
from core.wall import Wall
from core.gate import Gate

class Map:
    def __init__(self, width = 7, height = 7, numGens = 3, numPallets = 3): # 
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)] # _ --> means annoynomous variable
        self.__grid = self.grid
        self.positions = [(i, j) for i in range(width) for j in range(height)]  
        self.corners = [(1,1), (1, height - 2), (width - 2, 1), (width - 2, height - 2)]   
        
        # finds the midpoints of the sides of the map
        self.midpoints = [(0, int((height - 1) / 2)) if width % 2 == 1 else (0, int(width / 2)), 
                          (width - 1, int((height - 1) / 2)) if width % 2 == 1 else (width - 1, int(width / 2)),
                          (int((width - 1) / 2), height - 1) if width % 2 == 1 else ( int(width / 2), height - 1),
                          (int((width - 1) / 2), 0) if width % 2 == 1 else (int(width / 2), 0)]
        
        self.emptyCoordinates = self.positions
        self.gateOpen = False
        self.autogenerate(numGens, numPallets)

    def autogenerate(self, numGens, numPallets):
        # No (2, 2), preexisting position
        playerPosX = int((self.height - 1) / 2) if self.height % 2 == 1 else int((self.height) / 2)
        playerPosY = int((self.width - 1) /2) if self.width % 2 == 1 else int((self.width) / 2)
        self.emptyCoordinates.remove((playerPosX, playerPosY)) # for player
        
        # First, generate the outer walls
        
        for corner in self.corners: #removes corner spawns 
            self.emptyCoordinates.remove(corner)
        
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                if y % (len(self.grid) - 1) in [0, (len(self.grid) - 1)] or x % (len(self.grid) - 1) in [0, (len(self.grid) - 1)]:
                    self.grid[y][x] = Wall()
                    self.emptyCoordinates.remove((x,y))

        for _ in range(numGens):
            coordinate = random.choice(self.positions)
            x, y = coordinate
            self.grid[y][x] = Generator(x,y)
            self.emptyCoordinates.remove(coordinate)
        
        for _ in range(numPallets):
            coordinate = random.choice(self.positions)
            x, y = coordinate
            self.grid[y][x] = Pallet()
            self.emptyCoordinates.remove(coordinate)

    def generateGate(self) -> None:
        
        midpoint = random.choice(self.midpoints)
        x, y = midpoint
        if x not in [0, self.height - 1]:
            for i in range(x - 1, x + 2):
                self.grid[y][i] = Gate()
        elif y not in [0, self.width - 1]:
            for i in range(y - 1, y + 2):
                self.grid[i][x] = Gate()
        self.gateOpen = True
    
    def addPlayer(self, player) -> None:
        self.grid[player.positionY][player.positionX] = player
    
    def getItemAt(self, x, y):
        return self.__grid[y][x]

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

