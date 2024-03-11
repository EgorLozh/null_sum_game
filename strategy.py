import random

from player import Player


class GoodBoy(Player):
    def play(self):
        return True


class BadBoy(Player):
    def play(self):
        return False


class CopyCat(Player):
    def play(self):
        return self.enemy_memory[-1]


class Goofy(Player):
    def play(self):
        return random.choice([True, False])
