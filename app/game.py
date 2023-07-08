from game_elements import Player, Pot, BettingRound, Card, Board, Hand
import random
class Game:
    def __init__(self, players) -> None:
        self.players = players

        deck = self.deal_cards()
        for player in self.players:
            player.set_holecards((deck.pop(), deck.pop()))

        self.board = Board(deck[:5])
    
    def run(self):
        pot = Pot()
        for _ in range(4):
            round = BettingRound()
    
    def deal_cards():
        deck = [Card(rank, suit) for rank in range(2,15) for suit in ["h", "s", "d", "c"]]
        random.shuffle(deck)
        return deck

print(Game.deal_cards())


