# Pygame importieren 
import pygame

# Dice importieren
from dice import Dice

# Klasse 
class Cup():  
    # Attribute
    def __init__(self):
        self.dice = [Dice() for _ in range(5)] # Liste mit 5 Würfeln erstellen

    # Methoden 
    def roll_all(self): # Erster Zug mit allen Würfeln 
        for d in self.dice:
            d.held = False # Alle Würfel sind frei
            d.roll() # Alle Würfel werfen 

    def roll_unheld(self): # Zweiter und dritter Zug mit den übrigen Würfeln 
        for d in self.dice:
            d.roll()
    
    def get_values(self):
        return [d.value for d in self.dice]

    def reset(self):
        for d in self.dice:
            d.held = False

    
