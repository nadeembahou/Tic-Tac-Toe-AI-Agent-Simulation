# goal_player_tests.py
import unittest
from parameterized import parameterized
from board import Board
from goal_player import GoalPlayer

class GoalPlayerTests(unittest.TestCase):
    @parameterized.expand([
        ('XXO-O----',6),
        ('XXOOO-X--', 5),
        ('XOXXO-O-X',5)
    ])
    def test_goal_player(self, state, expected_move):
        board = Board(state)
        player = GoalPlayer(1)  # Assuming the player ID is 1
        result = player.get_next_move(board)
        self.assertEqual(expected_move, result)
    @parameterized.expand([
        ('XOXXO-O-X',7)
    ])
    def test_goal_player(self, state, expected_move):
        board = Board(state)
        player = GoalPlayer(2)  # Assuming the player ID is 2
        result = player.get_next_move(board)
        self.assertEqual(expected_move, result)

if __name__ == '__main__':
    unittest.main()
