import unittest
from cardGame import Card, CardGame

class TestCardGame(unittest.TestCase):

    def test_check_for_ace(self):
        game = CardGame()
        card_ace = Card('Spades', 1)
        card_not_ace = Card('Hearts', 5)
        self.assertTrue(game.check_for_ace(card_ace))
        self.assertFalse(game.check_for_ace(card_not_ace))

    def test_highest_card(self):
        game = CardGame()
        card1 = Card('Diamonds', 8)
        card2 = Card('Clubs', 8)
        self.assertEqual(game.highest_card(card1, card2), card2)
    
    def test_cards_total(self):
        game = CardGame()
        cards = [Card('Hearts', 3), Card('Spades', 7), Card('Diamonds', 2)]
        total = game.cards_total(cards)
        self.assertEqual(total, "You have a total of 12")

if __name__ == "__main":
    unittest.main()
