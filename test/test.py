from game_elements.player import Player


# TEST TWORZENIA GRACZY Z KLASĄ PLAYER

def test_player_init():
    player = Player('Mariusz')
    assert player

def test_player_return_name():
    player = Player('Mariusz')
    assert player.name == 'Mariusz'

