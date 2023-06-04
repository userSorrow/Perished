from core.player import Player, Killer
from core.map import Map
from core.pallet import Pallet
from core.generator import Generator
from core.wall import Wall
from core.gate import Gate

map = Map(7,7)
#playerName = input("Enter Player Name: ")
player = Player("b", map)
killer = Killer("k", map)
playing = True
turn = 0
playerDead = player.isDead()

while playing and not playerDead:
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
        if selected not in list(player.movementChanges.keys()):
            print("\nInvalid Move, Please Try Again!")
            turn -= 1
        else:
            player.move(selected.lower())
    
    elif killerTurn:
        print("Killer's Turn")
        
        options = killer.getAvailableOptions()
        print("\nOptions")
        for option in list(options.keys()):
            print(str(option) + ": " + str(options[option]))
        selected = input("What would you like to do? ")
        if selected not in list(killer.movementChanges.keys()):
            print("\nInvalid Move, Please Try Again!")
            turn -= 1
        else:
            killer.move(selected.lower())

    
    
    totalGenLeft = len(Generator.all)
    if totalGenLeft == 0 and not map.gateOpen:
        map.generateGate()
    
    turn += 1
    playing = not player.crossGate
    playerDead = player.isDead()
    
if playerDead:
    print(f"\nPlayer {player.name} has died!")
    
elif not playing:
    print("""\nYou survived!    
    For now....""")
        
    
    
