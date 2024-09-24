# Import libraries
from player import Player
from board import Board
import random


# Represents a tic-tac-toe player using purely random moves
class RandomPlayer(Player):

    # Gets the players next random move
    def get_next_move(self, board: Board) -> int:
        open_spaces = board.get_open_spaces()
        return random.choice(open_spaces)
