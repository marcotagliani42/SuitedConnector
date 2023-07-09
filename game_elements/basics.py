from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

class Player:
    def __init__(self, name, stack) -> None:
        self.name = name
        self.stack = stack
        self.hole_cards = tuple()

    def set_holecards(self, cards):
        self.hole_cards = cards
    
    def pay(self,amount):
        self.stack += amount

    #todo
    def getAction(self, to_call):
        ans = input("Enter action amount")
        return ans.split()[0], int(ans.split()[1])

    
class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

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
        for i in range(5):
            print(self.cards[i])
            yield