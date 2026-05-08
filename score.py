class Score:
    UPPER_CATEGORIES = ("ones", "twos", "threes", "fours", "fives", "sixes")

    def __init__(self):
        self.used = {}

    def set(self, category, value):
        self.used[category] = value

    def bonus(self):
        upper_total = sum(self.used.get(category, 0) for category in self.UPPER_CATEGORIES)
        return 35 if upper_total >= 63 else 0

    def total(self):
        return sum(self.used.values()) + self.bonus()

    def get_total(self):
        return self.total()
