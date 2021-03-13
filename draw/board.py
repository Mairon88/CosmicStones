import pygame






# FUNKCJA RYSUJĄCA KARTY I ZNACZNIKI NA PLANSZY GŁOWNEJ
def draw_cards_markers(window, coordinates, element,cards_info, marker_size=0):
    list_of_markers = ['szm','sza', 'ru', 'di', 'on', 'zł']  # ZMIENNA POMOCNICZA DO WYKASOWANIA
    myfont2 = pygame.font.SysFont('ARIAL', 20) # POMOCNICZNA DO WYKASOWANIA
    if element == 'ar_card':
        c = 0
        for i in coordinates:
            pygame.draw.rect(window, (150, 150, 150), i)
            text = str(cards_info[c].name)  # Tytył gry
            text_x_y = (i)  # Położenie tekstu na ekranie
            game_name = myfont2.render(text, True, (250, 255, 255))
            window.blit(game_name, text_x_y)
            c+=1
    elif element == 's_card':
        c = 0
        for i in coordinates:
            pygame.draw.rect(window, (150, 150, 150), i)

            if c > 0:
                text = cards_info[c - 1][0].name  # Tytył gry
                text_x_y = (i)  # Położenie tekstu na ekranie
                game_name = myfont2.render(text, True, (250, 255, 255))
                window.blit(game_name, text_x_y)
                z = 0
                text_bonus = str("bonus: "+str(cards_info[c - 1][0].bonus)) # Tytył gry
                text_x_y = (i[0], i[1] + 25 + z * 25)  # Położenie tekstu na ekranie
                game_name = myfont2.render(text_bonus, True, (250, 255, 255))
                window.blit(game_name, text_x_y)
                for key, value in cards_info[c-1][0].stones.items():
                    text = str(key)+" "+str(value)  # Tytył gry
                    text_x_y = (i[0],i[1]+50+z*25)  # Położenie tekstu na ekranie
                    game_name = myfont2.render(text, True, (250, 255, 255))
                    window.blit(game_name, text_x_y)
                    z += 1
            c+=1

    elif element == 'marker':
        m=0
        for i in coordinates:
            pygame.draw.circle(window, (150, 150, 150), i, marker_size, 0)
            text = list_of_markers[m]  # Tytył gry
            text_x_y = (i)  # Położenie tekstu na ekranie
            game_name = myfont2.render(text.upper(), True, (250, 255, 255))
            window.blit(game_name, text_x_y)
            m+=1
# FUNKCJA RYSUJĄCA PRZYCISKI NA PLANSZY GŁOWNEJ
def draw_buttons(window, coordinates, width):
    list_of_button = ['weź 3', 'weź 2', 'kup', 'rezerwuj'] # ZMIENNA POMOCNICZA DO WYKASOWANIA
    myfont2 = pygame.font.SysFont('ARIAL', 20)
    n = 0
    for i in coordinates:
        pygame.draw.rect(window, (1, 150, 150), i)
        text = list_of_button[n]  # Tytył gry
        text_x_y = (i)  # Położenie tekstu na ekranie
        game_name = myfont2.render(text.upper(), True, (250, 255, 255))
        window.blit(game_name, text_x_y)
        n+=1

# FUNKCJA RYSUJĄCA ELEMENTY GRACZY
def draw_player_place(window, coordinates):
    pass

