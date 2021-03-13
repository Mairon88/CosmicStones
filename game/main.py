import pygame
import sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import draw.text as pt
import draw.board as db
import draw.characters as char
import logic.functions as func
import game_elements.data_to_prepare_elements as pele
import game_elements.data_to_prepare_elements as datp
import game_elements.stone_cards as stc
import random


# INICJALIZACJA PYGAME
pygame.init()

var = True

# INICJALIZACJA CZCIONEK
pygame.font.init()  # Inicjalizacja czionek
myfont = pygame.font.SysFont('ARIAL', 40)   #Wczytanie czcionki
myfont2 = pygame.font.SysFont('ARIAL', 30)
# TWORZENIE OKNA GRY
infoObject = pygame.display.Info()  # informacje o wymiarach ekranu
width = infoObject.current_w-150    # wymiary potrzbne dla okna gry
height = infoObject.current_h-100   # wymiary potrzbne dla okna gry
window = pygame.display.set_mode((width, height), pygame.SCALED)    # Utworzenie okna o podanych wymiarach
pygame.display.set_caption(' o o COSMIC o STONES o o ')   # Nazwa wyświtlana w ramce okna gry

# GŁÓWNE ZMIENNE
number_of_players = 2  # Liczba graczy
list_of_players = [] # Lista przechowująca obiekty graczy
game_over = False
game_run = True
confirm_name = 0 # Zmienna pomocnicza do potwierdzenia wprowadzenia imienia gracza
prepare_game_elements = True    # Zmienna to przygotowania elementów
player_turn = 0 #indeks aktualnego gracza z listy graczy
change_player = False
action = ['take_3_markers','take_2_markers','buy_a_card','reserve_a_card']
selected_action = '' # Wybrana
check_set_three = set({}) # zbriór do sprawdzenia czy wybrano 3 rozne znaczniki
check_list_two = [] # lista do sprawdzenia czy wybrano 2 te same znaczniki

# POŁOZENIE GRACZY NA EKRANIE
# indeks 0 - gracz 1, indeks 1 - gracz 2 itd.
# gracz 1 [0][0] - width_pos, [0][1] - height_pos, [0][2] - width_size, [0][3] - height_size
player_coordinates = [[width * 0.01977, height * 0.019, width * 0.2401, height * 0.4489],
                      [width * 0.743, height * 0.019, width * 0.2401, height * 0.4489],
                      [width * 0.743, height * 0.527, width * 0.2401, height * 0.4489],
                      [width * 0.01977,height * 0.527, width * 0.2401, height * 0.4489]]

# LISTA UTWORZONYCH OBIEKTÓW Z ZNACZNIKAMI
markers = []

# LISTA UTWORZONYCH KART ARYSTOKRATÓW
aristo_card = []

# LISTY UTWORZONYCH KART KAMIENI
card_lvl_1 = []
card_lvl_2 = []
card_lvl_3 = []

# LISTY KART KAMIENI AKTUALNIE WYŁOŻONYCH NA STOLE
line_lvl1 = [[],[],[],[]]
line_lvl2 = [[],[],[],[]]
line_lvl3 = [[],[],[],[]]

# WYMIARY KART KAMIENI
card_s_width_size = width * 0.075
card_s_height_size = height * 0.18

#WYMIAR ZNACZNIKÓW
marker_size = height * 0.0612

# WYMIARY KART ARYSTOKRATÓW
card_a_width_size = width * 0.075
card_a_height_size = height * 0.1355

# ODSTĘP MIĘDZY KARTAMI
padding_x = width * 0.005
padding_y = height * 0.02

# WSPÓŁRZĘDNE KART NA EKRANIE
coordinates_a_card = []
coordinates_card_lvl_1 = []
coordinates_card_lvl_2 = []
coordinates_card_lvl_3 = []

# WSPÓŁRZĘDNE PRZYCISKÓW NA EKRANIE
coordinates_buttons = []

# WSPÓŁRZĘDNE ZNACZNIKÓW NA EKRANIE
coordinates_marker = []

# GŁOWNE EKRANY GRY
list_view = ['start_view', 'number_of_players_view', 'player_names_view', 'game_view', 'result_view']
current_view = list_view[0]

# GŁÓWNA PĘTLA GRY

while True:
    window.fill((0, 0, 0))

    # OBŁSUGA ZDARZEŃ
    # np.wyjście z gry i przejście miedzy ekranami

    # PĘTLA ZDARZEŃ
    for event in GAME_EVENTS.get():

        # ZDANIERZA ZWIAZANE Z PRZYCIŚNIECIEM KLAWICZA NA KLAWIATRZUE
        if event.type == pygame.KEYDOWN:

            # WCIŚNIECIE KLAWISZA ENTER
            if game_run and event.key == pygame.K_r:
                selected_action = ''


            # WCIŚNIECIE KLAWISZA ENTER
            if event.key == pygame.K_RETURN:

                # PRZY WIDOCZNYM EKRANIE STARTOWYM WCIŚNIECIE KLAWISZAA ENTER SPOWODUJE PRZEJSCIE DO KOLEJNEGO WIDOKU
                if current_view == "start_view":
                    current_view = list_view[1]

                # JESLI ZOSTANIE WYBRANA ILOSC GRACZY TO WCISNIECIE ENTERU SPOWODUJE PRZEJSCIE DO KOLEJNEGO WIDOKU
                elif current_view == "number_of_players_view" and number_of_players in [2, 3, 4]:
                    current_view = list_view[2]
                    list_of_players = []    # ZRESETOWANIE LISTY GRACZY

                elif current_view == "player_names_view":

                    # PRZYPISYWANIE IMION GRACZOM
                    func.enter_player_names(confirm_name, list_of_players)
                    if len(char.word) > 3:
                        confirm_name += 1
                        char.word = 'gracz {}'.format(confirm_name+1)
                        if confirm_name == len(list_of_players):
                            current_view = list_view[3]
                            confirm_name = 0

                elif current_view == "game_view" and game_over and game_run == False:
                    current_view = list_view[4]
                    prepare_game_elements = True
                    char.word = "gracz 1"

                # PO ZAKOŃCZENIU GRY I WIDOKU WYNIKÓW PO WCIŚNiECIU ENTER GRA ROZPOCZNIE SIE PONOWNIE
                elif current_view == "result_view":
                    current_view = list_view[3]
                    player_turn = 0

            # PO ZAKOŃCZENIU GRY POWRÓT DO WYBORU ILOSCI GRACZY
            if event.key == pygame.K_BACKSPACE:
                if current_view == "result_view":
                    current_view = list_view[1]
                    confirm_name = 0
                    player_turn = 0

            # ZAMKNIĘCIE PROGRAMU
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == GAME_GLOBALS.QUIT:
            sys.exit()

        # Jeśli spełniony jest warunek to mozemy podać liczbe graczy i zapisąć ta liczbe do zmiennej
        if current_view == list_view[1]:
            char.characters(event, 'num_of_players')

        # Jeśli spełniony jest warunek to mozemy podać imiona graczy i je zapisać
        if current_view == list_view[2]:
            char.characters(event, 'player_names')

        # PRZYCIŚNIECIE I ZWOLNIENIE PRZYCISKU MYSZY SPOWODUJE DALSZE DZIAŁANIA
        if event.type == pygame.MOUSEBUTTONUP:
            if current_view == 'game_view':

                # ZWRACA POZYCJE KURSORA W PIXELACH
                mouse_pos = pygame.mouse.get_pos()

                # PRZELICZENIE I ZAKTUALIZOWANIE ZASOBÓW GRACZA
                list_of_players[player_turn].update_sum_of_stones()


                # PO KLIKNIECIU NA KARTE ZOSTAJE ZAKTUALIZOWANY STAN KART NA STOLE
                updated_cards_after_choose = func.choose_card(coordinates_card_lvl_1, coordinates_card_lvl_2,
                                                              coordinates_card_lvl_3, line_lvl1, line_lvl2,
                                                              line_lvl3,
                                                              mouse_pos, selected_action, list_of_players[player_turn])
                (line_lvl1, line_lvl2, line_lvl3) = updated_cards_after_choose[0]
                card = updated_cards_after_choose[1]

                # WYBRANY ZNACZNIK
                marker = func.choose_marker(markers, coordinates_marker, mouse_pos, marker_size, selected_action,
                                            list_of_players[player_turn], check_list_two, check_set_three)



                # WYBRANA AKCJA
                if selected_action == '' or selected_action == 'buy_a_card':
                    selected_action = func.choose_button(coordinates_buttons, action, mouse_pos, markers, list_of_players[player_turn], selected_action)

                # WYKONANIE WYBRANEJ AKCJI
                func.do_the_action(selected_action, list_of_players[player_turn], marker, card, markers)

                # ZAKTUALIZOWANIE PUNKTÓW GRACZA
                if list_of_players[player_turn].bought_card:
                    list_of_players[player_turn].points = 0
                    list_of_players[player_turn].count_pts()


                # SRRAWDZENIE CZY OSIĄGNIĘTO WARUNKI DO ZMIANY GRACZA
                selected_action, change_player = func.check_conditions_to_change_player(selected_action, list_of_players[player_turn], check_set_three, markers, mouse_pos)


                # print("==========Aktualny stan znaczników na stole==========")
                # for i in markers:
                #     print(i.name, i.quantity)
                # print("=====================================================")
                print("==========Aktualny stan zasobów graczy===============")
                print(f"Wybrana akcja: {selected_action}")
                print(f"Gracz: {list_of_players[player_turn].name}")
                print(f"Gracz: {list_of_players[player_turn].can_i_buy_sth}")
                # print(f"Znaczniki: {list_of_players[player_turn].markers}")
                # print(f"Ilosc wybranych znaczników: {list_of_players[player_turn].number_of_selected_markers}")
                # print(f"Wybrane znaczniki w przypadku trzech {check_set_three}")
                # print(f"Wybrane znaczniki w przypadku dwóch {check_list_two}")
                # print(f"Ilość znaczników gracza {list_of_players[player_turn].check_num_of_player_markers()}")
                # print(f"Karty emerald gracza: {list_of_players[player_turn].stone_cards_em}")
                # print(f"Karty sapphire gracza: {list_of_players[player_turn].stone_cards_sa}")
                # print(f"Karty ruby gracza: {list_of_players[player_turn].stone_cards_ru}")
                # print(f"Karty diamond gracza: {list_of_players[player_turn].stone_cards_di}")
                # print(f"Karty onyx gracza: {list_of_players[player_turn].stone_cards_on}")
                # print(f"SUMA KAMIENI KARTY Z  ZNACZNIKAMI:{list_of_players[player_turn].sum_of_stones_card_markers}")
                print("=====================================================")

                player_turn, change_player, check_list_two, check_set_three = func.player_next(list_of_players, player_turn, change_player, check_list_two, check_set_three)

    # WYŚWIETLANIE TEKSTÓW NA EKRANIE
    pt.show_text(window, width, height, myfont, myfont2, current_view, number_of_players, confirm_name, player_turn,
                 list_of_players, markers, card_lvl_1, card_lvl_2, card_lvl_3)

    # ZAPISANIE ILOŚCI GRACZY DO ZMIENNEJ
    if current_view == "number_of_players_view":
        number_of_players = func.enter_num_of_pl()

    # TWORZENIE GRACZY
    if current_view == "player_names_view":
        func.create_players(number_of_players, list_of_players, player_coordinates, width, height)

    # ROZPOCZĘCIE GRY
    if current_view == 'game_view':

        # TWORZENIE ELEMENTÓW GRY
        if prepare_game_elements:
            markers = func.create_markers(pele.prepare_markers, number_of_players)
            aristo_card = func.create_aristo(pele.prepare_aristo_card, number_of_players)

            for cards in datp.list_cards_lvl_3:
                for card in cards:
                    card_lvl_3.append(stc.Stone_Card(card[0], card[1], card[2], card[3]))

            for cards in datp.list_cards_lvl_2:
                for card in cards:
                    card_lvl_2.append(stc.Stone_Card(card[0], card[1], card[2], card[3]))

            for cards in datp.list_cards_lvl_1:
                for card in cards:
                    card_lvl_1.append(stc.Stone_Card(card[0], card[1], card[2], card[3]))

            # POTASOWANIE KART KAMIENI
            for i in range(3):
                random.shuffle(card_lvl_1)
                random.shuffle(card_lvl_2)
                random.shuffle(card_lvl_3)

            # UTWORZENIE WSPÓŁRZĘDNYCH KART I ZNACZNIKÓW
            coordinates_a_card = func.card_coordinates(width, height, 0, card_a_width_size,
                                                           card_a_height_size, padding_x, 0, len(aristo_card), 1, 'card')
            coordinates_card_lvl_1 = func.card_coordinates(width, height, card_a_height_size, card_s_width_size,
                                                           card_s_height_size, padding_x, padding_y, 5, 3, 'card')
            coordinates_card_lvl_2 = func.card_coordinates(width, height, card_a_height_size, card_s_width_size,
                                                           card_s_height_size, padding_x, padding_y, 5, 2, 'card')
            coordinates_card_lvl_3 = func.card_coordinates(width, height, card_a_height_size, card_s_width_size,
                                                           card_s_height_size, padding_x, padding_y, 5, 1, 'card')
            coordinates_marker = func.card_coordinates(width, height, card_a_height_size, card_s_width_size,
                                                           card_s_height_size, padding_x, padding_y, 6, 4, 'marker')

            coordinates_buttons = func.button_coordinates(width, height, card_a_height_size, card_s_width_size, padding_x)


            prepare_game_elements = False



        # POBIERANIE KART Z STOSU I UZUPEŁNIANIE NA STOLE JEŚLI KTÓREJŚ BRAKUJE
        update_cards = func.place_the_card(card_lvl_1, card_lvl_2, card_lvl_3, line_lvl1, line_lvl2, line_lvl3)
        (card_lvl_1, card_lvl_2, card_lvl_3, line_lvl1, line_lvl2, line_lvl3) = update_cards

        if var:
            for i in line_lvl1:
                print(i[0].stones)
            var = False

        # AKTUALIZACJA INFORMACJI O TYM CZY GRACZA STAC CHOCIAZ NA JEDNA KARTE, JESLI NIE TO OPCJA KUPOWANIA JEST WYLACZONA
        # list_of_players[player_turn].check_can_i_buy_sth(line_lvl1, line_lvl2, line_lvl3)
        #WYBÓR KARTY Z STOŁU PRZEZ GRACZA JEŚLI SPEŁNIONĄ SĄ WSZYSTKIE WARUNKI

        # WYŚWIETLANIE KART
        db.draw_cards_markers(window, coordinates_a_card,0,'card')
        db.draw_cards_markers(window, coordinates_card_lvl_1,0, 'card')
        db.draw_cards_markers(window, coordinates_card_lvl_2,0, 'card')
        db.draw_cards_markers(window, coordinates_card_lvl_3,0, 'card')
        db.draw_cards_markers(window, coordinates_marker, height, 'marker', marker_size)

        # WYŚWIWETLANIE PRZYCISKÓW
        db.draw_buttons(window, coordinates_buttons)
    # WYŚWIETLANIE STOŁU GRACZA WRAZ Z ELEMENTAMI GRY
    for i in list_of_players:
        i.draw_player_board(window)
        i.draw_player_text(window)
        i.draw_player_stone_cards(window)
        i.draw_player_markers(window)
        i.draw_player_reserved_stone_cards(window)
        i.draw_player_gold_marker(window)


    # POMOCNICZNE WYŚWIETLANIE TEKSTU
    if current_view =="game_view":
        player = myfont.render(str(player_turn+1), True, (250, 255, 255))
        window.blit(player, (width/2, height*0.01))
        num_of_card_l3 = myfont2.render(str(len(card_lvl_3)), True, (250, 255, 255))
        window.blit(num_of_card_l3, (width * 0.305, height * 0.25))
        num_of_card_l2 = myfont2.render(str(len(card_lvl_2)), True, (250, 255, 255))
        window.blit(num_of_card_l2, (width * 0.305, height * 0.45))
        num_of_card_l1 = myfont2.render(str(len(card_lvl_1)), True, (250, 255, 255))
        window.blit(num_of_card_l1, (width * 0.305, height * 0.65))


    pygame.display.update()
