import  pygame

class Player():
    def __init__(self, name, window, player_coordinates):
        self.name = name # Nazwa gracza
        self.points = 0 # Punkty gracza
        self.markers = {} # Znaczniki gracza
        self.aristo_cards = [] # Karty arystokratów gracza
        self.stone_cards = [] # Karty kamieni gracza
        self.reserved_cards = [] # Zarezerwowane karty
        self.number_of_selected_markers = 0 # Zmienna pomocniczna, aktualna ilosc wybranych znacznikow z stolu podczas tury
        self.took_card = False # Czy wybrano kartę?
        self.bought_card = False # Czy kupiono kartę?
        self.window = window # Okno gry
        self.width_pos = player_coordinates[0]
        self.height_pos = player_coordinates[1]
        self.width_size = player_coordinates[2]
        self.height_size = player_coordinates[3] # Współrzędne ustawienia garacza na ekranie, do tych wartości
        # będziemy sie odnosic przy tworzeniu zasobów gracza

    def draw_player_board(self):
        pygame.draw.rect(self.window, (0, 50, 50), (self.width_pos, self.height_pos, self.width_size, self.height_size))  # P1 AREA

    def draw_player_markers(self):
        pass

    def draw_player_stone_cards(self):
        pass

    def draw_player_aristo_card(self):
        pass

    def draw_player_text(self):
        myfont = pygame.font.SysFont('ARIAL', 25)
        player_name = myfont.render(self.name.title(), True, (250, 255, 255))
        self.window.blit(player_name, (self.width_pos, self.height_pos))

        player_pts = myfont.render("Pts: "+str(self.points), True, (250, 255, 255))
        self.window.blit(player_pts, (self.width_pos+self.width_size*0.8, self.height_pos))


