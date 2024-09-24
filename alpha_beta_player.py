#Sources:  Lecture notes, videos, GPT/Gemini, Previous code.

# Import libraries
from player import Player  # Import the base Player class
from board import Board  # Import the Board class


# Represents a minimax agent with alpha-beta pruning
class AlphaBetaPlayer(Player):

    # Gets the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        # Call the alpha-beta function to find the best move
        _, move = self.alpha_beta(board, float('-inf'), float('inf'), True)
        return move

    # Perform alpha-beta pruning to get the minimax score for the current board state
    def alpha_beta(self, board: Board, alpha: float, beta: float, maximizing_player: bool) -> (float, int):
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
                # Recursively call alpha-beta for the child board
                eval, _ = self.alpha_beta(child_board, alpha, beta, False)
                # Update the maximum evaluation value and best move
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                # Update alpha
                alpha = max(alpha, eval)
                # Perform alpha-beta pruning
                if beta <= alpha:
                    break
            # Return the maximum evaluation value and the best move
            return max_eval, best_move
        else:
            # If the player is minimizing, perform similar steps as maximizing player
            min_eval = float('inf')
            best_move = None
            for move in board.get_legal_moves():
                child_board = board.copy()
                child_board.make_move(move, self.opponent_mark)
                eval, _ = self.alpha_beta(child_board, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    # Gets the minimax score for the current board state (used for testing)
    def get_minimax(self, board: Board, maximizing_player: bool, alpha: float, beta: float) -> float:
        if board.is_terminal():
            return self.get_score(board)

        if maximizing_player:
            max_eval = float('-inf')
            for move in board.get_legal_moves():
                child_board = board.copy()
                child_board.make_move(move, self.mark)
                eval = self.get_minimax(child_board, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.get_legal_moves():
                child_board = board.copy()
                child_board.make_move(move, self.opponent_mark)
                eval = self.get_minimax(child_board, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    # Gets the score of the current board state
    def get_score(self, board: Board) -> float:
        if board.has_win(self.mark):
            return 10
        elif board.has_win(self.opponent_mark):
            return -10
        else:
            return 0
