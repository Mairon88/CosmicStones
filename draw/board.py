import pygame

# FUNKCJA RYSUJĄCA KARTY I ZNACZNIKI NA PLANSZY GŁOWNEJ
def draw_cards_markers(window, coordinates, element,cards_info, marker_size=0):
    list_of_markers = ['emerald_m.png','sapphire_m.png', 'ruby_m.png', 'diamond_m.png', 'onyks_m.png', 'gold_m.png']
    list_of_reverse = ['3_rev.png','2_rev.png','1_rev.png']
    # ZMIENNA POMOCNICZA DO WYKASOWANIA
    myfont2 = pygame.font.SysFont('ARIAL', 20) # POMOCNICZNA DO WYKASOWANIA
    if element == 'ar_card':
        c = 0
        for i in coordinates:
            draw_ar_card = pygame.draw.rect(window, (0, 0, 0), i)
            # text = str(cards_info[c].name)  # Tytył gry
            # text_x_y = (i)  # Położenie tekstu na ekranie
            # game_name = myfont2.render(text, True, (250, 255, 255))
            # window.blit(game_name, text_x_y)
            img = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/'+str(cards_info[c].name)+'.png')

            window.blit(img, draw_ar_card)
            c+=1
    elif element == 's_card_1' or element == 's_card_2' or element == 's_card_3':
        c = 0
        for i in coordinates:
            draw_card = pygame.draw.rect(window, (50, 100, 0), i)
            if c == 0 and element == 's_card_1':
                reverse = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/' + list_of_reverse[2])
                window.blit(reverse, draw_card)
            elif c == 0 and element == 's_card_2':
                reverse = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/' + list_of_reverse[1])
                window.blit(reverse, draw_card)
            elif c == 0 and element == 's_card_3':
                reverse = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/' + list_of_reverse[0])
                window.blit(reverse, draw_card)

            if c > 0:
                if cards_info[c - 1] != []:
                    img = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/'+cards_info[c - 1][0].images)
                    window.blit(img, draw_card)

                # TEKST DO WYSWIETLANIA W RAMACH SPRAWDZENIA POPRAWNOSCI WYSWIETLANIA OBRAZKOW
                # text = cards_info[c - 1][0].name  # Tytył gry
                # text_x_y = (i)  # Położenie tekstu na ekranie
                # game_name = myfont2.render(text, True, (250, 255, 255))
                # window.blit(game_name, text_x_y)
                # z = 0
                # text_bonus = str("bonus: "+str(cards_info[c - 1][0].bonus)) # Tytył gry
                # text_x_y = (i[0], i[1] + 25 + z * 25)  # Położenie tekstu na ekranie
                # game_name = myfont2.render(text_bonus, True, (250, 255, 255))
                # window.blit(game_name, text_x_y)
                # for key, value in cards_info[c-1][0].stones.items():
                #     text = str(key)+" "+str(value)  # Tytył gry
                #     text_x_y = (i[0],i[1]+50+z*25)  # Położenie tekstu na ekranie
                #     game_name = myfont2.render(text, True, (250, 255, 255))
                #     window.blit(game_name, text_x_y)
                #     z += 1
            c+=1

    elif element == 'marker':
        m=0
        for i in coordinates:
            img = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/' + list_of_markers[m])
            draw_marker = pygame.draw.circle(window, (150, 150, 150), i, marker_size, 0)
            window.blit(img, draw_marker)
            #
            # text = list_of_markers[m]  # Tytył gry
            # text_x_y = (i)  # Położenie tekstu na ekranie
            # game_name = myfont2.render(text.upper(), True, (250, 255, 255))
            # window.blit(game_name, text_x_y)
            m+=1
# FUNKCJA RYSUJĄCA PRZYCISKI NA PLANSZY GŁOWNEJ

def draw_buttons(window, coordinates, width):
    list_of_button = ['take_3.png', 'take_2.png', 'buy.png', 'reserved.png'] # ZMIENNA POMOCNICZA DO WYKASOWANIA

    myfont2 = pygame.font.SysFont('ARIAL', 20)
    n = 0
    for i in coordinates:
        button = pygame.draw.rect(window, (1, 150, 150), i)
        img = pygame.image.load('/home/mariusz/PycharmProjects/five_stones/images/' + list_of_button[n])
        window.blit(img, button)
        # text = list_of_button[n]  # Tytył gry
        # text_x_y = (i)  # Położenie tekstu na ekranie
        # game_name = myfont2.render(text.upper(), True, (250, 255, 255))
        # window.blit(game_name, text_x_y)
        n+=1



