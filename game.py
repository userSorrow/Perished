from core.player import Player, Killer
from core.map import Map
from core.pallet import Pallet
from core.generator import Generator
from core.wall import Wall
from core.gate import Gate

map = Map(11,11)
#playerName = input("Enter Player Name: ")
player = Player("b", map)
killer = Killer("k", map)
playing = True
turn = 0

while playing:
    print(map)
    playerTurn = turn % 4 in [0,1]
    killerTurn = turn % 4 in [2,3]
    
    if playerTurn:
        print("Player's Turn")
        
        options = player.getAvailableOptions()
        print("\nOptions")
        for option in list(options.keys()):
            print(str(option) + ": " + str(options[option]))
        selected = input("What would you like to do? ")
        player.move(selected.lower())
    
    elif killerTurn:
        print("Killer's Turn")
        
        options = killer.getAvailableOptions()
        print("\nOptions")
        for option in list(options.keys()):
            print(str(option) + ": " + str(options[option]))
        selected = input("What would you like to do? ")
        killer.move(selected.lower())

    
    
    totalGenLeft = len(Generator.all)
    if totalGenLeft == 0 and not map.gateOpen:
        map.generateGate()
    
    turn += 1
    playing = not player.crossGate

print("""\nYou survived!    
For now....""")
        
    
    
