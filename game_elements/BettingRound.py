from collections import deque


class BettingRound:
    
    def run(players,pot,blinds):
        player_tocall = BettingRound.create_ptc()
        calls = set(player_tocall[-2][0])
        
        while len(calls) < len(player_tocall):
            
            player, to_call = player_tocall.popleft()
            action = player.getAction(to_call)

            if action == to_call:
                calls.add(player)
                player_tocall.append((player,0))
                
            elif action > to_call:
                player_tocall = [(player, due+action[1]) for player,due in player_tocall] 
                calls = set(player)
                player_tocall.append((player,0))
            
            else:
                pot.fold_player(player)
            
            if 0 == player.get_stack():
                player_tocall.pop()
                calls.remove(player)

            pot.place_bet(action, player)
        
        return list(calls), pot
    
    def create_ptc(self,players, blinds):
        queue = deque([[player, blinds[1]] for player in players])
        queue[-2][1] = blinds[1] - blinds[0]
        queue[-1][1] = 0

        return queue