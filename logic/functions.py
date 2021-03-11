import draw.characters as char
import game_elements.player as plr
import game_elements.stone_markers as mrk
import game_elements.aristocrat_cards as aric
import random
import time


# FUNKCJA DO PODAWANIA ILOSCI GRACZY
def enter_num_of_pl():
    number_of_players = char.num
    return number_of_players


# FUNKCJA TWORZACA OBIEKTY GRACZY
def create_players(number_of_players, list_of_players, player_coordinates, width, height):
    if number_of_players is not None:
        if len(list_of_players) < number_of_players:
            for i in range(number_of_players):
                list_of_players.append(plr.Player("No_Name", player_coordinates[i], width, height))


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
def card_coordinates(width, height, card_a_height_size, card_width_size, card_height_size, padding_x, padding_y, quantity,
                     level, element):
    coordinates_list = []
    if element == 'card':
        for i in range(quantity):
            coordinates_list.append((width * 0.2711 + padding_x, height*0.02+card_a_height_size + level*padding_y+(level-1)*card_height_size, card_width_size, card_height_size))  # P1 AREA
            padding_x += card_width_size/2 + width * 0.056
    elif element == 'marker':
        for i in range(quantity):
            coordinates_list.append((width * 0.2711 +height*0.06+ padding_x, height*0.008+card_a_height_size + level*padding_y+(level-1)*card_height_size + height * 0.075))  # P1 AREA
            padding_x += card_width_size/2 + width * 0.039
    return coordinates_list

# WYZNACZANIE WSPÓŁRZĘDNYCH PRZYCISKÓW
def button_coordinates(width, height, card_a_height_size, card_a_width_size, padding_x):
    coordinates_b_list = []
    for i in range(4):
        coordinates_b_list.append((width * 0.2711 + padding_x, height-(height*0.08), card_a_width_size*1.1, card_a_height_size/2.5))  # P1 AREA
        padding_x += card_a_width_size/2 + width * 0.085

    return coordinates_b_list

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
                line_lvl3, mouse_pos, selected_action, current_player):
    # CHECK LINE LVL3
    card = None
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
            if (pos_x < mouse_pos[0] < pos_x + size_x) and (pos_y < mouse_pos[1] < pos_y + size_y) and selected_action == 'buy_a_card' and current_player.can_i_afford_it(line_lvl3[pos_indx-1]):
                print("Klikam w dobrym miejscu")
                if len(line_lvl3[pos_indx-1]) > 0:
                    card = line_lvl3[pos_indx-1].pop()


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
            if (pos_x < mouse_pos[0] < pos_x + size_x) and (pos_y < mouse_pos[1] < pos_y + size_y) and selected_action == 'buy_a_card' and current_player.can_i_afford_it(line_lvl2[pos_indx - 1]):
                print("Klikam w dobrym miejscu")
                if len(line_lvl2[pos_indx - 1]) > 0:
                    card = line_lvl2[pos_indx - 1].pop()

    for position1 in coordinates_card_lvl_1:
        pos_indx = coordinates_card_lvl_1.index(position1)
        if pos_indx == 0:
            continue
        else:
            pos_x = coordinates_card_lvl_1[pos_indx][0]
            pos_y = coordinates_card_lvl_1[pos_indx][1]
            size_x = coordinates_card_lvl_1[pos_indx][2]
            size_y = coordinates_card_lvl_1[pos_indx][3]
            if (pos_x < mouse_pos[0] < pos_x + size_x) and (pos_y < mouse_pos[1] < pos_y + size_y) and selected_action == 'buy_a_card' and current_player.can_i_afford_it(line_lvl1[pos_indx - 1]):
                print("Klikam w dobrym miejscu")
                if len(line_lvl1[pos_indx - 1]) > 0:
                    card = line_lvl1[pos_indx - 1].pop()

    return (line_lvl1, line_lvl2, line_lvl3), card# ZWRACANA ZOSTAJE KROTKA DO ZAKTRUALIZOWANIA STANU NA STOLE

# WYBIERANIE ZNACZNIKOW Z STOLU
def choose_marker(marker, coordinates_marker, mouse_pos, marker_size,selected_action, current_player, check_list_two, check_set_three):
    if (selected_action == 'take_3_markers' and current_player.number_of_selected_markers < 3) or (selected_action == 'take_2_markers' and current_player.number_of_selected_markers < 2):
        for position in coordinates_marker[:-1]:
            # SPRAWDZAMY CZY KURSOR ZNAJDUJE SIE WEWNATRZ OKREGU SYMBOLIZUJACEGO ZNACZNIK
            pos_indx = coordinates_marker.index(position)
            delta_x = mouse_pos[0] - position[0]
            delta_y = mouse_pos[1] - position[1]
            dsp = pow((pow(delta_x, 2) + pow(delta_y, 2)), 0.5)

            # WARUNEK SPRAWDZAJACY CZY KURSOR MYSZY ZNAJDUJE SIE NA ZNACZNIKU
            # JEŚLI WSZYSTKIE WARUNKI SĄ SPEŁNIONE MOZNA KLIKNAC NA ZNACZNIK I ZOSTAJE USUNIETY Z STOŁU
            if dsp < marker_size and marker[pos_indx].quantity > 0:

                if selected_action == 'take_3_markers' and marker[pos_indx].name not in check_set_three:
                    check_set_three.add(marker[pos_indx].name)
                    marker[pos_indx].sub_marker()
                    return marker[pos_indx].name
                # POTRZEBNE WARUNKI DLA DWÓCH PRZYPADKÓW
                elif selected_action == 'take_2_markers':
                    if check_list_two == [] and marker[pos_indx].quantity >=4:
                        check_list_two.append(marker[pos_indx].name)

                    if marker[pos_indx].name in check_list_two:
                        marker[pos_indx].sub_marker()
                        return marker[pos_indx].name



# WYBÓR AKCJI PRZEZ NACIŚNIECIE ODPOWIEDNIEGO PRZYCISKU
def choose_button(coordinates_buttons, action, mouse_pos, markers, current_player):

    for position in coordinates_buttons:
        pos_indx = coordinates_buttons.index(position)

        pos_x = coordinates_buttons[pos_indx][0]
        pos_y = coordinates_buttons[pos_indx][1]
        size_x = coordinates_buttons[pos_indx][2]
        size_y = coordinates_buttons[pos_indx][3]

        # Zapis warunku sprawdzającego do zmiennej, sprawdza czy jest sens wybierania opcji wyboru znaczników
        requirement = (pos_x < mouse_pos[0] < pos_x + size_x) and (pos_y < mouse_pos[1] < pos_y + size_y)
        stones_in_stock_four = (markers[0].quantity < 4 and markers[1].quantity < 4 and markers[2].quantity < 4
                           and markers[3].quantity < 4 and markers[4].quantity < 4)

        stones_in_stock_zero = (markers[0].quantity == 0 and markers[1].quantity == 0 and markers[2].quantity == 0
                                and markers[3].quantity == 0 and markers[4].quantity == 0)
        # WARUNEK SPRAWDZAJACY CZY KURSOR MYSZY ZNAJDUJE SIE NA PRZYCISKU
        if requirement and pos_indx == 0 and not stones_in_stock_zero:
            return action[0]

        elif requirement and pos_indx == 1 and not stones_in_stock_four:
            return action[1]

        elif requirement and pos_indx == 2 and current_player.can_i_buy_sth:
            return action[2]

        elif requirement and pos_indx == 3:
            return action[3]

    return ''

# OKREŚLANIE CZYJA KOLEJ
def player_next(list_of_players, player_turn, change_player, check_list_two, check_set_three):
    if change_player:
        list_of_players[player_turn].number_of_selected_markers = 0
        list_of_players[player_turn].took_card = False
        list_of_players[player_turn].bought_card = False

        if player_turn != len(list_of_players)-1:
            player_turn += 1
        else:
            player_turn = 0

        return player_turn, False,[], set({})
    return player_turn, change_player, check_list_two, check_set_three

# WYKONANIE ODPOWIEDNIEJ AKCJI
def do_the_action(selected_action, current_player, marker, card):
    if selected_action == 'take_3_markers' and marker != None and current_player.number_of_selected_markers < 3:
        current_player.markers.setdefault(marker, 0)
        current_player.markers[marker] += 1
        print("Biorę trzy znaczniki różnego koloru")
        current_player.number_of_selected_markers += 1

    elif selected_action == 'take_2_markers' and marker != None and current_player.number_of_selected_markers < 2:
        current_player.markers.setdefault(marker, 0)
        current_player.markers[marker] += 1
        print("Biorę dwa znaczniki tego samego koloru")
        current_player.number_of_selected_markers += 1

    elif selected_action == 'reserve_a_card' and marker != None:
        print("Rezerwuje kartę i biorę znacznik złota")

    elif selected_action =='buy_a_card':
        if card != None:
            if card.name == 'emerald':
                current_player.stone_cards_em.append(card)
            elif card.name == 'sapphire':
                current_player.stone_cards_sa.append(card)
            elif card.name == 'ruby':
                current_player.stone_cards_ru.append(card)
            elif card.name == 'diamond':
                current_player.stone_cards_di.append(card)
            elif card.name == 'onyx':
                current_player.stone_cards_on.append(card)
            current_player.bought_card = True


# JEŚLI WYBRANO AKCJE Z TRZEMA ZNACZNIKAMI A MOZNA WZIAC MNIEJ NIZ 3 TO PO WYRABNIU JEDNEGO LUB DWOCH ZMIANA GRACZA
# JEŚLI CHOCIAZ JEDEN ZNACZNIK INNY NIZ TE CO WYBRALISMY MA WARTOSC WIEKSZA NIZ 0 TO ZRWACA FALSE
def action_three_with_null(check_set_three, markers):
    for i in markers[:-1]:
        if i.name not in check_set_three and i.quantity > 0:
            return False
    return True

# SPRAWDZENIE WARUNKOW DO ZMIANY GRACZA
def check_conditions_to_change_player(selected_action, current_player, check_set_three, markers, mouse_pos):
    if selected_action == 'take_3_markers' and (current_player.number_of_selected_markers == 3 or action_three_with_null(check_set_three, markers)):
        if current_player.check_num_of_player_markers() < 11:
            return '', True
        else:
            current_player.choose_player_marker(mouse_pos, markers)
            if current_player.check_num_of_player_markers() < 11:
                return '', True
            else:
                return selected_action, False
    elif selected_action == 'take_2_markers' and current_player.number_of_selected_markers == 2:
        if current_player.check_num_of_player_markers() < 11:
            return '', True
        else:
            current_player.choose_player_marker(mouse_pos, markers)
            if current_player.check_num_of_player_markers() < 11:
                return '', True
            else:
                return selected_action, False

    elif selected_action == 'reserve_a_card' and current_player.took_card:
        current_player.taked_card = False
        return '', True

    elif selected_action == 'buy_a_card' and current_player.bought_card:
        current_player.bought_card = False
        return '', True
    else:
        return selected_action, False
