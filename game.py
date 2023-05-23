from core.player import Player
from core.map import Map
from core.pallet import Pallet
from core.generator import Generator

map = Map()
#playerName = input("Enter Player Name: ")
player = Player("b", map)

playing = True

while playing:
    print(map)
    options = player.getAvailableOptions()
    print("Options")
    for option in list(options.keys()):
        print(str(option) + ": " + str(options[option]))
    selected = input("What would you like to do? ")
    player.move(selected)
