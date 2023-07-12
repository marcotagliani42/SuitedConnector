class Pot:
    def __init__(self, players, amount = 0) -> None:
        self.total = amount
        self.player_balance = {player:0 for player in players}

    def payout(self, board):
        winners = board.get_winners(self.player_balance.keys())
        min_balance = min([balance for player, balance in  self.player_balance.items() if player in winners])
        pot = 0        
        for player, balance in self.player_balance.items():
            pot += min(balance,min_balance)
            self.player_balance[player] -= min(balance,min_balance)
            if not self.player_balance[player]:
                del player
        
        self.pay_winners(winners, pot)
        if self.total:
            self.payout(board)

    
    def pay_winners(self,winners,pot):
        for winner in winners:
            winner.pay(pot//len(self.pay_winners))
        self.total -= pot

    def fold_player(self,player):
        self.players.remove(player)
    
    def getAmount(self):
        return self.total
    
    def place_bet(self, bet, player):
        self.total += bet
        self.player_balance[player] += bet
