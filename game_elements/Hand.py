from collections import defaultdict, Counter
from itertools import permutations

class Hand:
    ranks = {"highcard":0, "pair": 1, "twopair":2, "trips": 3,
               "straight": 4, "flush": 5, "fullhouse":6, "quads":7, "straightflush": 8}

    def __init__(self, cards) -> None:
        self.cards = cards

        count_ranks = defaultdict(list)
        for rank, count in Counter([card.getRank() for card in self.cards]).items():
            count_ranks[count].append(rank)
        
        self.count_ranks = count_ranks
        self.rank, self.card_strength = self.evaluate_hand()
        
    def evaluate_hand(self):
        return self.rank_hand(self.count_ranks), self.get_card_strength(self.count_ranks)
    
    def get_card_strength(self):
        res = []
        for count, ranks in sorted(self.count_ranks, reverse=True).items():
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
            if suit == "":
                suit = card.getSuit()
            elif card.getSuit() != suit:
                return False
        
        return True
    

    def rank_hand(self):

        if self.straight() and self.flush():
            return "straightflush"
        if 4 in self.count_ranks:
            return "quads"
        if 3 in self.count_ranks and 2 in self.count_ranks:
            return "fullhouse"
        if self.flush():
            return "flush"
        if self.straight():
            return "straight"
        if 3 in self.count_ranks:
            return "trips"
        if 2 in self.count_ranks:
            return "twopair" if len(self.count_ranks[2] == 2) else "pair"
        return "highcard"
    
    def __eq__(self, other: object) -> bool:
        return Hand.ranks[self.hand] == Hand.ranks[other] and self.card_strength == other.card_strength

    def __lt__(self, other):
        if Hand.ranks[self.hand] == Hand.ranks[other]:
            return self.card_strength < other.card_strength
        return Hand.ranks[self.hand] < Hand.ranks[other]
    
    def __gt__(self, other):
        return not (self < other or self == other)
  