class Player(object):
    def __init__(self, strategy=None):
        self.hand = {}
        self.hand["clubs"] = []
        self.hand["diamonds"] = []
        self.hand["hearts"] = []
        self.hand["spades"] = []
        self.hand_points = 0
        self.strategy = strategy

    def count_points(self):
        print self.hand_points
        for suite in self.hand.iterkeys():
            for card in self.hand[suite]:
                if card == 1:
                    self.hand_points += 4
                if card == 13:
                    self.hand_points += 3
                if card == 12:
                    self.hand_points += 2
                if card == 11:
                    self.hand_points += 1

        if len(self.hand["clubs"]) == 0:
            self.hand_points += 3
        elif len(self.hand["clubs"]) == 1:
            self.hand_points += 2
        elif len(self.hand["clubs"]) == 2:
            self.hand_points += 1

        if len(self.hand["diamonds"]) == 0:
            self.hand_points += 3
        elif len(self.hand["diamonds"]) == 1:
            self.hand_points += 2
        elif len(self.hand["diamonds"]) == 2:
            self.hand_points += 1

        if len(self.hand["hearts"]) == 0:
            print "len hearts"
            self.hand_points += 3
        elif len(self.hand["hearts"]) == 1:
            self.hand_points += 2
        elif len(self.hand["hearts"]) == 2:
            self.hand_points += 1

        if len(self.hand["spades"]) == 0:
            print "len spades"
            self.hand_points += 3
        elif len(self.hand["spades"]) == 1:
            self.hand_points += 2
        elif len(self.hand["spades"]) == 2:
            self.hand_points += 1

        return self.hand_points

    def open_bid(self):
        if self.hand_points >= 13:
            if self.hand_points >= 15:
                if self.hand_points >= 22:
                    return (2, "clubs")
                elif self.hand_points >= 20:
                    if len(self.hand["spades"]) > 2 and len(self.hand["hearts"]) > 2 and len(self.hand["diamonds"]) > 2 and len(self.hand["clubs"]) > 2:
                        return (2, "no trump")
                elif len(self.hand["spades"]) > 2 and len(self.hand["hearts"]) > 2 and len(self.hand["diamonds"]) > 2 and len(self.hand["clubs"]) > 2:
                    return (1, "no trump")
            if len(self.hand["hearts"]) >= 5:
                return (1, "hearts")
            if len(self.hand["spades"]) >= 5:
                return (1, "spades")
            if len(self.hand["diamonds"]) >= 4:
                return (1, "diamonds")
            else:
                return (1, "clubs")
        else:
            return None


