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
    

    def execute_action(self, target, turn):
        if turn % 3  == 0 and turn != 0 and self.current_action == "attack" :
            target.take_damage(self.damage*2)
            print(f"{self.name} uses GIGACHAD SMASH and attacks you for {self.damage*2} damage")
        else:
            super().execute_action(target,turn)