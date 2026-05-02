import random
class Enemy:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.block = 0
        self.current_action = "attack"
    
    def take_damage(self,amount):
        damage = max(0,amount - self.block)
        self.hp = max(0,self.hp - damage)
        self.block = max(0, self.block - amount)


    def is_alive(self):
        return self.hp > 0
    


    def take_action(self):
        action = random.choice(["attack","block"])
        if action == "attack":
            self.current_action = "attack"
            
        elif action == "block":
            self.current_action = "block"    
            self.block = random.randint(4,6) 

    def get_intent(self):
        if self.current_action == "attack":
            return(f"{self.name} is intending to deal {self.damage} damage to you")
        elif self.current_action == "block":
            return(f"{self.name} is intending to block(4-6 damage)")

    def execute_action(self,target):
        if self.current_action == "attack":
            actual_damage = max(0,self.damage - target.block)
            blocked_amount = self.damage - actual_damage
            target.take_damage(self.damage)          
            if blocked_amount > 0:
                print(f"{self.name} attacks for {self.damage}, you blocked {blocked_amount}! You take {actual_damage} damage!")  
            else:
                print(f"{self.name} attacks your for {actual_damage} damage!")
