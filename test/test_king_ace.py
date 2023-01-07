import unittest
from unittest import mock
import blackjack


class KingAceTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        with mock.patch('builtins.input', return_value="N"):
            self.hands = blackjack.play(1, "13,1") # Runs the game with 1 player, a hand of a kings and an ace.

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_king_ace(self):  # any method beginning with 'test' will be run by unittest
        hand_score = self.hands[0].total
        self.assertEqual(hand_score, 21)


if __name__ == '__main__':
    unittest.main()