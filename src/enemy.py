#enemy.py
import random

class Enemy:
    def __init__(self, name="Slime", hp=30):
        self.name = name
        self.hp = hp
        self.block = 0

    def take_damage(self, damage):
        reduced = max(0, damage - self.block)
        self.block = 0
        self.hp = max(0, self.hp - reduced)
        return reduced

    def attack_damage(self):
        return random.randint(4, 8)

    def is_alive(self):
        return self.hp > 0