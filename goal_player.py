import time
from board import Board
from utility_player import UtilityPlayer
import math


class GoalPlayer(UtilityPlayer):
    def get_next_move(self, board: Board) -> int:
        start_time = time.time()
        '''dm = self.get_decisive_move(board)
        if dm != None:
            print("--- %s seconds ---" % (time.time() - start_time))
            return dm'''
        state = ''.join(board.spaces)
        mark = self.mark
        bm = self.find_best_move(state, mark)
        print("--- %s seconds ---" % (time.time() - start_time))
        return bm

    def evaluate(self, state):
        """
        Function to evaluate the state of the tic-tac-toe game.
        Returns 1 if 'X' wins, -1 if 'O' wins, and 0 for draw or incomplete game.
        """
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for condition in win_conditions:
            if state[condition[0]] == state[condition[1]] == state[condition[2]]:
                if state[condition[0]] == self.mark:
                    return 1
                elif state[condition[0]] == self.opponent_mark:
                    return -1

        if '-' not in state:
            return 0  # Draw
        else:
            return None  # Incomplete game

    def minimax(self, state, depth, maximizing_player):
        """
        Minimax function to find the best move in the tic-tac-toe game.
        """
        score = self.evaluate(state)
        if score is not None:
            return score

        if maximizing_player:
            max_eval = -math.inf
            for i in range(len(state)):
                if state[i] == '-':
                    new_state = state[:i] + self.mark + state[i + 1:]
                    eval = self.minimax(new_state, depth + 1, False)
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for i in range(len(state)):
                if state[i] == '-':
                    new_state = state[:i] + self.opponent_mark + state[i + 1:]
                    eval = self.minimax(new_state, depth + 1, True)
                    min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self, state, mark):
        """
        Function to find the best move for the given state and mark ('X' or 'O').
        """
        best_move = None
        best_score = -math.inf if mark == self.mark else math.inf

        for i in range(len(state)):
            if state[i] == '-':
                if mark == self.mark:
                    new_state = state[:i] + mark + state[i + 1:]
                    score = self.minimax(new_state, 0, False)
                    if score > best_score:
                        best_score = score
                        best_move = i
                else:
                    new_state = state[:i] + mark + state[i + 1:]
                    score = self.minimax(new_state, 0, True)
                    if score < best_score:
                        best_score = score
                        best_move = i

        return best_move
