import pygame
import sys
import pygame.event as GAME_EVENTS
import draw.characters as char

def show_text(window, width, height, myfont,current_view, number_of_players, confirm):
    if current_view == 'start_view':
        text = 'COSMIC STONES'  # Tytył gry
        text_width, text_height = myfont.size(text)  # Określenie szerokości i wysokości tekstu w pikselach
        text_x_y = (width / 2 - (text_width / 2), height / 2 - (text_height / 2))  # Położenie tekstu na ekranie
        game_name = myfont.render(text.upper(), True, (250, 255, 255))
        window.blit(game_name, text_x_y)

    elif current_view == 'number_of_players_view':
        text = 'PODAJ ILOŚĆ GRACZY OD 2 DO 4 I ZATWIERDŹ WCISKAJĄC ENTER'  # Tytył gry
        text_width, text_height = myfont.size(text)  # Określenie szerokości i wysokości tekstu w pikselach
        text_x_y = (width / 2 - (text_width / 2), height / 2 - (text_height / 2))  # Położenie tekstu na ekranie
        game_name = myfont.render(text.upper(), True, (250, 255, 255))
        window.blit(game_name, text_x_y)
        if number_of_players is not None:
            show_num = myfont.render(str(number_of_players), True, (250, 255, 255))
            window.blit(show_num, ((width / 2), (height / 2 + 50)))


    elif current_view == 'player_names_view':
        text = 'PODAJ IMIONA GRACZY'  # Tytył gry
        text_width, text_height = myfont.size(text)  # Określenie szerokości i wysokości tekstu w pikselach
        text_x_y = (width / 2 - (text_width / 2), height / 2 - (text_height / 2))  # Położenie tekstu na ekranie
        game_name = myfont.render(text.upper(), True, (250, 255, 255))
        window.blit(game_name, text_x_y)
        player_name = "Gracz nr "+str(confirm+1)+" : "+char.word
        show_name = myfont.render(str(player_name).upper(), True, (250, 255, 255))
        window.blit(show_name, ((width / 2 - 250), (height / 2 + 50)))


    elif current_view == 'game_view':
        text = 'TRWA GRA'  # Tytył gry
        text_width, text_height = myfont.size(text)  # Określenie szerokości i wysokości tekstu w pikselach
        text_x_y = (width / 2 - (text_width / 2), 50)  # Położenie tekstu na ekranie
        game_name = myfont.render(text.upper(), True, (250, 255, 255))
        window.blit(game_name, text_x_y)

    elif current_view == 'result_view':
        text = 'WYNIKI'  # Tytył gry
        text_width, text_height = myfont.size(text)  # Określenie szerokości i wysokości tekstu w pikselach
        text_x_y = (width / 2 - (text_width / 2), 50)  # Położenie tekstu na ekranie
        game_name = myfont.render(text.upper(), True, (250, 255, 255))
        window.blit(game_name, text_x_y)


