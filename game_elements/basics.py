from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from Hand import Hand
from enum import Enum, unique

class Player:

    def __init__(self, stack, name = None) -> None:
        self.name = name
        self.hole_cards = tuple()

    def set_holecards(self, cards):
        self.hole_cards = cards
    
    def pay(self,amount):
        self.stack += amount
    
    def get_stack(self,stack):
        return self.stack

    #todo. take from stack
    def getAction(self, to_call):
        pass
@unique
class CardRank(Enum):
    DEUCE = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7
    NINE = 8
    TEN = 9
    JACK = 10
    QUEEN = 11
    KING = 12
    ACE = 13

    
class Card:

    def __init__(self, card) -> None:
        self.rank = Card.values[card[0]]
        self.suit = card[1]

    def getRank(self):
        return Card.reverse_values[self.rank]
    
    def getSuit(self):
        return self.suit
    
    def getNext(self):
        pass
    
    def __eq__(self, other: object) -> bool:
        return self.rank == other.rank
    def __lt__(self, other: object) -> bool:
        return self.rank < other.rank
    def __gt__(self, other: object) -> bool:
        return self.rank > other.rank
    def __repr__(self) -> str:
        return f'{self.rank}{self.suit}'

class Board:
    def __init__(self, cards) -> None:
        self.cards = cards

    def best_hand(self,holecards):
        return max(list(map(lambda x: Hand(x), combinations(self.cards+list(holecards),5))))
    
    def get_winners(self, players):
        hands = {player: self.best_hand(player.get_holecards()) for player in players}
        best_hand = max(hands.values())
        return [player for player in players if hands[player] == best_hand]
    
    def show_card(self):
        pass