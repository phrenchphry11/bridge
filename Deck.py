import random

class Deck(object):
    def __init__(self):
        self.cards = {}
        self.cards["clubs"] = []
        self.cards["diamonds"] = []
        self.cards["hearts"] = []
        self.cards["spades"] = []

        for i in range(1,14):
            self.cards["clubs"].append(i)
            self.cards["diamonds"].append(i)
            self.cards["hearts"].append(i)
            self.cards["spades"].append(i)

    def shuffle_and_return(self):
        shuffled_deck = []
        for suite in self.cards.iterkeys():
            for card in self.cards[suite]:
                shuffled_deck.append((suite,card))
        random.shuffle(shuffled_deck)
        return shuffled_deck
