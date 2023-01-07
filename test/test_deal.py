import unittest
from unittest import mock
import blackjack


class DealTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        with mock.patch('builtins.input', return_value="1"):
            self.hands = blackjack.play(1)

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_deal(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.hands[0].cards)
        self.assertEqual(number_of_cards, 2)


if __name__ == '__main__':
    unittest.main()
