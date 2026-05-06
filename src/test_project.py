from player import Player
from enemy import Enemy

def test_player_takes_damage():
    player = Player("Test")
    player.take_damage(10)
    assert player.hp == 40  # 50 - 10 = 40