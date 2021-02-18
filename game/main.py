import pygame
import sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import draw.text as pt
import draw.characters as char
import logic.functions as func


# INICJALIZACJA PYGAME
pygame.init()

# INICJALIZACJA CZCIONEK
pygame.font.init()  # Inicjalizacja czionek
myfont = pygame.font.SysFont('ARIAL', 40)   #Wczytanie czcionki

# TWORZENIE OKNA GRY
infoObject = pygame.display.Info()  # informacje o wymiarach ekranu
width = infoObject.current_w-200    # wymiary potrzbne dla okna gry
height = infoObject.current_h-200   # wymiary potrzbne dla okna gry
window = pygame.display.set_mode((width, height), pygame.SCALED)    # Utworzenie okna o podanych wymiarach
pygame.display.set_caption(' o o FIVE o STONES o o ')   # Nazwa wyświtlana w ramce okna gry

# GŁÓWNE ZMIENNE
number_of_players = 0  # Liczba graczy
list_of_players = []
game_over = True
confirm_name = 0
prepare_game_elements = True


# DANE DO PRZYGOTOWANIA ZNACZNIKÓW , TRUE = JOKER
prepare_markers = [('emerald', False),
           ('sapphire', False),
           ('ruby', False),
           ('diamond', False),
           ('onyx', False),
           ('gold', True),]

# DANE DO PRZYGOTOWANIA KART ARYSTOKRATÓW
prepare_aristo_card = [['e3s3d3',{'emerald': 3, 'sapphire': 3, 'diamond': 3}],
                       ['o4r4',{'onyx': 4, 'ruby': 4}],
                        ['o3s3d3',{'onyx': 3, 'sapphire': 3, 'diamond': 3}],
                        ['o3r3e3',{'onyx': 3, 'ruby': 3, 'emerald': 3}],
                        ['o4d4',{'onyx': 4, 'diamond': 4}],
                        ['e3s3r3',{'emerald': 3, 'sapphire': 3, 'ruby': 3}],
                        ['r4e4',{'roby': 4, 'emerald': 4}],
                        ['s4d4',{'sapphire': 4, 'diamond': 4}],
                        ['o3r3d3',{'onyx': 3, 'ruby': 3, 'diamond': 3}],
                        ['s4e4',{'sapphire': 4, 'emerald': 4}],
                       ]

# LISTA UTWORZONYCH OBIEKTÓW Z ZNACZNIKAMI
markers = []

# LISTA UTWORZONYCH KART ARYSTOKRATÓW
aristo_card = []

# GŁOWNE EKRANY GRY
list_view = ['start_view', 'number_of_players_view', 'player_names_view', 'game_view', 'result_view']
current_view = list_view[0]
# GŁÓWNA PĘTLA GRY

while True:
    window.fill((0, 0, 0))

    # OBŁSUGA ZDARZEŃ
    # np.wyjście z gry i przejście miedzy ekranami

    for event in GAME_EVENTS.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                if current_view == "start_view":
                    current_view = list_view[1]

                elif current_view == "number_of_players_view" and number_of_players in [2, 3, 4]:
                    current_view = list_view[2]
                    list_of_players = []


                elif current_view == "player_names_view":
                    # PRZYPISYWANIE IMION GRACZOM

                    func.enter_player_names(confirm_name, list_of_players)
                    confirm_name += 1
                    char.word = 'gracz {}'.format(confirm_name+1)
                    if confirm_name == len(list_of_players):
                        current_view = list_view[3]
                        confirm_name = 0

                elif current_view == "game_view" and game_over:
                    current_view = list_view[4]
                    prepare_game_elements = True
                    char.word = "gracz 1"

                elif current_view == "result_view":
                    current_view = list_view[3]



            # PO ZAKOŃCZENIU GRY POWRÓT DO WYBORU ILOSCI GRACZY
            if event.key == pygame.K_BACKSPACE:
                if current_view == "result_view":
                    current_view = list_view[1]
                    confirm_name = 0

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


    # WYŚWIETLANIE TEKSTÓW NA EKRANIE
    pt.show_text(window, width, height, myfont, current_view, number_of_players, confirm_name)

    # ZAPISANIE ILOŚCI GRACZY DO ZMIENNEJ
    number_of_players = func.enter_num_of_pl()

    # TWORZENIE GRACZY
    func.create_players(current_view, number_of_players, list_of_players)

    # ROZPOCZĘCIE GRY
    if current_view == "game_view":
        # TWORZENIE ELEMENTÓW GRY
        if prepare_game_elements:
            markers = func.create_markers(prepare_markers, number_of_players)
            aristo_card = func.create_aristo(prepare_aristo_card, number_of_players)
            prepare_game_elements = False



    pygame.display.update()
