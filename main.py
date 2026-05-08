import pygame
from dice import Dice
from rules import Rules
from score import Score

pygame.init()

# Fenster
WIDTH, HEIGHT = 800, 800 # Groesse
window = pygame.display.set_mode((WIDTH, HEIGHT)) # Fenster erstellen
pygame.display.set_caption("Kniffel") # Titel setzen

DIE_SIZE = 60
DIE_GAP = 30
DICE_START_X = (WIDTH - (5 * DIE_SIZE + 4 * DIE_GAP)) // 2
DICE_Y = 200

SCORE_BLOCK_WIDTH = 270
SCORE_BLOCK_HEIGHT = 300
SCORE_BLOCK_GAP = 90
SCORE_BLOCK_TOP = 375
SCORE_BLOCK_LEFT = (WIDTH - (2 * SCORE_BLOCK_WIDTH + SCORE_BLOCK_GAP)) // 2
SCORE_LEFT_X = SCORE_BLOCK_LEFT + 15
SCORE_RIGHT_X = SCORE_BLOCK_LEFT + SCORE_BLOCK_WIDTH + SCORE_BLOCK_GAP + 15
SCORE_ROW_Y = SCORE_BLOCK_TOP + 15
DARK_GRAY = (70, 70, 70)

font = pygame.font.SysFont(None, 32)
small_font = pygame.font.SysFont(None, 26)

# Objekte erstellen
dice = [Dice() for _ in range(5)] # 5 Wuerfel
rules = Rules() # Regeln
score = Score() # Score

# Spielvariablen
categories = [
    "ones",
    "twos",
    "threes",
    "fours",
    "fives",
    "sixes",
    "three_of_a_kind",
    "four_of_a_kind",
    "fullhouse",
    "small_straight",
    "large_straight",
    "kniffel",
    "chance",
]
category_names = {
    "ones": "Einser",
    "twos": "Zweier",
    "threes": "Dreier",
    "fours": "Vierer",
    "fives": "Fuenfer",
    "sixes": "Sechser",
    "three_of_a_kind": "Dreierpasch",
    "four_of_a_kind": "Viererpasch",
    "fullhouse": "Fullhouse",
    "small_straight": "Kleine Strasse",
    "large_straight": "Grosse Strasse",
    "kniffel": "Kniffel",
    "chance": "Chance",
}
category_keys = [
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9,
    pygame.K_q,
    pygame.K_w,
    pygame.K_e,
    pygame.K_r,
]
category_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Q", "W", "E", "R"]
upper_categories = categories[:6]
lower_categories = categories[6:]
rolls_left = 3 # Wuerfe pro Runde
has_rolled_this_turn = False

running = True # Hauptschleife


def draw_text(text, pos, color=(255, 255, 255), text_font=font):
    window.blit(text_font.render(text, True, color), pos)


def draw_score_row(category, x, y):
    key = category_labels[categories.index(category)]
    value = score.used.get(category, "-")
    color = (170, 170, 170) if category in score.used else (230, 230, 230)
    draw_text(f"{key}  {category_names[category]}", (x, y), color, small_font)
    draw_text(str(value), (x + 190, y), color, small_font)


def draw_score_block(block_categories, x, y):
    pygame.draw.rect(window, (48, 48, 54), (x - 15, y - 15, SCORE_BLOCK_WIDTH, SCORE_BLOCK_HEIGHT), border_radius=8)
    pygame.draw.rect(window, DARK_GRAY, (x - 15, y - 15, SCORE_BLOCK_WIDTH, SCORE_BLOCK_HEIGHT), 2, border_radius=8)

    for i, category in enumerate(block_categories):
        draw_score_row(category, x, y + i * 30)


def draw_die(value, x, y, held):
    color = (235, 95, 95) if held else (245, 245, 245)
    pygame.draw.rect(window, color, (x, y, DIE_SIZE, DIE_SIZE), border_radius=10)
    pygame.draw.rect(window, (25, 25, 25), (x, y, DIE_SIZE, DIE_SIZE), 2, border_radius=10)

    pip_positions = {
        "top_left": (x + 17, y + 17),
        "top_right": (x + 43, y + 17),
        "middle_left": (x + 17, y + 30),
        "center": (x + 30, y + 30),
        "middle_right": (x + 43, y + 30),
        "bottom_left": (x + 17, y + 43),
        "bottom_right": (x + 43, y + 43),
    }
    pips_by_value = {
        1: ["center"],
        2: ["top_left", "bottom_right"],
        3: ["top_left", "center", "bottom_right"],
        4: ["top_left", "top_right", "bottom_left", "bottom_right"],
        5: ["top_left", "top_right", "center", "bottom_left", "bottom_right"],
        6: ["top_left", "top_right", "middle_left", "middle_right", "bottom_left", "bottom_right"],
    }

    for pip in pips_by_value[value]:
        pygame.draw.circle(window, (15, 15, 15), pip_positions[pip], 5)


def draw_empty_die(x, y):
    pygame.draw.rect(window, (245, 245, 245), (x, y, DIE_SIZE, DIE_SIZE), border_radius=10)
    pygame.draw.rect(window, (25, 25, 25), (x, y, DIE_SIZE, DIE_SIZE), 2, border_radius=10)


# Funktion: Wuerfeln
def roll_dice():
    global rolls_left, has_rolled_this_turn
    if rolls_left > 0:
        for d in dice:
            d.roll() # Wuerfel werfen
        rolls_left -= 1 # Wuerfe reduzieren
        has_rolled_this_turn = True


# Spielschleife
while running:
    window.fill((220, 220, 220)) # Hintergrund

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Spiel beenden

        # Wuerfel anklicken
        if event.type == pygame.MOUSEBUTTONDOWN and has_rolled_this_turn:
            x, y = pygame.mouse.get_pos()

            for i, d in enumerate(dice):
                dx = DICE_START_X + i * (DIE_SIZE + DIE_GAP)
                dy = DICE_Y

                if dx < x < dx + DIE_SIZE and dy < y < dy + DIE_SIZE:
                    d.held = not d.held # Wuerfel halten / loesen

        # Tastatur
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                roll_dice() # wuerfeln

            # Kategorie waehlen
            if event.key in category_keys:
                idx = category_keys.index(event.key)

                if idx < len(categories):
                    cat = categories[idx]

                    if cat not in score.used and has_rolled_this_turn:
                        value = rules.score(cat, dice)
                        score.set(cat, value)

                        rolls_left = 3 # neue Runde
                        has_rolled_this_turn = False

                        for d in dice:
                            d.held = False # Reset Wuerfel

    # Wuerfel zeichnen
    for i, d in enumerate(dice):
        x = DICE_START_X + i * (DIE_SIZE + DIE_GAP)
        y = DICE_Y
        if has_rolled_this_turn:
            draw_die(d.value, x, y, d.held)
        else:
            draw_empty_die(x, y)

    # Fenster
    draw_text(f"Rolls: {rolls_left}", (20, 20), DARK_GRAY)
    draw_text(f"Score: {score.total()}", (20, 60), DARK_GRAY)

    # Kategorien anzeigen
    draw_score_block(upper_categories, SCORE_LEFT_X, SCORE_ROW_Y)
    bonus_color = (120, 220, 150) if score.bonus() else (190, 190, 190)
    draw_text("Bonus", (SCORE_LEFT_X, SCORE_ROW_Y + 190), bonus_color, small_font)
    draw_text(str(score.bonus()), (SCORE_LEFT_X + 190, SCORE_ROW_Y + 190), bonus_color, small_font)

    draw_score_block(lower_categories, SCORE_RIGHT_X, SCORE_ROW_Y)

    pygame.display.update() # Bildschirm aktualisieren

pygame.quit() # Pygame beenden
