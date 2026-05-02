from cards import Strike, Defend
import random


class Deck:
    def __init__(self):
        self.cards = [Strike(), Strike(), Strike(), Defend(), Defend(), Defend()]
        random.shuffle(self.cards)
        self.hand = []
        self.discard = []

    def draw(self,n):
        for _ in range(n):
            if not self.cards:
                break
            card = self.cards.pop(0)
            self.hand.append(card)
    
    def discard_hand(self):
        self.discard.extend(self.hand)
        self.hand = []
    

    def reshuffle(self):
        if not self.cards:
            self.cards = self.discard
            random.shuffle(self.cards)
            self.discard = []