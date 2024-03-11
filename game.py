import random
from typing import List
from player import Player

class Game:
    cost_of_draw = 3
    cost_of_win = 5
    cost_of_lose = -1
    cost_of_life = 1

    def __init__(self, players: List[Player]):
        self.players = players

    def startGame(self, epochs=100, limit=1000, step=3):
        for epoch in range(epochs):
            if len(self.players) < 2:
                self.printStatistic()
                print(f'В популяции меньше двух игроков')
                break
            if len(self.players)>limit:
                self.printStatistic()
                print(f'В популяции больше {limit} игроков')
                break
            random.shuffle(self.players)
            pairs = []
            for i in range(1,len(self.players), 2):
                pair = (self.players[i-1], self.players[i])
                pairs.append(pair)
            for pair in pairs:
                self.playGame(*pair)
            if epoch % step == 0:
                self.printStatistic()
        print('Прошли все эпохи')

    def printStatistic(self):
        statistic={}
        for player in self.players:
            name = type(player).__name__
            if name in statistic:
                statistic[name] += 1
            else:
                statistic[name] = 1
        keys = sorted(statistic.keys())
        for key in keys:
            print(f'{key}: {statistic[key]}', end=',')
        print()

    def playGame(self, p1, p2):
        wins = (Game.cost_of_lose, Game.cost_of_lose)
        if p1.play() and p2.play():
            wins = (Game.cost_of_draw, Game.cost_of_draw)
        elif p1.play() and not p2.play():
            wins = (Game.cost_of_lose, Game.cost_of_win)
        elif p2.play() and not p1.play():
            wins = (Game.cost_of_win, Game.cost_of_lose)

        self.updateBudget(p1, p2, wins)
        self.updateMemory(p1, p2, wins)


    def updateMemory(self, p1, p2, wins):
        if wins[0]==wins[1]==self.cost_of_draw:
            p1.enemy_memory.append(True)
            p2.enemy_memory.append(True)
            p1.memory.append(True)
            p2.memory.append(True)

        elif wins[0]==self.cost_of_win:
            p1.enemy_memory.append(True)
            p2.enemy_memory.append(False)
            p1.memory.append(False)
            p2.memory.append(True)

        elif wins[1]==self.cost_of_win:
            p1.enemy_memory.append(False)
            p2.enemy_memory.append(True)
            p1.memory.append(True)
            p2.memory.append(False)

        else:
            p1.enemy_memory.append(False)
            p2.enemy_memory.append(False)
            p1.enemy_memory.append(False)
            p2.enemy_memory.append(False)



    def updateBudget(self, p1, p2, wins):
        p1.budget += wins[0] - Game.cost_of_life
        p2.budget += wins[1] - Game.cost_of_life

        if p1.budget>100:
            p1.buget = 50
            self.players.append(p1)
        if p2.budget>100:
            p2.budget = 50
            self.players.append(p2)


        if p1.budget<0:
            self.players.remove(p1)
        if p2.budget<0:
            self.players.remove(p2)