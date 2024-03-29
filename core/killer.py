import random
from core.generator import Generator
from core.player import Player
from core.pallet import Pallet
from core.wall import Wall

class Killer:
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
        self.positionX, self.positionY = random.choice(self.map.corners) 
        self.dmg = 1
        map.addPlayer(self)
    
    def getAvailableOptions(self) -> str:
        """
        options = {
            "Move": ["up", "down", "right", "left"],
            "Generator": ["break"],
            "Pallet": ["break"],
            "Stay": ["stay"]
        }
        """
        def getResponse(move) -> str:
            item = self.getItemAt(move)
            if item == None:
                return "move " + move
            if isinstance(item, Generator):
                return f"generator progress: {item.progress}% -> break generator?"
            if isinstance(item, Pallet):
                return "break pallet"
            if isinstance(item, Wall): # when reaching wall, there should be no movement option
                return "wall"
            if isinstance(item, Player):
                return "attack " + item.name


        options = {}
        for key in list(self.movementChanges.keys()):
            if getResponse(key) != "wall": # there is probably a better way to prevent option from coming up
                options[key] = getResponse(key)
            
        return options
    
    def attack(self, player) -> None:
        player.health -= self.dmg
    
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
            item.increaseProgress(-25) # reduces the generator's progress 
            
        if isinstance(item, Pallet): # need one for pallet
            x = item.positionX
            y = item.positionY
                
            self.map.grid[x][y] = None
            
        if isinstance(item, Player): # need one for player
            self.attack(item)
        
        self.map.grid[self.positionY][self.positionX] = self # put player back on map (and suits perfectly for walls)
        
    def __str__(self) -> str:
        return "K"



# class Killer(Player):
#     def __init__(self, name, map) -> None:
#         super().__init__(name, map)
#         self.map = map
#         self.positionX, self.positionY = random.choice(self.map.corners) 
#         self.dmg = 1
#         map.addPlayer(self)
        
#     def getAvailableOptions(self) -> str:
#         """
#         options = {
#             "Move": ["up", "down", "right", "left"],
#             "Generator": ["break"],
#             "Pallet": ["break"],
#             "Stay": ["stay"]
#         }
#         """
#         def getResponse(move) -> str:
#             item = self.getItemAt(move)
#             if item == None:
#                 return "move " + move
#             if isinstance(item, Generator):
#                 return f"generator progress: {item.progress}% -> break generator?"
#             if isinstance(item, Pallet):
#                 return "break pallet"
#             if isinstance(item, Wall): # when reaching wall, there should be no movement option
#                 return "wall"
#             if isinstance(item, Player):
#                 return "attack " + item.name


#         options = {}
#         for key in list(self.movementChanges.keys()):
#             if getResponse(key) != "wall": # there is probably a better way to prevent option from coming up
#                 options[key] = getResponse(key)
            
#         return options
    
#     def attack(self, player) -> None:
#         player.health -= self.dmg
        
#     def move(self, direction) -> None:
#         # need a method to check the surrounding of the player
#         # if the grid where the player is going is None, that means it is an empty site
        
#         self.map.grid[self.positionY][self.positionX] = None # sets the original player position to None
#         item = self.getItemAt(direction) 
        
#         if item is None:
#             self.positionX += self.movementChanges[direction][0] # this is wrong because we are setting the position at this position not actually changing the position
#             self.positionY += self.movementChanges[direction][1]
            
#         if isinstance(item, Generator):
#             item.increaseProgress(-25) # reduces the generator's progress 
            
#         if isinstance(item, Pallet): # need one for pallet
#             x = item.positionX
#             y = item.positionY
                
#             self.map.grid[y][x] = None
            
#         if isinstance(item, Player): # need one for player
#             self.attack(item)
        
#         self.map.grid[self.positionY][self.positionX] = self # put player back on map (and suits perfectly for walls)
    
#     def __str__(self) -> str:
#         return "K"