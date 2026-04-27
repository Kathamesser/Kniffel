import pygame

import random 

class Dice(): # Klasse
    def __init__(self, value = 1, size = 60, color = (255,255,255), x = 0, y = 0): # Konstruktor
        self.value = value 
        self.size = size 
        self.color = color
        self.position_x = x
        self.position_y = y
    
    # Methoden
    def roll_dice(self): # Würfeln 
        self.value = random.randint(1-6)

    def show_value(self): # Ergebnis anzeigen
        print(self.value)
