class Game:
    def __init__(self, players, player_limit) -> None:
        self.players = players
        self.player_limit = player_limit
    
    def run():
        pass

    def remove_player(self, removed):
        self.players = [player for player in self.players if player != removed]

    def add_player(self,player):
        self.players.append(player)

class PotLimitPreflop(Game):
    def __init__(self, players, limit) -> None:
        super().__init__(players)
        self.limit = limit

class NoLimitHoldem(Game):
    pass