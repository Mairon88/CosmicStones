class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.markers = {}
        self.aristo_cards = []
        self.stone_cards = []
        self.reserved_cards = 0
        self.number_of_selected_markers = 0
        self.took_card = False
        self.bought_card = False



