from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from Hand import Hand

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
        ans = input("Enter action amount")
        self.stack -= ans
        return ans.split()[0], int(ans.split()[1])

    
class Card:
    values = {str(num):num for num in range(2,11)}
    values.update({"J":11, "Q":12, "K":13, "A":14})

    def __init__(self, card) -> None:
        self.rank = Card.values[card[0]]
        self.suit = card[1]

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
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