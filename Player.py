#! /usr/bin/env python
import const


class Player(object):
    def __init__(self, name=None, strategy=None, team=None):
        self.name = name
        self.hand = {}
        self.hand["clubs"] = []
        self.hand["diamonds"] = []
        self.hand["hearts"] = []
        self.hand["spades"] = []
        self.hand_points = 0
        self.strategy = strategy
        self.team = team

    def count_points(self):
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
            self.hand_points += 3
        elif len(self.hand["hearts"]) == 1:
            self.hand_points += 2
        elif len(self.hand["hearts"]) == 2:
            self.hand_points += 1

        if len(self.hand["spades"]) == 0:
            self.hand_points += 3
        elif len(self.hand["spades"]) == 1:
            self.hand_points += 2
        elif len(self.hand["spades"]) == 2:
            self.hand_points += 1

        return self.hand_points

    def open_bid(self):
        if self.hand_points >= 13:
            if self.hand_points >= 16:
                if self.hand_points >= 22:
                    return 2, "clubs"
                elif self.hand_points >= 20:
                    if len(self.hand["spades"]) > 2 and len(self.hand["hearts"]) > 2 and len(self.hand["diamonds"]) > 2 and len(self.hand["clubs"]) > 2:
                        return 2, "no trump"
                elif len(self.hand["spades"]) > 2 and len(self.hand["hearts"]) > 2 and len(self.hand["diamonds"]) > 2 and len(self.hand["clubs"]) > 2:
                    return 1, "no trump"
            if len(self.hand["hearts"]) >= 5:
                return 1, "hearts"
            if len(self.hand["spades"]) >= 5:
                return 1, "spades"
            if len(self.hand["diamonds"]) >= 4:
                return 1, "diamonds"
            else:
                return 1, "clubs"
        elif self.hand_points >= 6:
            if len(self.hand["clubs"]) >= 6:
                return 2, "clubs"
            elif len(self.hand["diamonds"]) >= 6:
                return 2, "diamonds"
            elif len(self.hand["hearts"]) >= 6:
                return 2, "hearts"
            elif len(self.hand["spades"]) >= 6:
                return 2, "spades"
        else:
            return None

    def response_bid(self, opener, opening_bid):
        longest = 0
        long_suite = ""
        for suite in ["clubs", "diamonds", "hearts", "spades"]:
            if len(self.hand[suite]) > longest:
                longest = len(self.hand[suite])
                long_suite = suite
        if opener == self.team:
            if opening_bid == (2,"clubs"):
                if long_suite == "clubs":
                    return 3,"clubs"
                else:
                    return 2, long_suite
            elif self.hand_points >= 6:
                level,suite = opening_bid
                no_trump = True
                for suite in ["clubs", "diamonds", "hearts", "spades"]:
                    if len(self.hand[suite])<=2:
                        no_trump = False
                if len(self.hand[suite]) >= 3:
                    return level+1, suite
                elif no_trump:
                    return level,"no trump"
                else:
                    if long_suite == "clubs":
                        long_suite = const.CLUBS
                    if long_suite == "diamonds":
                        long_suite = const.DIAMONDS
                    if long_suite == "hearts":
                        long_suite = const.HEARTS
                    if long_suite == "spades":
                        long_suite = const.SPADES

                    if long_suite > suite:
                        return level,long_suite
                    else:
                        return level+1, long_suite

            else:
                return None

        else:
            raise NotImplementedError
                

