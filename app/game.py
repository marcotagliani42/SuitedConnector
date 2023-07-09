from game_elements import Player, Pot, BettingRound, Card, Board, Hand
import random
from collections import deque
class Game:
    def __init__(self, players, blinds) -> None:
        self.players = players
        self.bigb, self.smallb = blinds
        deck = self.deal_cards()
        for player in self.players:
            player.set_holecards((deck.pop(), deck.pop()))

        self.board = Board(deck[:5])
    
    def run(self):
        stage = 0
        while players and stage < 4:
            self.reveal_cards(stage)
            stage += 1
            round = BettingRound(players)
            players, pots = round.start()
    
    def deal_cards():
        deck = [Card(rank, suit) for rank in range(2,15) for suit in ["h", "s", "d", "c"]]
        random.shuffle(deck)
        return deck
    
    def reveal_cards():
        pass

