import pygame
from dice import Dice
from rules import Rules
from score import Score

pygame.init()

# Fenster
WIDTH, HEIGHT = 600, 800 # Größe
window = pygame.display.set_mode((WIDTH, HEIGHT)) # Fenster erstellen
pygame.display.set_caption("Kniffel") # Titel setzen

font = pygame.font.SysFont(None, 32)

# Objekte erstellen
dice = [Dice() for _ in range(5)] # 5 Würfel
rules = Rules() # Regeln
score = Score() # Score

# Spielvariablen
categories = ["ones","twos","threes","fours","fives","sixes","full","kniffel","chance"]
rolls_left = 3 # Würfe pro Runde

running = True # Hauptschleife


# Funktion: Würfeln
def roll_dice():
    global rolls_left
    if rolls_left > 0:
        for d in dice:
            d.roll() # Würfel werfen
        rolls_left -= 1 # Würfe reduzieren


# Spielschleife
while running:
    window.fill((30, 30, 30)) # Hintergrund

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Spiel beenden

        # Würfel anklicken
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            for i, d in enumerate(dice):
                dx = 100 + i * 90
                dy = 200

                if dx < x < dx + 60 and dy < y < dy + 60:
                    d.held = not d.held # Würfel halten / lösen

        # Tastatur
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                roll_dice() # würfeln

            # Kategorie wählen
            if pygame.K_1 <= event.key <= pygame.K_9:
                idx = event.key - pygame.K_1

                if idx < len(categories):
                    cat = categories[idx]

                    if cat not in score.used:
                        value = rules.score(cat, dice)
                        score.set(cat, value)

                        rolls_left = 3 # neue Runde

                        for d in dice:
                            d.held = False # Reset Würfel

    # Würfel zeichnen
    for i, d in enumerate(dice):
        x = 100 + i * 90
        y = 200

        color = (200, 50, 50) if d.held else (255, 255, 255)

        pygame.draw.rect(window, color, (x, y, 60, 60)) # Würfel
        text = font.render(str(d.value), True, (0, 0, 0))
        window.blit(text, (x + 20, y + 15))

    # Fenster
    window.blit(font.render(f"Rolls: {rolls_left}", True, (255,255,255)), (20, 20))
    window.blit(font.render(f"Score: {score.total()}", True, (255,255,255)), (20, 60))

    # Kategorien anzeigen
    for i, c in enumerate(categories):
        text = font.render(f"{i+1}:{c}", True, (200,200,200))
        window.blit(text, (350, 150 + i * 25))

    pygame.display.update() # Bildschirm aktualisieren

pygame.quit() # Pygame beenden 