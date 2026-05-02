import random
class Enemy:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.block = 0
    
    def take_damage(self,amount):
        damage = max(0,amount - self.block)
        self.hp = max(0,self.hp - damage)
        self.block = max(0,self.block - amount)


    def is_alive(self):
        return self.hp > 0
    
    def get_intent(self):
        return f"{self.name} intends to attck you for {self.damage} damage"
    

    def take_action(self,target):
        action = random.choice(["attack","block"])
        if action == "attack":
            target.take_damage(self.damage)
            print("\n=========================================================================")
            print(f"{self.name} decided to attack you and deal {self.damage} damage to you")
            print("=========================================================================\n")
        elif action == "block":
            self.block = random.randint(4,6)
            print("\n=========================================================================")
            print(f"{self.name} decided to block and gains {self.block} block")
            print("=========================================================================\n")