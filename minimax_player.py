# Import libraries
from player import Player
from board import Board
from argmax import argmax

# Represents a brute-force minimax agent
class MinimaxPlayer(Player):

    # Gets the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        # Call the minimax function to find the best move
        _, move = self.minimax(board, True)
        return move

    # Perform minimax algorithm to get the minimax score for the current board state
    def minimax(self, board: Board, maximizing_player: bool) -> (float, int):
        # Check if the current board state is terminal
        if board.is_terminal():
            # If terminal, return the score and None (no move)
            return self.get_score(board), None

        # If the player is maximizing
        if maximizing_player:
            # Initialize the maximum evaluation value
            max_eval = float('-inf')
            best_move = None
            # Iterate over all legal moves
            for move in board.get_legal_moves():
                # Create a copy of the board and make the move
                child_board = board.copy()
                child_board.make_move(move, self.mark)
                # Recursively call minimax for the child board with the opposite player
                eval, _ = self.minimax(child_board, False)
                # Update the maximum evaluation value and best move
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            # Return the maximum evaluation value and the best move
            return max_eval, best_move
        else:
            # If the player is minimizing, perform similar steps as maximizing player
            min_eval = float('inf')
            best_move = None
            for move in board.get_legal_moves():
                child_board = board.copy()
                child_board.make_move(move, self.opponent_mark)
                eval, _ = self.minimax(child_board, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move

    # Gets the minimax score for the current board state (used for testing)
    def get_minimax(self, board: Board, maximizing_player: bool) -> float:
        score, _ = self.minimax(board, maximizing_player)
        return score

    # Gets the score of the current board state
    def get_score(self, board: Board) -> float:
        if board.has_win(self.mark):
            return 10
        elif board.has_win(self.opponent_mark):
            return -10
        else:
            return 0