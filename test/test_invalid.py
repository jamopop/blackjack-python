import unittest
from unittest import mock
import blackjack


class InvalidTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        with mock.patch('builtins.input', return_value="N"):
            self.hands = blackjack.play(1, "13,13,2") # Runs the game with 1 player, a hand of 2 kings and a 2. This ensures the hand should be bust. 

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_invalid(self):  # any method beginning with 'test' will be run by unittest
        hand_bust = self.hands[0].bust
        self.assertEqual(hand_bust, True)


if __name__ == '__main__':
    unittest.main()