from collections import Counter, defaultdict
from itertools import combinations, permutations
class Game:
    def __init__(self, players, player_limit) -> None:
        self.players = players
        self.player_limit = player_limit

    def remove_player(self, player):
        for i in range(len(self.players)):
            if player == self.players[i]:
                self.players.remove(i)
                return

    def add_player(self,player):
        if player not in self.players:
            self.players.append(player)
            return True
        return False

class Player:
    def __init__(self, name, stack, identification) -> None:
        self.name = name
        self.stack = stack
        self.id = identification

    def __eq__(self, __value: object) -> bool:
        return __value.id == self.id

class PotLimitPreflop(Game):
    def __init__(self, players, limit) -> None:
        super().__init__(players)
        self.limit = limit

class NoLimitHoldem(Game):
    pass

class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit

class Board:
    def __init__(self, cards) -> None:
        self.cards = cards

    def best_hand(self,card1,card2):

        self.cards.append(card1)
        self.cards.append(card2)
        best_hand = max(list(map(lambda x: Hand(x), combinations(self.cards,5))))
        self.cars.pop()
        self.cars.pop()

        return best_hand
    
class Hand:
    ranks = {"highcard":0, "pair": 1, "twopair":2, "trips": 3,
               "straight": 4, "flush": 5, "fullhouse":6, "quads":7, "straightflush": 8}

    def __init__(self, cards) -> None:
        self.cards = cards

        count_ranks = defaultdict(list)
        for rank, count in Counter([card.getRank() for card in self.cards]).items():
            count_ranks[count].append(rank)

        self.rank, self.card_strength = self.evaluate_hand(count_ranks)
        
    def evaluate_hand(self,count_ranks):
        return self.rank_hand(), self.get_card_strength(count_ranks)
    
    def get_card_strength(self, count_ranks):
        res = []
        for count, ranks in sorted(count_ranks, reverse=True).items():
            res += sorted(ranks)

        return tuple(res)

    def straight(self):
        for permutation in permutations(self.cards):
            for i in range(len(self.cards)-1):
                if ((permutation[i].getRank() + 1) % 13) != permutation[i+1].getRank():
                    break
            if any(lambda x: x.getRank() == 13, permutation) and (permutation[0].getRank() == 13 or permutation[4].getRank() == 13):
                return True
        
        return False
    
    def flush(self):
        suit = ""
        for card in self.cards:
            if not suit:
                suit = card.getSuit()
            elif card.getSuit() != suit:
                return False
        
        return True
    

    def rank_hand(self, count_ranks):

        if self.straight() and self.flush():
            return "straightflush"
        if 4 in count_ranks:
            return "quads"
        if 3 in count_ranks and 2 in count_ranks:
            return "fullhouse"
        if self.flush():
            return "flush"
        if self.straight():
            return "straight"
        if 3 in count_ranks:
            return "trips"
        if 2 in count_ranks:
            return "twopair" if len(count_ranks[2] == 2) else "pair"
        return "highcard"
    
    def __eq__(self, __value: object) -> bool:
        return Hand.ranks[self.hand] == Hand.ranks[__value] and self.card_strength == __value.card_strength

    def __lt__(self, __value):
        if Hand.ranks[self.hand] == Hand.ranks[__value]:
            return self.card_strength < __value.card_strength
        return Hand.ranks[self.hand] < Hand.ranks[__value]
    
    def __gt__(self, __value):
        return not self < __value
class BettigRound:
    pass

class Pot:
    def __init__(self) -> None:
        pass