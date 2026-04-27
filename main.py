import pygame
pygame.init()

# Überschrift (Fenstertitel setzen)
pygame.display.set_caption("Kniffel")

running = True # Hauptschleife läuft solange True ist

width = 600 # Breite vom Fenster
height = 800 # Höhe vom Fenster

# Fenster setzen 
window = pygame.display.set_mode((width, height))