from player import Player
from game import Game
from strategy import *

players = []
for i in range(10):
    players.append(GoodBoy())
    players.append(BadBoy())
    players.append(CopyCat())
    players.append(Goofy())
game = Game(players)
game.startGame(epochs=10**4)