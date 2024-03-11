class Player:
    def __init__(self):
        self.budget = 50
        self.memory = [True]
        self.enemy_memory = [True]

    def __str__(self):
        return (f"{type(self).__name__}{self.budget}")

    def play(self)->bool:
        pass