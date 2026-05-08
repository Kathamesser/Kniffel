# Klasse
class Score:
    # Attribute
    def __init__(self):
        self.used = {} # gespeicherte Kategorien + Punkte

    # Methoden
    def set(self, category, value):
        self.used[category] = value # Kategorie speichern

    def total(self):
        return sum(self.used.values()) # Gesamtscore berechnen