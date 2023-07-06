class Game:
    def __init__(self, players, player_limit) -> None:
        self.players = players
        self.player_limit = player_limit

    def remove_player(self, player):
        for i in range(len(self.players)):
            if player == self.players[i]:
                self.players.remove(i)

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
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit

class Board:
    def __init__(self, cards) -> None:
        self.cards = cards

    def evaluate(self,card1,card2):
        self.cards.append(card1)
        self.cards.append(card2)
        best_hand = max(self.combinations())
        self.cars.pop()
        self.cars.pop()

        return best_hand
    
    def combinations(self):
        combinations = [[]]
        for i in range(len(self.cards)):
            combinations += [combo + [self.cards[i]] for combo in combinations]

        return [combo for combo in combinations if len(combo) == 5]
    
for combo in Board(["ac", "ah", "kh", "8h", "7s", "9s", '3d']).combinations():
    print(combo)

    

class Hand:
    values = {}
class BettigRound:
    pass

class Pot:
    def __init__(self) -> None:
        pass