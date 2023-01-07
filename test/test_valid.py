import unittest
from unittest import mock
import blackjack


class ValidTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        with mock.patch('builtins.input', return_value="N"):
            self.hands = blackjack.play(1, "2,2") # Runs the game with 1 player, a hand of 2 2s. This ensures the hand shouldn't be bust.

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_valid(self):  # any method beginning with 'test' will be run by unittest
        hand_bust = self.hands[0].bust
        self.assertEqual(hand_bust, False)


if __name__ == '__main__':
    unittest.main()