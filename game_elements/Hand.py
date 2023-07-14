from collections import defaultdict, Counter
from itertools import permutations
from enum import Enum, unique

@unique
class HandStrength(Enum):
    HIGHCARD = 1
    PAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULLHOUSE = 7
    FOUROFAKIND = 8
    STRAIGHTFLUSH = 9
class Hand:

    def __init__(self, cards) -> None:
        if len(cards) != 5:
            raise ValueError("not a valid hand")
        self.strength, self.card_strength = self.evaluate_hand(cards)
    
    def get_strength(self):
        return self.rank
    def get_cardstrength(self):
        return self.card_strength
    
    def evaluate_hand(self, cards):
        count_ranks = self.create_countranks(cards)
        return self.handstrength(count_ranks, cards), self.cardstrength(count_ranks)
    
    def create_countranks(self,cards):
        count_ranks = defaultdict(list)
        for rank, count in Counter([card.getRank() for card in cards]).items():
            count_ranks[count].append(rank.value)
        return count_ranks
    
    def cardstrength(self, count_ranks):
        res = []
        for count, ranks in sorted(count_ranks.items(), reverse=True).items():
            res += sorted(ranks)

        return tuple(res)

    def isStraight(self,cards):
        cards = sorted(cards)
        ace_first = cards[-1] + cards[:4]
        return self.straight_helper(cards) or self.straight_helper(ace_first)
    
    
    def straight_helper(self,cards):
        for i in range(4):
            if not (cards[i+1] == cards[i].getNext()):
                return False
        return True
    
    def isFlush(self,cards):
        suit = ""
        for card in cards:
            if suit == "":
                suit = card.getSuit()
            elif card.getSuit() != suit:
                return False
        
        return True
    

    def handstrength(self, count_ranks, cards):
        straight = self.isStraight(cards)
        flush = self.isFlush(cards)

        if straight and flush:
            return HandStrength["STRAIGHTFLUSH"]
        if 4 in count_ranks:
            return HandStrength["FOUROFAKIND"]
        if 3 in count_ranks and 2 in count_ranks:
            return HandStrength["FULLHOUSE"]
        if flush:
            return HandStrength["FLUSH"]
        if straight:
            return HandStrength["STRAIGHT"]
        if 3 in count_ranks:
            return HandStrength["THREEOFAKIND"]
        if 2 in count_ranks:
            return HandStrength["TWOPAIR"] if len(count_ranks[2]) == 2 else HandStrength["PAIR"]
        return HandStrength["PAIR"]
    
    def compare_cardstrength(self,list1,list2):
        for i in range(len(list1)):
            if list1[i] > list2[i]:
                return 1
            else:
                return -1
        return 0
    
    def __eq__(self, other: object) -> bool:
        return self.strength == HandStrength[other] and self.compare_cardstrength(self.card_strength, other.card_strength)

    def __lt__(self, other):
        if self.strength == other.get_strength():
            return self.compare_cardstrength(self.card_strength, other.get_cardstrength()) == -1
        return self.strength < other.get_strength()
    
    def __gt__(self, other):
        return not (self < other or self == other)
  