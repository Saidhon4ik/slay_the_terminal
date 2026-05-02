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
        super().__init__("Gigachad", 40, 7)
    

    def execute_action(self, target, turn):
        if turn % 3  == 0 and turn != 0 and self.current_action == "attack" :
            actual_damage = max(0, self.damage*2 - target.block)
            blocked = self.damage*2 - actual_damage
            if blocked > 0:
                print(f"{self.name} GIGACHAD SMASH for {self.damage*2}, you blocked {blocked}! You take {actual_damage} damage!")
            else:
                print(f"{self.name} GIGACHAD SMASH for {actual_damage} damage!")
            target.take_damage(self.damage*2)
        else:
            super().execute_action(target,turn)