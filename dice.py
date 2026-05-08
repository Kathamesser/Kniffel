import random

# Klasse
class Dice:
    # Attribute
    def __init__(self):
        self.value = random.randint(1, 6) # Zufallswert zwischen 1 und 6
        self.held = False # Würfel ist am Anfang nicht gehalten

    # Methoden
    def roll(self):
        if not self.held: # Nur würfeln wenn nicht gehalten
            self.value = random.randint(1, 6) # Neuer Zufallswert