import random
from enemy import Enemy

class Slime(Enemy):
    def __init__(self):
        super().__init__("Slime", 20, 4)



class Goblin(Enemy):
    def __init__(self):
        self.dodge = False
        super().__init__("Goblin", 30, 6)
    
    def take_damage(self, amount):
        if random.random() < 0.25:
            self.dodge = True
            print(f"{self.name} dodged your attack and took no damage")
        else:
            super().take_damage(amount)
            self.dodge = False


class Gigachad(Enemy):
    def __init__(self):
        super().__init__("Gigachad", 50, 8)