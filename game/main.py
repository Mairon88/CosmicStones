import pygame
import sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import draw.text as pt


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
word = ''
list_of_players = []
enter_name = 0
all_names_ok = False
game_over = False
player = 0

# WYŚWIETLANIE TEKSTU





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
                if current_view == list_view[0]:
                    current_view = list_view[1]
                    print("Prześlismy do liczby graczy")
                elif current_view == list_view[1]:
                    current_view = list_view[2]
                    print("Prześlismy do imion graczy")
                elif current_view == list_view[2]:
                    current_view = list_view[3]
                    print("Prześlismy do gry")
                elif current_view == list_view[3]:
                    current_view = list_view[4]
                    print("Prześlismy podsumowania gry")
                elif current_view == list_view[4]:
                    current_view = list_view[3]
                    print("Prześlismy do gry")

            if event.key == pygame.K_BACKSPACE:
                if current_view == list_view[4]:
                    current_view = list_view[1]
                    print("Prześlismy do liczby graczy")
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == GAME_GLOBALS.QUIT:
            sys.exit()


    pt.show_text(window, width, height, myfont, current_view) # WYŚWIETLANIE TEKSTÓW NA EKRANIE

    #         if player_names_view and len(list_of_players) >= number_of_players:
    #             char.characters(event, 'text')
    #             if event.key == pygame.K_RETURN and enter_name < len(list_of_players):
    #                 list_of_players[enter_name].name = char.word
    #                 char.word = ''
    #                 enter_name += 1
    #

    #
    #     if number_of_players_view:
    #         char.characters(event, 'num_of_players')
    #
    #
    # elif number_of_players_view:

    #
    #     number_of_players = char.num    # Przypisanie do zmiennej num ilosci graczy na za pomoca funkcji characters
    #     show_num = myfont.render(str(number_of_players), True, (250, 255, 255))
    #     window.blit(show_num, ((width/2), (height/2+50)))
    #
    # elif player_names_view:
    #     if len(list_of_players) < number_of_players:
    #         for i in range(number_of_players):
    #             list_of_players.append(Player('No_name'))
    #
    #     elif len(list_of_players) >= number_of_players:
    #         for i in list_of_players:
    #             pass
    #
    # player_name = 'PODAJ IMIE DLA GRACZA {}'.format(enter_name + 1)  # Tytył gry
    # player_name_text_width, player_name_text_height = myfont.size(
    #     player_name)  # Określenie szerokości i wysokości tekstu w pikselach
    # player_name_x_y = (width / 2) - (player_name_text_width / 2), (
    #             height / 2 - (player_name_text_height / 2))  # Położenie tekstu na ekranie
    # ply_names = myfont.render(player_name.upper(), True, (250, 255, 255))
    # window.blit(ply_names, player_name_x_y)

    pygame.display.update()
