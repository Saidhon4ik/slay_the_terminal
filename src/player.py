class Player:
    def __init__(self,name,hp = 50,block = 0, damage = 6):
        self.name = name #just name
        self.hp = hp #base hp
        self.max_hp = hp #max_hp, capped at 50 for now
        self.block = block # base shield
        self.damage = damage # base atk

    def deal_damage(self,target):
        pass

    
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