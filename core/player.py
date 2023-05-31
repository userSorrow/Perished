from core.generator import Generator
from core.map import Map
from core.pallet import Pallet
from core.wall import Wall
from core.gate import Gate

class Player:
    movementChanges = {
        #   : [x, y]
        "up": [0, -1], # changed this from 1 to -1 
        "down": [0, 1], # changed this from -1 to 1 
        "left": [-1, 0],
        "right": [1, 0]
    }
    
    def __init__(self, name, map):
        self.health = 2
        self.name = name
        self.map = map
        self.positionX = int((self.map.height - 1) / 2) if self.map.height % 2 == 1 else int((self.map.height) / 2) # this  
        self.positionY = int((self.map.width - 1) /2) if self.map.width % 2 == 1 else int((self.map.width) / 2)
        self.crossGate = False
        map.addPlayer(self)
    
    def isDead(self):
        return self.health <= 2
    
    def getAvailableOptions(self) -> str:
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
            # need to add a better one for being unable to vault
            if isinstance(item, Gate):             # need to add a gate one
                return "escape"
            if isinstance(item, Pallet):
                return "vault pallet"
            if isinstance(item, Wall): # when reaching wall, there should be no movement option
                return "wall"
            # add killer later

        options = {}
        for key in list(self.movementChanges.keys()):
            if getResponse(key) != "wall": # there is probably a better way to prevent option from coming up
                options[key] = getResponse(key)

        return options
    
    def areaAroundPlayer(self) -> list:
        area = []
        # [space above player, space below player, space to the left of player, space to the right of the player]
        
        area.append(self.map.grid[self.positionY - 1][self.positionX])
        area.append(self.map.grid[self.positionY + 1][self.positionX])
        area.append(self.map.grid[self.positionY][self.positionX - 1])
        area.append(self.map.grid[self.positionY][self.positionX + 1])
        
        return area
    
    # @getattr
    def getItemAt(self, move) -> object:
        changeX = self.movementChanges[move][0]
        changeY = self.movementChanges[move][1]
        return self.map.grid[self.positionY + changeY][self.positionX + changeX]
  
    def move(self, direction) -> None:
        # need a method to check the surrounding of the player
        # if the grid where the player is going is None, that means it is an empty site
        
        self.map.grid[self.positionY][self.positionX] = None # sets the original player position to None
        item = self.getItemAt(direction) 
        
        if item is None:
            self.positionX += self.movementChanges[direction][0] # this is wrong because we are setting the position at this position not actually changing the position
            self.positionY += self.movementChanges[direction][1]
            
        if isinstance(item, Generator):
            item.increaseProgress(100) # max is 100, I set it at 100 for testing purpose
            if item.isGenCompleted():
                x = item.positionX
                y = item.positionY
                
                self.map.grid[y][x] = None
                Generator.all.remove(item) # this is used later on to determine if player completes every generator
            # find the square the player is refering to and if generator is completed that square becomes "None"
            
        if isinstance(item, Pallet): # need one for pallet
            originalX, originalY = self.positionX, self.positionY
            
            self.positionX += self.movementChanges[direction][0] 
            self.positionY += self.movementChanges[direction][1]
            
            item = self.getItemAt(direction)
            
            if item is None:
                self.positionX += self.movementChanges[direction][0] 
                self.positionY += self.movementChanges[direction][1]
            else:
                self.positionX = originalX
                self.positionY = originalY
        
        if not isinstance(item, Gate):
            self.map.grid[self.positionY][self.positionX] = self # put player back on map (and suits perfectly for walls)
        else:
            self.crossGate = True
        
    def __str__(self) -> str:
        return "*"
