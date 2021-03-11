import  pygame

class Player():
    def __init__(self, name, player_coordinates, width, height):
        self.name = name # Nazwa gracza
        self.points = 0 # Punkty gracza

        self.markers = {'emerald':0, 'sapphire':0,'ruby':0, 'diamond':0, 'onyx':0, 'gold':0} # Znaczniki gracza
        self.aristo_cards = [] # Karty arystokratów gracza

        self.stone_cards_em = [] # Karty kamieni gracza emerald
        self.stone_cards_sa = []  # Karty kamieni gracza sapphire
        self.stone_cards_ru = []  # Karty kamieni gracza ruby
        self.stone_cards_di = []  # Karty kamieni gracza diamond
        self.stone_cards_on = []  # Karty kamieni gracza onyx

        self.sum_of_stones_card_markers = {'emerald': 0, 'sapphire': 0, 'ruby': 0, 'diamond': 0, 'onyx': 0, 'gold': 0}

        self.reserved_cards = [] # Zarezerwowane karty
        self.number_of_selected_markers = 0 # Zmienna pomocniczna, aktualna ilosc wybranych znacznikow z stolu podczas tury
        self.num_of_all_markers = 0
        self.can_i_buy_sth = True
        self.took_card = False # Czy wybrano kartę?
        self.bought_card = False # Czy kupiono kartę?

        self.width_pos = player_coordinates[0]
        self.height_pos = player_coordinates[1]
        self.width_size = player_coordinates[2]
        self.height_size = player_coordinates[3] # Współrzędne ustawienia garacza na ekranie, do tych wartości
        # będziemy sie odnosic przy tworzeniu zasobów gracza
        self.stone_cards_width = width * 0.038
        self.stone_cards_height = height * 0.1
        self.marker_size = width * 0.038 / 2

        self.width = width
        self.height = height

        self.stone_cards_coordinates = []
        self.markers_coordinates = []
        self.reserved_cards_coordinates = []
        self.gold_markers_coordinates = []

        self.marker_padding_x = 0
        self.stone_cards_padding_x = 0
        self.reserved_stone_cards_padding_x = 0
        self.num_of_card_padding_x = 0
        self.num_of_markers_padding_x = 0

    def draw_player_board(self, window):
        pygame.draw.rect(window, (0, 50, 50), (self.width_pos, self.height_pos, self.width_size, self.height_size))  # P1 AREA

    def draw_player_markers(self, window):
        for i in range(5):
            if len(self.markers_coordinates) < 5:
                self.markers_coordinates.append([self.width_pos+self.marker_size*1.25+self.marker_padding_x*(self.marker_size*2+self.width*0.01),self.height_pos+self.height*0.23, self.marker_size])
            pygame.draw.circle(window, (150, 150, 150), (self.width_pos+self.marker_size*1.25+self.marker_padding_x*(self.marker_size*2+self.width*0.01),self.height_pos+self.height*0.23), self.marker_size, 0)
            self.marker_padding_x += 1
        self.marker_padding_x = 0

    def draw_player_gold_marker(self, window):
        if len(self.gold_markers_coordinates) < 1:
            self.gold_markers_coordinates.append([self.width_pos+self.marker_size*1.25+(self.marker_size*7+self.width*0.01),self.height_pos+self.height*0.343+ self.marker_size, self.marker_size])
        pygame.draw.circle(window, (150, 150, 150), (self.width_pos+self.marker_size*1.25+(self.marker_size*7+self.width*0.01),self.height_pos+self.height*0.343+self.marker_size), self.marker_size, 0)

    def draw_player_stone_cards(self, window):
        for i in range(5):
            # DODANIE WSPÓŁRZĘDNYCH KART GRACZA DO LISTY
            if len(self.stone_cards_coordinates) < 5:
                self.stone_cards_coordinates.append([self.width_pos+self.stone_cards_width*0.13+
                                (self.stone_cards_padding_x*(self.stone_cards_width+self.width*0.01)),self.height_pos+self.height*0.05,
                                                    self.stone_cards_width, self.stone_cards_height])
            # RYSOWANIE KART GRACZA
            pygame.draw.rect(window, (200, 150, 50),(self.width_pos+self.stone_cards_width*0.13+
                            (self.stone_cards_padding_x*(self.stone_cards_width+self.width*0.01)), self.height_pos+self.height*0.05,
                            self.stone_cards_width, self.stone_cards_height))  # P1 AREA
            self.stone_cards_padding_x += 1
        self.stone_cards_padding_x = 0


    def draw_player_reserved_stone_cards(self, window):
        for i in range(3):
            # DODANIE WSPÓŁRZĘDNYCH KART GRACZA DO LISTY
            if len(self.reserved_cards_coordinates) < 3:
                self.reserved_cards_coordinates.append([self.width_pos+self.stone_cards_width*0.13+
                                (self.reserved_stone_cards_padding_x*(self.stone_cards_width+self.width*0.01)),self.height_pos+self.height*0.31,
                                                    self.stone_cards_width, self.stone_cards_height])
            # RYSOWANIE KART GRACZA
            pygame.draw.rect(window, (200, 150, 50),(self.width_pos+self.stone_cards_width*0.13+
                            (self.reserved_stone_cards_padding_x*(self.stone_cards_width+self.width*0.01)), self.height_pos+self.height*0.31,
                            self.stone_cards_width, self.stone_cards_height))  # P1 AREA
            self.reserved_stone_cards_padding_x += 1
        self.reserved_stone_cards_padding_x = 0


    def draw_player_aristo_card(self):
        pass

    def draw_player_text(self, window):
        myfont = pygame.font.SysFont('ARIAL', 25)
        myfont2 = pygame.font.SysFont('ARIAL', 20)

        player_name = myfont.render(self.name.title(), True, (250, 255, 255))
        window.blit(player_name, (self.width_pos, self.height_pos))

        player_aristo = myfont.render("x" + str(len(self.aristo_cards)), True, (250, 255, 255))
        window.blit(player_aristo, (self.width_pos + self.width_size * 0.6, self.height_pos))

        player_pts = myfont.render("Pts: "+str(self.points), True, (250, 255, 255))
        window.blit(player_pts, (self.width_pos+self.width_size*0.8, self.height_pos))

        list_width_len_cards = [len(self.stone_cards_em),len(self.stone_cards_sa),len(self.stone_cards_ru),len(self.stone_cards_di),len(self.stone_cards_on)]

        for i in range(5):
            num_of_cards = myfont2.render("x" + str(list_width_len_cards[i]), True, (250, 255, 255))
            window.blit(num_of_cards, (self.width_pos+self.stone_cards_width*0.13+self.num_of_card_padding_x*(self.stone_cards_width+self.width*0.01), self.height_pos+self.height*0.15))
            self.num_of_card_padding_x += 1
        self.num_of_card_padding_x = 0


        for i in self.markers.keys():
            num_of_markers = myfont2.render("x" + str(self.markers[i]), True, (250, 255, 255))
            if i != 'gold':
                window.blit(num_of_markers, (self.width_pos+self.stone_cards_width*0.13+self.num_of_markers_padding_x*(self.stone_cards_width+self.width*0.01), self.height_pos+self.height*0.265))
                self.num_of_markers_padding_x += 1
            elif i == 'gold':
                window.blit(num_of_markers, (
                self.width_pos + self.stone_cards_width * 0.13 + 3 * (
                            self.stone_cards_width + self.width * 0.01), self.height_pos + self.height * 0.413))
                self.num_of_markers_padding_x += 1

        self.num_of_markers_padding_x = 0


    def check_num_of_player_markers(self):
        self.num_of_all_markers = sum([self.markers['emerald'],self.markers['sapphire'],self.markers['ruby'],self.markers['diamond'],self.markers['onyx'],self.markers['gold']])
        return self.num_of_all_markers


    def choose_player_marker(self, mouse_pos, markers):
        for position in self.markers_coordinates:
            # SPRAWDZAMY CZY KURSOR ZNAJDUJE SIE WEWNATRZ OKREGU SYMBOLIZUJACEGO ZNACZNIK
            pos_indx = self.markers_coordinates.index(position)
            pos_indx_key = list(self.markers.keys())[pos_indx]
            delta_x = mouse_pos[0] - position[0]
            delta_y = mouse_pos[1] - position[1]
            dsp = pow((pow(delta_x, 2) + pow(delta_y, 2)), 0.5)

            # WARUNEK SPRAWDZAJACY CZY KURSOR MYSZY ZNAJDUJE SIE NA ZNACZNIKU
            # JEŚLI WSZYSTKIE WARUNKI SĄ SPEŁNIONE MOZNA USUNĄĆ NADMIAR ZNACZNIKÓW
            if dsp < self.marker_size and self.markers[pos_indx_key] > 0:
                self.markers[pos_indx_key] -= 1
                markers[pos_indx].add_marker()

    def can_i_afford_it(self,card):
        for key in card[0].stones.keys():
            if card[0].stones[key] > self.markers[key]:
                print("Nie stać Cię")
                return False
        print("Karta kupiona")
        return True




        # print("Czy mnie na to stać???")
        # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Wymagania dla kart I poziomu >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # for i in line_lvl1:
        #     print(i[0].name, i[0].stones)
        #     for key_lvl1 in i[0].stones.keys():
        #         if i[0].stones[key_lvl1] > self.sum_of_stones_card_markers[key_lvl1]:
        #             print("Nie stać Cię")
        #             continue
        #     print("Stać Cię na tą kartę")
        # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Wymagania dla kart II poziomu >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # for j in line_lvl2:
        #     print(j[0].name, j[0].stones)
        #     for key_lvl2 in j[0].stones.keys():
        #         if j[0].stones[key_lvl2] > self.sum_of_stones_card_markers[key_lvl2]:
        #             print("Nie stać Cię")
        #             continue
        #         print("Stać Cię na tą kartę")
        # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Wymagania dla kart III poziomu >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # for k in line_lvl3:
        #     print(k[0].name, k[0].stones)
        #     for key_lvl3 in k[0].stones.keys():
        #         if k[0].stones[key_lvl3] > self.sum_of_stones_card_markers[key_lvl3]:
        #             print("Nie stać Cię")
        #             break
        #     print("Stać Cię na tą kartę")

        # JEŚLI WARUNKI ZOSTANA SPEŁNIONE TO
        # self.can_i_buy_sth = True

    def update_sum_of_stones(self):
        self.sum_of_stones_card_markers['emerald'] = self.markers['emerald'] + len(self.stone_cards_em)
        self.sum_of_stones_card_markers['sapphire'] = self.markers['sapphire'] + len(self.stone_cards_sa)
        self.sum_of_stones_card_markers['ruby'] = self.markers['ruby'] + len(self.stone_cards_ru)
        self.sum_of_stones_card_markers['diamond'] = self.markers['diamond'] + len(self.stone_cards_di)
        self.sum_of_stones_card_markers['onyx'] = self.markers['onyx'] + len(self.stone_cards_on)
        self.sum_of_stones_card_markers['gold'] = self.markers['gold']






