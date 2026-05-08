from player import Player
from cup import Cup
from rules import Rules

class Game:
    def __init__(self, names):
        self.players = [Player(n) for n in names]
        self.current = 0
        self.cup = Cup()
        self.rules = Rules()
        self.round = 1

    def current_player(self):
        return self.players[self.current]

    def next_player(self):
        self.current = (self.current + 1) % len(self.players)
        if self.current == 0:
            self.round += 1

    def is_over(self):
        return self.round > 13

    def winner(self):
        return max(self.players, key=lambda p: p.scorecard.get_total())