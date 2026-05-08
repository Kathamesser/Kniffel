# Pygame importieren 
import pygame 

from score import ScoreCard

class Player:
    def __init__(self, name):
        self.name = name
        self.rolls_left = 3
        self.scorecard = ScoreCard()

    def reset_rolls(self):
        self.rolls_left = 3

    def roll_dice(self, cup):
        if self.rolls_left > 0:
            cup.roll_unheld()
            self.rolls_left -= 1