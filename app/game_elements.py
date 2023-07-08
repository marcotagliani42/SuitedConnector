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
    
    def __eq__(self, other: object) -> bool:
        return Hand.ranks[self.hand] == Hand.ranks[other] and self.card_strength == other.card_strength

    def __lt__(self, other):
        if Hand.ranks[self.hand] == Hand.ranks[other]:
            return self.card_strength < other.card_strength
        return Hand.ranks[self.hand] < Hand.ranks[other]
    
    def __gt__(self, other):
        return not (self < other or self == other)
    
class BettingRound:
    def __init__(self, pots, player_tocall, potlimit = False) -> None:
        self.potlimit = potlimit
        self.player_tocall = player_tocall
        self.pots = pots
    
    def start(self):
        calls = set(self.player_tocall[-2][0])

        while len(calls) < len(self.player_tocall):
            
            player, to_call = self.player_tocall.popleft()
            action = player.getAction(to_call)

            if action[0] == "call":
                calls.add(player)
                self.player_tocall.append((player,0))
                
            elif action[0] == "raise":
                self.player_tocall = [(player, due+action[1]) for player,due in self.players_tocall] 
                calls = set(player)
                self.player_tocall.append((player,0))
            
            elif action[0] == "fold":
                for pot in self.pots:
                    pot.fold_player(player)
            
            elif action[0] == "allin" and action[1] <= to_call:
                new_pot = Pot([player for player,due in self.player_tocall])
                self.pots.append(new_pot)
            else:
                pass
            
    
class Pot:
    def __init__(self, players, amount = 0) -> None:
        self.amount = amount
        self.players = players

    def payout(self, board):
        winners = board.get_winners(self.players)
        for winner in winners:
            winner.pay(self.amount//len(winners))
    
    def fold_player(self,player):
        self.players.remove(player)
    
    def getAmount(self):
        return self.amount