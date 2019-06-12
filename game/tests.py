from django.test import TestCase
from game.game_manager import GameManager


class GameTestCase(TestCase):
    def setUp(self):
        self.case1 = GameManager(number_of_players=2,
                                 sequence='RYGPBRYGBRPOP',
                                 deck='R, B, GG, Y, P, B, P, RR')
        self.case2 = GameManager(number_of_players=2,
                                 sequence='​RYGRYB',
                                 deck='R, YY, G, G, B')
        self.case3 = GameManager(number_of_players=3,
                                 sequence='QQQQQQQQQ',
                                 deck='Q, QQ, Q, Q, QQ, Q')

    def test_game_results_is_valid(self):
        self.assertEqual(self.case1.result(), 'Player 1 won after 7 cards.')

    def test_game_two_win_results_is_valid(self):
        self.assertEqual(self.case2.result(), 'Player 2 won after 4 cards.')

    def test_game_results_with_common_squares_valid(self):
        self.assertEqual(self.case3.result(), 'No player won after 6 cards.')
