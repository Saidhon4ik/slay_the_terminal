class Enemy:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage

    
    def take_damage(self,amount):
        self.hp = max(0, self.hp - amount)


    def is_alive(self):
        return self.hp > 0
    
    def get_intent(self):
        return f"{self.name} intends to attck you for {self.damage} damage"