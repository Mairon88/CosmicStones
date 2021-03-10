class Markers():
    def __init__(self, name, joker, quantity, num_of_players):
        self.name = name
        self.joker = joker
        self.quantity = quantity
        self.num_of_players = num_of_players

    def sub_marker(self):
        if self.quantity > 0:
            self.quantity -= 1

    def add_marker(self):
        if self.quantity < self.num_of_players and self.name != 'gold':
            self.quantity += 1
        elif self.quantity < 5 and self.name == 'gold':
            self.quantity += 1
        else:
            pass

    def __str__(self):
        return self.name
