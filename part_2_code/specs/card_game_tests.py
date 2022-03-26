import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Spades", 10)
        self.card3 = Card("Diamonds", 10)
        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace_when_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

    def test_check_for_ace_not_ace(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card2))

    def test_highest_card_first(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card2, self.card1))

    def test_highest_card_last(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_highest_card_equal(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card2, self.card3))

    def test_cards_total(self):
        self.assertEqual("You have a total of 21", self.card_game.cards_total(self.cards))