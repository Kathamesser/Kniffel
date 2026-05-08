from collections import Counter

# Klasse
class Rules:
    # Methoden
    def score(self, category, dice):
        d = [x.value for x in dice] # Werte aus Würfeln holen

        if category == "ones": return d.count(1) * 1
        if category == "twos": return d.count(2) * 2
        if category == "threes": return d.count(3) * 3
        if category == "fours": return d.count(4) * 4
        if category == "fives": return d.count(5) * 5
        if category == "sixes": return d.count(6) * 6

        if category == "chance": return sum(d)

        if category == "kniffel":
            return 50 if len(set(d)) == 1 else 0 # alle gleich

        if category == "full":
            return 25 if sorted(Counter(d).values()) == [2, 3] else 0

        return 0