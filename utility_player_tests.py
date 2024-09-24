import unittest
from parameterized import parameterized
from utility_player import UtilityPlayer
from board import Board

class UtilityPlayerTests(unittest.TestCase):
    @parameterized.expand([
        ["---------", 0],
        ["X--------", 1],
        ["OX-X-----", 2],
        ["X-X------", 1],

    ])
    def test_get_next_move(self, state, expected_move):
        board = Board(state)
        player = UtilityPlayer(2)
        result = player.get_next_move(board)
        self.assertEqual(expected_move, result)
    @parameterized.expand([
        ["XXO-O----", 6],

    ])
    def test_get_next_move(self, state, expected_move):
        board = Board(state)
        player = UtilityPlayer(1)
        result = player.get_next_move(board)
        self.assertEqual(expected_move, result)
if __name__ == '__main__':
    unittest.main()
