import unittest
from unittest import TestCase
from game_elements import Hand, BettingRound, Card, Pot, Board

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
    pass
class TestBoard(TestCase):
    pass

if __name__ == '__main__':
    unittest.main()