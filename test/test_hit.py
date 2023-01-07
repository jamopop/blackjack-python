import unittest
from unittest import mock
import blackjack


class HitTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        with mock.patch('builtins.input', return_value="Y"):
            self.hands = blackjack.play(1, "5,5", 1) # Runs the game with 1 player, a hand of "5,5", and a round limit of 1. This ensures there are no unexpected prompts i.e. asking for ace choice.

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_hit(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.hands[0].cards)
        self.assertEqual(number_of_cards, 3)


if __name__ == '__main__':
    unittest.main()
