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
all_names_ok = False
game_over = False
confirm_name = 0


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
                elif current_view == "player_names_view":
                    func.enter_player_names(confirm_name,list_of_players)
                    confirm_name += 1
                    char.word = ''
                    if confirm_name == 4:
                        current_view = list_view[3]
                        confirm_name = 0
                elif current_view == "game_view":
                    current_view = list_view[4]
                elif current_view == "result_view":
                    current_view = list_view[3]

            if event.key == pygame.K_BACKSPACE:
                if current_view == "result_view":
                    current_view = list_view[1]

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
    pt.show_text(window, width, height, myfont, current_view, number_of_players)

    # ZAPISANIE ILOŚCI GRACZY DO ZMIENNEJ
    number_of_players = func.enter_num_of_pl()

    # TWORZENIE GRACZY
    func.create_players(current_view, number_of_players, list_of_players)

    pygame.display.update()
