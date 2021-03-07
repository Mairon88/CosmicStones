import pygame

# FUNKCJA RYSUJĄCA KARTY I ZNACZNIKI NA PLANSZY GŁOWNEJ
def draw_cards_markers(window, coordinates, height, element, marker_size=0):
    if element == 'card':
        for i in coordinates:
            pygame.draw.rect(window, (150, 150, 150), i)
    elif element == 'marker':
        for i in coordinates:
            pygame.draw.circle(window, (150, 150, 150), i, marker_size, 0)

# FUNKCJA RYSUJĄCA PRZYCISKI NA PLANSZY GŁOWNEJ
def draw_buttons(window, coordinates):
    for i in coordinates:
        pygame.draw.rect(window, (150, 150, 150), i)

# FUNKCJA RYSUJĄCA ELEMENTY GRACZY
def draw_player_place(window, coordinates):
    pass
