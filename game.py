from core.player import Player
from core.map import Map
from core.pallet import Pallet
from core.generator import Generator

map = Map()
playerName = input("Enter Player Name: ")
player = Player(playerName, map)

print(map)
