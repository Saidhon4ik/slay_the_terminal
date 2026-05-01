#player.py
class Player:
    def __init__(self, hp=50):
        self.max_hp = hp
        self.hp = hp
        self.block = 0

    def take_damage(self, damage):
        reduced = max(0, damage - self.block)
        self.block = 0
        self.hp = max(0, self.hp - reduced)
        return reduced

    def gain_block(self, amount):
        self.block += amount

    def is_alive(self):
        return self.hp > 0