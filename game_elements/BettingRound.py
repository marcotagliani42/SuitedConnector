class BettingRound:
    def __init__(self, pot, players) -> None:
        self.player_tocall = self.create_ptc(players)
        self.pot = pot
    
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
            
            else:
                self.pot.fold_player(player)
    
    def create_ptc(self,players):
        pass
    