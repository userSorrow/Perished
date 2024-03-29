import random
from core.generator import Generator
from core.pallet import Pallet
from core.wall import Wall
from core.gate import Gate
from core.structure import Structure

class Map:
    def __init__(self, width = 13, height = 13, numGens = 3, numPallets = 3): # 
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)] # _ --> means annoynomous variable
        self.__grid = self.grid
        self.positions = [(i, j) for i in range(width) for j in range(height)]  
        self.corners = [(1,1), (1, height - 2), (width - 2, 1), (width - 2, height - 2)]   
        self.structures = [Structure().L, Structure().doubleL, Structure().L, Structure().shack]
        self.structure_corners = [((2,6), (2,6)), ((2,6), (7,11)), ((7,11), (2,6)), ((7,11), (7,11))]
        # finds the midpoints of the sides of the map
        self.midpoints = [(0, int((height - 1) / 2)) if width % 2 == 1 else (0, int(width / 2)), 
                          (width - 1, int((height - 1) / 2)) if width % 2 == 1 else (width - 1, int(width / 2)),
                          (int((width - 1) / 2), height - 1) if width % 2 == 1 else (int(width / 2), height - 1),
                          (int((width - 1) / 2), 0) if width % 2 == 1 else (int(width / 2), 0)]
        
        self.emptyCoordinates = self.positions
        self.gateOpen = False
        self.autogenerate()

    def autogenerate(self) -> None:
        # No (2, 2), preexisting position
        playerPosX = int((self.height - 1) / 2) if self.height % 2 == 1 else int((self.height) / 2)
        playerPosY = int((self.width - 1) /2) if self.width % 2 == 1 else int((self.width) / 2)
        self.emptyCoordinates.remove((playerPosX, playerPosY)) # for player
        
        # First, generate the outer walls
        
        for corner in self.corners: #removes corner spawns , this is for killer
            self.emptyCoordinates.remove(corner)
        
        for y in range(len(self.grid)): # this generates the outer wall
            for x in range(len(self.grid)):
                if y % (len(self.grid) - 1) in [0, (len(self.grid) - 1)] or x % (len(self.grid) - 1) in [0, (len(self.grid) - 1)]:
                    self.grid[y][x] = Wall()
                    self.emptyCoordinates.remove((x,y))

        # generating structures
        for i in range(len(self.structure_corners)):
            x, y = self.structure_corners[i]
            a,b = x
            c,d = y
            
            m = 0
            for j in range(a,b):
                n = 0
                for k in range(c,d):
                    item = self.structures[i][m][n]
                    
                    if isinstance(item, Generator):
                        print(len(Generator.all))
                        item.positionX, item.positionY = j,k
                    elif isinstance(item, Pallet):
                        item.positionX, item.positionY = j,k
                    self.grid[j][k] = item
                    n += 1
                m += 1

        # for _ in range(numGens):
        #     coordinate = random.choice(self.positions)
        #     x, y = coordinate
        #     self.grid[y][x] = Generator(x,y)
        #     self.emptyCoordinates.remove(coordinate)
        
        # for _ in range(numPallets):
        #     coordinate = random.choice(self.positions)
        #     x, y = coordinate
        #     self.grid[y][x] = Pallet(x,y)
        #     self.emptyCoordinates.remove(coordinate)

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

