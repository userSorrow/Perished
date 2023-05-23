from core.generator import Generator
from core.map import Map
from core.pallet import Pallet

class Player:
    movementChanges = {
        #   : [x, y]
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [1, 0]
    }
    
    def __init__(self, name, map):
        self.health = 2
        self.name = name
        self.map = map
        self.positionX = 2
        self.positionY = 2
        map.addPlayer(self)
    
    def isDead(self):
        return self.health <= 2
    
    def getAvailableOptions(self):
        """
        options = {
            "Move": ["up", "down", "right", "left"],
            "Generator": ["fix"],
            "Pallet": ["throw"],
            "Stay": ["stay"]
        }
        """
        def getResponse(move) -> str:
            item = self.getItemAt(move)
            if item == None:
                return "move " + move
            if isinstance(item, Generator):
                return "fix generator"
            if isinstance(item, Pallet):
                return "vault pallet"
            # add killer later

        options = {}
        for key in list(self.movementChanges.keys()):
            options[key] = getResponse(key)

        return options
    
    def areaAroundPlayer(self):
        area = []
        # [space above player, space below player, space to the left of player, space to the right of the player]
        
        area.append(self.map.grid[self.positionY - 1][self.positionX])
        area.append(self.map.grid[self.positionY + 1][self.positionX])
        area.append(self.map.grid[self.positionY][self.positionX - 1])
        area.append(self.map.grid[self.positionY][self.positionX + 1])
        
        return area
    
    def getItemAt(self, move):
        changeX = self.movementChanges[move][0]
        changeY = self.movementChanges[move][1]
        return self.map.grid[self.positionY + changeY][self.positionX + changeX]
    
    def move(self, direction):
        # need a method to check the surrounding of the player
        # if the grid where the player is going is None, that means it is an empty site
        
        self.map.grid[self.positionY][self.positionX] = None # sets the original player position to None
        
        if direction == "up" and self.areaAroundPlayer()[0] is None:
            self.positionY -= 1
        elif direction == "down" and self.areaAroundPlayer()[1] is None:
            self.positionY += 1
        elif direction == "left" and self.areaAroundPlayer()[2] is None:
            self.positionX -= 1
        elif direction == "right" and self.areaAroundPlayer()[3] is None:
            self.positionX += 1
        
        self.map.grid[self.positionY][self.positionX] = self # put player back on map
        
    def __str__(self) -> str:
        return "*"
