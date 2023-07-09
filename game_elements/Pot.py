class Pot:
    def __init__(self, players, amount = 0) -> None:
        self.amount = amount
        self.players = players

    def payout(self, board):
        winners = board.get_winners(self.players)
    def fold_player(self,player):
        self.players.remove(player)
    
    def getAmount(self):
        return self.amount
    
    def place_bet(self,bet):
        self.amount += bet