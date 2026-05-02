class Player:
    def __init__(self,name,hp = 70,block = 0, damage = 8):
        self.name = name #just name
        self.hp = hp #base hp
        self.max_hp = hp #max_hp, capped at 50 for now
        self.block = block # base shield
        self.damage = damage # base atk

    def heal(self):
        regen = int(0.3*self.max_hp)
        print("=====================================================")
        print(f"You were at {self.hp} hp")
        self.hp = min(self.max_hp, self.hp+int(0.3*self.max_hp))
        print(f"""After defeating a monster, 
you healed your hp by {regen}. Now you have {self.hp}/{self.max_hp} hp""")
        print("=====================================================")
    def deal_damage(self,target):
        target.take_damage(self.damage)

    
    def take_damage(self,amount):
        damage = max(0, amount - self.block)
        self.hp = max(0, self.hp - damage)
        self.block = max(0,self.block-amount)

    def add_block(self,amount):
        self.block += amount #gain 'amount' of block
    
    def skip_turn(self):
        print("You just skipped the turn")

    def is_alive(self):
        return self.hp > 0