import draw.characters as char
import game_elements.player as plr

def enter_num_of_pl():
    number_of_players = char.num
    return number_of_players

def create_players(current_view, number_of_players, list_of_players):
    if current_view == "player_names_view" and number_of_players is not None:
        if len(list_of_players) < number_of_players:
            for i in range(number_of_players):
                list_of_players.append(plr.Player("No_Name"))

def enter_player_names(confirm_name, list_of_players):
    list_of_players[confirm_name].name = char.word

