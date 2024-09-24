
import time
from board import Board
from conditional_player import ConditionalPlayer


# Represents a tic-tac-toe agent evaluating moves with a utility function
# Note: this agent inherits from a conditional player
# Note: it uses it's conditional logic for making decisive moves
class UtilityPlayer(ConditionalPlayer):

    # Gets the next move using an utility function
    # and conditional logic for decisive moves
    def get_next_move(self, board: Board) -> int:
        start_time = time.time()
        if board.is_empty():
            return 0
        dm = self.get_decisive_move(board)
        if dm != None:
            print("--- %s seconds ---" % (time.time() - start_time))
            return dm
        utilities = self.get_utility_of_spaces(board)
        max = -99
        num = -1
        for i in range(len(utilities)):
            if max < utilities[i]:
                max = utilities[i]
                num = i
        print("--- %s seconds ---" % (time.time() - start_time))
        return num

    # Place mark in a spot and get utility of the new state of the board
    def get_utility_of_spaces(self, board: Board):
        utilities = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(board.spaces)):
            if board.spaces[i] != '-':
                utilities[i] = -99
            else:
                utilities[i] = self.get_utility(board, i)
        return utilities

    def get_utility(self, board: Board, i):
        spaces = board.spaces.copy()
        spaces[i] = self.mark
        utility = 0
        for l in board.lines:
            c1 = 0
            c2 = 0
            for p in l:
                if board.spaces[p] == self.mark:
                    c1 += 1
                if board.spaces[p] == self.opponent_mark:
                    c2 += 1
            if c2 == 0:
                if c1 == 1:
                    utility += 1
                if c1 == 2:
                    utility += 3
            if c1 == 0:
                if c2 == 1:
                    utility -= 1
                if c2 == 2:
                    utility -= 3
        return utility
