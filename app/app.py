class App:
    pass
class Table:
    def __init__(self, player_limit, buyin, blinds) -> None:
        self.player_limit = player_limit
        self.buyin = buyin

    def remove_player(self, removed):
        self.players = [player for player in self.players if player != removed]

    def add_player(self,player):
        if len(self.players) == self.player_limit:
            return False
        else:
            self.players.append(player)
        return True