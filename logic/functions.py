import draw.characters as char
import game_elements.player as plr
import game_elements.stone_markers as mrk
import game_elements.aristocrat_cards as aric
import random

def enter_num_of_pl():
    number_of_players = char.num
    return number_of_players

def create_players(current_view, number_of_players, list_of_players):
    if current_view == "player_names_view" and number_of_players is not None:
        if len(list_of_players) < number_of_players:
            for i in range(number_of_players):
                list_of_players.append(plr.Player("No_Name"))

def enter_player_names(confirm_name, list_of_players):
    if char.word is str:
        list_of_players[confirm_name].name = 'sdfsdf'
    list_of_players[confirm_name].name = char.word

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
        markers.append(mrk.Markers(stone[0],stone[1], n))
    return markers


def create_aristo(prepare_aristo, num_of_players):
    aristo = []
    if num_of_players == 4:
        n = 5
    elif num_of_players == 3:
        n = 4
    else:
        n = 3

    cards = random.sample(prepare_aristo, k=n)
    print(cards)
    for card in cards:
        aristo.append(aric.Aristo(card[0], card[1]))
    return aristo