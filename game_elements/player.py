import pygame


class Player():
    def __init__(self, name, player_coordinates, width, height):
        self.name = name # Nazwa gracza
        self.points = 0 # Punkty gracza

        self.markers = {'emerald':0, 'sapphire':0,'ruby':0, 'diamond':0, 'onyx':0, 'gold':0} # Znaczniki gracza
        self.aristo_cards = [] # Karty arystokratów gracza
        self.safe_gold = 0
        self.use_gold = 0
        self.stone_cards_em = [] # Karty kamieni gracza emerald
        self.stone_cards_sa = []  # Karty kamieni gracza sapphire
        self.stone_cards_ru = []  # Karty kamieni gracza ruby
        self.stone_cards_di = []  # Karty kamieni gracza diamond
        self.stone_cards_on = []  # Karty kamieni gracza onyx

        self.cards = {'emerald':0, 'sapphire':0,'ruby':0, 'diamond':0, 'onyx':0,}
        self.sum_of_stones_card_markers = {'emerald': 0, 'sapphire': 0, 'ruby': 0, 'diamond': 0, 'onyx': 0}

        self.reserved_cards = [[],[],[]] # Zarezerwowane karty
        self.number_of_selected_markers = 0 # Zmienna pomocniczna, aktualna ilosc wybranych znacznikow z stolu podczas tury
        self.num_of_all_markers = 0

        self.took_card = True # Czy wybrano kartę?
        self.reserve_card = False # Czy zarezerwowano kartę?
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
        list_of_markers = ['emerald_m.png', 'sapphire_m.png', 'ruby_m.png', 'diamond_m.png', 'onyks_m.png',
                           'gold_m.png']
        for i in range(5):
            if len(self.markers_coordinates) < 5:
                self.markers_coordinates.append([self.width_pos+self.marker_size*1.25+self.marker_padding_x*(self.marker_size*2+self.width*0.01),self.height_pos+self.height*0.23, self.marker_size])
            markers = pygame.draw.circle(window, (0, 0, 0), (self.width_pos+self.marker_size*1.25+self.marker_padding_x*(self.marker_size*2+self.width*0.01),self.height_pos+self.height*0.23), self.marker_size, 1)
            img = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/' + list_of_markers[i])
            img = pygame.transform.scale(img, (int(self.marker_size*2), int(self.marker_size*2)))
            window.blit(img, markers)
            self.marker_padding_x += 1
        self.marker_padding_x = 0

    def draw_player_gold_marker(self, window):
        list_of_markers = ['emerald_m.png', 'sapphire_m.png', 'ruby_m.png', 'diamond_m.png', 'onyks_m.png',
                           'gold_m.png']
        if len(self.gold_markers_coordinates) < 1:
            self.gold_markers_coordinates.append([self.width_pos+self.marker_size*1.25+(self.marker_size*8+self.width*0.01),self.height_pos+self.height*0.343+ self.marker_size, self.marker_size])
        markers = pygame.draw.circle(window, (0, 0, 0), (self.width_pos+self.marker_size*1.25+(self.marker_size*9.5+self.width*0.01),self.height_pos+self.height*0.343+self.marker_size), self.marker_size, 0)
        img = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/' + list_of_markers[-1])
        img = pygame.transform.scale(img, (int(self.marker_size * 2), int(self.marker_size * 2)))
        window.blit(img, markers)

    def draw_player_stone_cards(self, window):
        list_of_cards = ['em_pl.png', 'sa_pl.png', 'ru_pl.png', 'di_pl.png', 'on_pl.png']
        for i in range(5):
            # DODANIE WSPÓŁRZĘDNYCH KART GRACZA DO LISTY
            if len(self.stone_cards_coordinates) < 5:
                self.stone_cards_coordinates.append([self.width_pos+self.stone_cards_width*0.13+
                                (self.stone_cards_padding_x*(self.stone_cards_width+self.width*0.01)),self.height_pos+self.height*0.05,
                                                    self.stone_cards_width, self.stone_cards_height])
            # RYSOWANIE KART GRACZA
            cards = pygame.draw.rect(window, (200, 150, 50),(self.width_pos+self.stone_cards_width*0.13+
                            (self.stone_cards_padding_x*(self.stone_cards_width+self.width*0.01)), self.height_pos+self.height*0.05,
                            self.stone_cards_width, self.stone_cards_height),1)  # P1 AREA
            img = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/' + list_of_cards[i])
            img = pygame.transform.scale(img, (int(self.stone_cards_width), int(self.stone_cards_height)))
            window.blit(img, cards)
            self.stone_cards_padding_x += 1
        self.stone_cards_padding_x = 0


    def draw_player_reserved_stone_cards(self, window):
        for i in range(3):
            # DODANIE WSPÓŁRZĘDNYCH KART GRACZA DO LISTY
            if len(self.reserved_cards_coordinates) < 3:
                self.reserved_cards_coordinates.append([self.width_pos+self.stone_cards_width*0.13+
                                (self.reserved_stone_cards_padding_x*(self.stone_cards_width+self.width*0.025)),self.height_pos+self.height*0.31,
                                                    self.stone_cards_width*1.5, self.stone_cards_height*1.35])
            # RYSOWANIE KART GRACZA
            pygame.draw.rect(window, (200, 150, 50),(self.width_pos+self.stone_cards_width*0.13+
                            (self.reserved_stone_cards_padding_x*(self.stone_cards_width+self.width*0.025)), self.height_pos+self.height*0.31,
                            self.stone_cards_width*1.5, self.stone_cards_height*1.35),1)  # P1 AREA
            self.reserved_stone_cards_padding_x += 1
        self.reserved_stone_cards_padding_x = 0


    def draw_player_aristo_card(self):
        pass

    def draw_player_text(self, window):
        name_list = ['EME', 'SAP', 'RUB', 'DIA', 'ONY']
        myfont = pygame.font.SysFont('ARIAL', 25)
        myfont2 = pygame.font.SysFont('ARIAL', 20)
        myfont3 = pygame.font.SysFont('ARIAL', 15)

        player_name = myfont.render(self.name.title(), True, (250, 255, 255))
        window.blit(player_name, (self.width_pos, self.height_pos))

        player_aristo = myfont.render("x" + str(len(self.aristo_cards)), True, (250, 255, 255))
        window.blit(player_aristo, (self.width_pos + self.width_size * 0.6, self.height_pos))

        player_pts = myfont.render("Pts: "+str(self.points), True, (250, 255, 255))
        window.blit(player_pts, (self.width_pos+self.width_size*0.8, self.height_pos))

        list_width_len_cards = [len(self.stone_cards_em),len(self.stone_cards_sa),len(self.stone_cards_ru),len(self.stone_cards_di),len(self.stone_cards_on)]

        # WYŚWIETLANIE ILOSCI KART DANEGO KAMIENIA
        for i in range(5):
            num_of_cards = myfont2.render("x" + str(list_width_len_cards[i]), True, (250, 255, 255))
            window.blit(num_of_cards, (self.width_pos+self.stone_cards_width*0.13+self.num_of_card_padding_x*(self.stone_cards_width+self.width*0.01), self.height_pos+self.height*0.15))
            self.num_of_card_padding_x += 1
        self.num_of_card_padding_x = 0

        # ROBOCZY OPIS KART

        for i in range(5):
            name_of_cards = myfont2.render(str(name_list[i]), True, (250, 255, 255))
            window.blit(name_of_cards, (self.width_pos+self.stone_cards_width*0.3+self.num_of_card_padding_x*(self.stone_cards_width+self.width*0.01), self.height_pos+self.height*0.08))
            self.num_of_card_padding_x += 1
        self.num_of_card_padding_x = 0


        for i in self.markers.keys():
            num_of_markers = myfont2.render("x" + str(self.markers[i]), True, (250, 255, 255))
            if i != 'gold':
                window.blit(num_of_markers, (self.width_pos+self.stone_cards_width*0.13+self.num_of_markers_padding_x*(self.stone_cards_width+self.width*0.01), self.height_pos+self.height*0.265))
                self.num_of_markers_padding_x += 1
            elif i == 'gold':
                window.blit(num_of_markers, (
                self.width_pos + self.stone_cards_width * 0.13 + 4 * (
                            self.stone_cards_width + self.width * 0.01), self.height_pos + self.height * 0.413))
                self.num_of_markers_padding_x += 1

        self.num_of_markers_padding_x = 0

        c = 0



        for i in self.reserved_cards_coordinates:
            if self.reserved_cards[c] != []:
                draw_card = pygame.draw.rect(window, (150, 150, 150), i)
                img = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/' + self.reserved_cards[c][0].images)
                img = pygame.transform.scale(img, (int(i[2]), int(i[3])))
                window.blit(img, draw_card)
                # text = self.reserved_cards[c][0].name  # nazwa karty zgodnie z kamieniem
                # text_x_y = (i)  # Położenie tekstu na ekranie
                # game_name = myfont3.render(text, True, (250, 255, 255))
                # window.blit(game_name, text_x_y)
                # z = 0
                # text_bonus = str("bonus: "+str(self.reserved_cards[c][0].bonus)) # Tytył gry
                # text_x_y = (i[0], i[1] + 25 + z * 25)  # Położenie tekstu na ekranie
                # game_name = myfont3.render(text_bonus, True, (250, 255, 255))
                # window.blit(game_name, text_x_y)
                # for key, value in self.reserved_cards[c][0].stones.items():
                #     text = str(key)+" "+str(value)  # Tytył gry
                #
                #     text_x_y = (i[0],i[1]+50+z*25)  # Położenie tekstu na ekranie
                #     game_name = myfont3.render(text, True, (250, 255, 255))
                #     window.blit(game_name, text_x_y)
                #     z += 1
            c+=1



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

    # FUNKCJA SPRAWDZA CZY STAC MNIE NA KARTE, NAJPIERW Z ZASOBÓW KART I KAMIENI A POZNIEJ Z DODATKIEM ZŁOTA
    def can_i_afford_it(self,card):
        print(f"TA KARTA MIAŁA TAKIE WYMAGANIA: {card[0].stones}")
        new_stone_requirements = {}
        self.use_gold = 0
        self.safe_gold = self.markers['gold']
        for key in card[0].stones.keys():
            if card[0].stones[key] > self.sum_of_stones_card_markers[key]:
                print("Sprawdzam czy masz złoto")
                if self.safe_gold > 0:
                    if card[0].stones[key] > self.sum_of_stones_card_markers[key] + self.safe_gold:
                        print("Nie stać Cię")
                        return False
                    else:
                        cost = card[0].stones[key] - self.sum_of_stones_card_markers[key]
                        if self.safe_gold >= cost:
                            self.safe_gold -= cost
                            self.use_gold += cost

                            marker_requirements =  card[0].stones[key] - self.cards[key] - cost
                            new_stone_requirements.setdefault(key,marker_requirements)
                        else:
                            print("Nie stać Cię masz za mało złota")
                            return False
                else:
                    print("Nie stać Cię, mało brakowało")
                    return False


        for key in new_stone_requirements.keys():
            card[0].stones[key] = new_stone_requirements[key]
        self.markers['gold'] -= self.use_gold
        print(f"A TERAZ MA TAKIE: {card[0].stones}")
        print("Karta kupiona")

        return True

    def pay_for_card(self, card, markers_on_table):
        print("Muszę oddać")
        print(f"PŁACE CA KARTĘ:{card.stones}")
        markers_on_table[5].quantity += self.use_gold
        for key, value in card.stones.items():
            print(self.markers[key])
            cost = value - (self.sum_of_stones_card_markers[key] - self.markers[key])
            if cost > 0:
                self.markers[key] -= cost
                for marker in markers_on_table:
                    if marker.name == key:
                        marker.quantity += cost

    def update_sum_of_stones(self):
        self.cards = {'emerald':len(self.stone_cards_em), 'sapphire':len(self.stone_cards_sa),
                      'ruby':len(self.stone_cards_ru), 'diamond':len(self.stone_cards_di), 'onyx':len(self.stone_cards_on)}
        self.sum_of_stones_card_markers['emerald'] = self.markers['emerald'] + len(self.stone_cards_em)
        self.sum_of_stones_card_markers['sapphire'] = self.markers['sapphire'] + len(self.stone_cards_sa)
        self.sum_of_stones_card_markers['ruby'] = self.markers['ruby'] + len(self.stone_cards_ru)
        self.sum_of_stones_card_markers['diamond'] = self.markers['diamond'] + len(self.stone_cards_di)
        self.sum_of_stones_card_markers['onyx'] = self.markers['onyx'] + len(self.stone_cards_on)
        # self.sum_of_stones_card_markers['gold'] = self.markers['gold']

    # METODA SPRAWDZAJACA PRZYJECIE ARYSTOKRATY
    def invate_aristo(self, card_a, coordinates_a_card):
        for card in card_a:
            index = card_a.index(card)
            positive_need_aristo = 0 # pomocniczna zmienna do sprawdzenia ile pozytywnych wymogów mamy

            for key in card.needs.keys():
                if card.needs[key] != self.cards[key]:
                    print("Nie Przyjmujemy arystokraty")
                    break
                else:
                    positive_need_aristo +=1
            if positive_need_aristo == len(card.needs.keys()):
                print("Przyjmuję ARYSTOKRATĘ!!!\n"*10)
                self.aristo_cards.append(card)
                card_a.pop(index)
                coordinates_a_card.pop(index)
        return card_a, coordinates_a_card


    def count_pts(self):
        self.points += len(self.aristo_cards)*3
        for em in self.stone_cards_em:
            self.points += em.bonus
        for sa in self.stone_cards_sa:
            self.points += sa.bonus
        for ru in self.stone_cards_ru:
            self.points += ru.bonus
        for di in self.stone_cards_di:
            self.points += di.bonus
        for on in self.stone_cards_on:
            self.points += on.bonus









