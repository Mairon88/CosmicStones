import draw.characters as char
import game_elements.player as plr
import game_elements.stone_markers as mrk
import game_elements.aristocrat_cards as aric
import random


# FUNKCJA DO PODAWANIA ILOSCI GRACZY
def enter_num_of_pl():
    number_of_players = char.num
    return number_of_players


# FUNKCJA TWORZACA OBIEKTY GRACZY
def create_players(number_of_players, list_of_players):
    if number_of_players is not None:
        if len(list_of_players) < number_of_players:
            for i in range(number_of_players):
                list_of_players.append(plr.Player("No_Name"))


# FUNKCJA DO PODAWANIA IMION GRACZY
def enter_player_names(confirm_name, list_of_players):
    list_of_players[confirm_name].name = char.word


# FUNKCJA TWORZACA ZNACZNIKI
def create_markers(prepare_markers, num_of_players):
    markers = []
    if num_of_players == 4:
        n = 7
    elif num_of_players == 3:
        n = 5
    else:
        n = 4
    for stone in prepare_markers:
        if stone[0] == 'gold':
            n = 5
        markers.append(mrk.Markers(stone[0],stone[1], n, num_of_players))
    return markers


# FUNKCJA TWORZACA KARTY ARYSTOKRATÓW
def create_aristo(prepare_aristo, num_of_players):
    aristo = []
    if num_of_players == 4:
        n = 5
    elif num_of_players == 3:
        n = 4
    else:
        n = 3

    # LOSOWANIE KILKU KART ARYSTOKRATOW ZGODNIE Z LICZBA GRACZ
    cards = random.sample(prepare_aristo, k=n)

    # TWORZENIE OBIEKTOW KART ARYSTOKRATOW
    for card in cards:
        aristo.append(aric.Aristo(card[0], card[1]))

    return aristo

# FUNKCJA WYZNACZAJĄCA WSPÓŁRZĘDNE DLA KART - PRZYDA SIE W RYSOWANIU I W WARUNKACH PRZY
# KLIKANIU MYSZKĄ
# LICZBY PRZEZ KTÓRE SĄ MNOŻONE SZEROKOŚCI I WYSOKOSCI TO PROCENTOWE POZYCJE LUB WYMIARY

# WYZNACZANIE WSPÓŁRZĘDNYCH KART DLA DANYCH POZIOMÓW
def card_coordinates(width, height, card_a_height_size, card_width_size, card_height_size, padding_x, padding_y, ilosc, level, element):
    coordinates_list = []
    if element == 'card':
        for i in range(ilosc):
            coordinates_list.append((width * 0.2711 + padding_x, height*0.0408+card_a_height_size + level*padding_y+(level-1)*card_height_size, card_width_size, card_height_size))  # P1 AREA
            padding_x += card_width_size/2 + width * 0.056
    elif element == 'marker':
        for i in range(ilosc):
            coordinates_list.append((width * 0.2711 +height*0.06+ padding_x, height*0.0408+card_a_height_size + level*padding_y+(level-1)*card_height_size + height * 0.075))  # P1 AREA
            padding_x += card_width_size/2 + width * 0.039
    return coordinates_list

# UZUPEŁNIANIE KART NA STOLE Z STOSU W ZALEŻNOŚCI OD POZIOMU
def place_the_card(card_lvl_1,card_lvl_2,card_lvl_3, line_lvl1, line_lvl2, line_lvl3):
    # Uzupełnianie kart poziomu trzeciego
    if [] in line_lvl3 and len(card_lvl_3)>0:
        for i in line_lvl3:
            if i == []:
                card3 = card_lvl_3.pop()
                indx = line_lvl3.index([])
                line_lvl3[indx].append(card3)

    if [] in line_lvl2 and len(card_lvl_2)>0:
        for i in line_lvl2:
            if i == []:
                card2 = card_lvl_2.pop()
                indx = line_lvl2.index([])
                line_lvl2[indx].append(card2)

    if [] in line_lvl1 and len(card_lvl_1)>0:
        for i in line_lvl1:
            if i == []:
                card1 = card_lvl_1.pop()
                indx = line_lvl1.index([])
                line_lvl1[indx].append(card1)

    return card_lvl_1,card_lvl_2,card_lvl_3, line_lvl1, line_lvl2, line_lvl3

# WYBIERANIE KARTY I USUWANIE JEJ Z STOŁU, PO CZYM UZUPEŁNIE Z STOSU ZGODNIE Z FUNKCJA POWYZEJ place_the_card
def choose_card(coordinates_card_lvl_1, coordinates_card_lvl_2, coordinates_card_lvl_3, line_lvl1, line_lvl2,
                line_lvl3, mouse_pos):
    # CHECK LINE LVL3
    for position3 in coordinates_card_lvl_3:
        pos_indx = coordinates_card_lvl_3.index(position3)
        if pos_indx == 0:   # POZYCJA O INDEKSIE 0 ODNOSI SIE DO STOSU A POTRZEBUJEMY WYŁACZNIE KARTY NA STOLE
            continue
        else:
            # POZYCJE I WYMIARY PIERWSZEJ KARTY POTRZBNE DO WARUNKU KLIKNIECIA W NIA
            pos_x = coordinates_card_lvl_3[pos_indx][0]
            pos_y = coordinates_card_lvl_3[pos_indx][1]
            size_x = coordinates_card_lvl_3[pos_indx][2]
            size_y = coordinates_card_lvl_3[pos_indx][3]

            # WARUNEK SPRAWDZAJACY CZY KURSOR MYSZY ZNAJDUJE SIE NA KARCIE
            # JEŚLI WSZYSTKIE WARUNKI SĄ SPEŁNIONE MOZNA KLIKNAC NA KARTE I ZOSTAJ ONA USUNIETA Z STOŁU
            if (pos_x < mouse_pos[0] < pos_x + size_x) and (pos_y < mouse_pos[1] < pos_y + size_y):
                print("Klikam w dobrym miejscu")
                if len(line_lvl3[pos_indx-1]) > 0:
                    line_lvl3[pos_indx-1].pop()

    # ZASADA JAK WYŻEJ ALE DLA INNYCH POZIOMÓW KART (DO ZOPTYMALIZOWANIA BO KOD SIE POWTARZA!!!)
    for position2 in coordinates_card_lvl_2:
        pos_indx = coordinates_card_lvl_2.index(position2)
        if pos_indx == 0:
            continue
        else:
            pos_x = coordinates_card_lvl_2[pos_indx][0]
            pos_y = coordinates_card_lvl_2[pos_indx][1]
            size_x = coordinates_card_lvl_2[pos_indx][2]
            size_y = coordinates_card_lvl_2[pos_indx][3]
            if (pos_x < mouse_pos[0] < pos_x + size_x) and (pos_y < mouse_pos[1] < pos_y + size_y):
                print("Klikam w dobrym miejscu")
                if len(line_lvl2[pos_indx - 1]) > 0:
                    line_lvl2[pos_indx - 1].pop()

    for position1 in coordinates_card_lvl_1:
        pos_indx = coordinates_card_lvl_1.index(position1)
        if pos_indx == 0:
            continue
        else:
            pos_x = coordinates_card_lvl_1[pos_indx][0]
            pos_y = coordinates_card_lvl_1[pos_indx][1]
            size_x = coordinates_card_lvl_1[pos_indx][2]
            size_y = coordinates_card_lvl_1[pos_indx][3]
            if (pos_x < mouse_pos[0] < pos_x + size_x) and (pos_y < mouse_pos[1] < pos_y + size_y):
                print("Klikam w dobrym miejscu")
                if len(line_lvl1[pos_indx - 1]) > 0:
                    line_lvl1[pos_indx - 1].pop()

    return line_lvl1, line_lvl2, line_lvl3 # ZWRACANA ZOSTAJE KROTKA DO ZAKTRUALIZOWANIA STANU NA STOLE


def choose_marker(marker, coordinates_marker, mouse_pos, marker_size):

    for position in coordinates_marker:
        # SPRAWDZAMY CZY KURSOR ZNAJDUJE SIE WEWNATRZ OKREGU SYMBOLIZUJACEGO ZNACZNIK
        pos_indx = coordinates_marker.index(position)
        delta_x = mouse_pos[0] - position[0]
        delta_y = mouse_pos[1] - position[1]
        dsp = pow((pow(delta_x, 2) + pow(delta_y, 2)), 0.5)

        # WARUNEK SPRAWDZAJACY CZY KURSOR MYSZY ZNAJDUJE SIE NA KARCIE
        # JEŚLI WSZYSTKIE WARUNKI SĄ SPEŁNIONE MOZNA KLIKNAC NA KARTE I ZOSTAJ ONA USUNIETA Z STOŁU
        if dsp < marker_size and marker[pos_indx].quantity > 0:
            marker[pos_indx].sub_marker()




