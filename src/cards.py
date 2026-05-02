#WELL WELL WELL, CARDS!!!! FINALLY

class Cards:
    def __init__(self,name,cost,description):
        self.name = name
        self.cost = cost
        self.description = description

class Strike(Cards):
    def __init__(self):
        super().__init__("Strike",1,"Deals 8 damage")
    
    def play(self,user,target):
        target.take_damage(8)


class Defend(Cards):
    def __init__(self):
        super().__init__("Block",1,"Blocks 8 upcoming damage and will be reset each turn")
        
    
    def play(self,user,target):
        user.add_block(8)