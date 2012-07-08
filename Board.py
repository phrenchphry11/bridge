#! /usr/bin/env python

import Deck
import Player


class Board(object):
    def __init__(self, player1, player2, player3, player4, deck):
        self.p1 = player1
        self.p2 = player2
        self.p3 = player3
        self.p4 = player4
        self.deck = deck
        self.team1 = [self.p1, self.p3]
        self.team2 = [self.p2, self.p4]

    def deal(self):
        shuffled_deck = self.deck.shuffle_and_return()
        for i in range(0,len(shuffled_deck),4):
            self.p1.hand[shuffled_deck[i][0]].append(shuffled_deck[i][1])
            self.p2.hand[shuffled_deck[i+1][0]].append(shuffled_deck[i+1][1])
            self.p3.hand[shuffled_deck[i+2][0]].append(shuffled_deck[i+2][1])
            self.p4.hand[shuffled_deck[i+3][0]].append(shuffled_deck[i+3][1])
        self.p1.count_points()
        self.p2.count_points()
        self.p3.count_points()
        self.p4.count_points()

    def bid(self):
        opener = None
        for player in [self.p1, self.p2, self.p3, self.p4]:
            first_bid = player.open_bid()
            opener = player
            if first_bid:
                break
        if not first_bid:
            return None
        else:
            for player in [self.p1, self.p2, self.p3, self.p4]:
                response = player.response_bid(opener, first_bid)
            print response
            if not response:
                return first_bid


def main():
    player1 = Player.Player(name="gyorgy")
    player2 = Player.Player(name="istvan")
    player3 = Player.Player(name="lorant")
    player4 = Player.Player(name="kovacs")
    player1.team = player3
    player3.team = player1
    player2.team = player4
    player4.team = player2
    deck = Deck.Deck()
    board = Board(player1, player2, player3, player4, deck)
    board.deal()
    print board.bid()

if __name__ == '__main__':
    main()
