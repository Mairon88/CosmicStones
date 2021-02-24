import pygame

def draw_cards_markers(window, coordinates, height, element, marker_size=0):
    if element == 'card':
        for i in coordinates:
            pygame.draw.rect(window, (150, 150, 150), i)
    elif element == 'marker':
        for i in coordinates:
            pygame.draw.circle(window, (150, 150, 150), i, marker_size, 0)
