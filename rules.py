from collections import Counter


# Klasse
class Rules:
    # Methoden
    def score(self, category, dice):
        d = [x.value for x in dice] # Werte aus Wuerfeln holen
        counts = Counter(d)
        unique_values = set(d)

        if category == "ones": return d.count(1) * 1
        if category == "twos": return d.count(2) * 2
        if category == "threes": return d.count(3) * 3
        if category == "fours": return d.count(4) * 4
        if category == "fives": return d.count(5) * 5
        if category == "sixes": return d.count(6) * 6

        if category == "three_of_a_kind":
            return sum(d) if max(counts.values()) >= 3 else 0

        if category == "four_of_a_kind":
            return sum(d) if max(counts.values()) >= 4 else 0

        if category == "fullhouse":
            return 25 if sorted(counts.values()) == [2, 3] else 0

        if category == "small_straight":
            straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
            return 30 if any(straight.issubset(unique_values) for straight in straights) else 0

        if category == "large_straight":
            return 40 if unique_values in ({1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}) else 0

        if category == "kniffel":
            return 50 if len(unique_values) == 1 else 0 # alle gleich

        if category == "chance": return sum(d)

        return 0
