import unittest
from unittest import TestCase
from game_elements import Hand, BettingRound, Pot
from game_elements.basics import Card, Player, Board

class TestHand(TestCase):
    pass

class TestBettingRound(TestCase):
    pass

class TestCard(TestCase):
    def test_equivalences(self):
        ad, ah = Card(14, "d"), Card(14, "h")
        self.assertEqual(ah, ad)
        self.assertFalse(ah < ad)
        self.assertFalse(ah > ad)

class TestPot(TestCase):
    def test_three_way_allin(self):
        player_A = Player(25)
        player_B = Player(75)
        player_C = Player(100)

        player_A.set_holecards(("Ac","Ad"))
        player_B.set_holecards(("Kc","Kd"))
        player_C.set_holecards(("Qc","Qd"))

        

        pot = Pot.Pot()
    
class TestBoard(TestCase):
    pass

if __name__ == '__main__':
    unittest.main()