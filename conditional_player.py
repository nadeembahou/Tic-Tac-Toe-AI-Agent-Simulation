# Import libraries
from player import Player
from board import Board

# Represents a tic-tac-toe agent that evaluates moves using conditional logic
class ConditionalPlayer(Player):

    # Returns the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        # If the board is not full
        if not board.is_full():
            # Check for decisive moves
            dm = self.get_decisive_move(board)
            if dm != None:
                return dm
            # If no decisive move, check for non-decisive moves
            ndm = self.get_non_decisive_move(board)
            if ndm != None:
                return ndm
        # If no move found, return None
        return None
    
    # Method to find a decisive move
    def get_decisive_move(self, board: Board):
        temp = ['X', 'X', 'O', '-', 'O', '-', '-', '-', '-']
        # If the board is not full
        if not board.is_full():
            # Check if expanding lines reveals a decisive move for the player
            exp = self.expand_line(board, self.mark, self.opponent_mark)
            if exp != None:
                if exp[0] == 2:
                    return exp[1]
            # Check if expanding lines reveals a decisive move for the opponent
            opp_exp = self.expand_line(board, self.opponent_mark, self.mark)
            if opp_exp != None:
                if opp_exp[0] == 2:
                    return opp_exp[1]
        # If no decisive move found, return None
        return None
    
    # Method to find a non-decisive move
    def get_non_decisive_move(self, board: Board):
        # If the board is empty, return the center position
        if board.is_empty():
            return 0
        # If the board is not full
        if not board.is_full():
            # Check if expanding lines reveals a non-decisive move for the player
            exp = self.expand_line2(board, self.mark)
            if exp == None:
                return None
            if exp[0] == 1:
                return exp[1]
            # Check if expanding lines reveals a non-decisive move for the opponent
            opp_exp = self.expand_line2(board, self.opponent_mark)
            if opp_exp == None:
                return None
            if opp_exp[0] == 1:
                return opp_exp[1]
        # If no non-decisive move found, return None
        return None
    
    # Method to expand lines to find decisive moves
    def expand_line(self, board: Board, mark, mark2):
        max = 0
        num = None
        i = 0
        # Example board configuration for reference
        t = ['X', 'X', 'O', '-', 'O', '-', '-', '-', '-']
        for line in board.lines:
            temp = 0
            # Skip the line if it contains opponent's mark
            if board.spaces[line[0]] == mark2 or board.spaces[line[1]] == mark2 or board.spaces[line[2]] == mark2:
                i += 1
                continue
            # Calculate the number of marks for the player in the line
            if board.spaces[line[0]] == mark:
                temp += 1
            if board.spaces[line[1]] == mark:
                temp += 1
            if board.spaces[line[2]] == mark:
                temp += 1
            # Update maximum and corresponding line index
            if temp >= max:
                max = temp
                num = i
            i += 1
        # If no decisive move found, return None
        if num == None:
            return None
        # Find an empty position in the line and return it
        for p in board.lines[num]:
            if board.spaces[p] == '-':
                return (max, p)
    
    # Method to expand lines to find non-decisive moves
    def expand_line2(self, board: Board, mark):
        max = 0
        num = None
        i = 0
        # Example board configuration for reference
        t = ['X', 'X', 'O', '-', 'O', '-', '-', '-', '-']
        for line in board.lines:
            temp = 0
            # Calculate the number of marks for the player in the line
            if board.spaces[line[0]] == mark:
                temp += 1
            if board.spaces[line[1]] == mark:
                temp += 1
            if board.spaces[line[2]] == mark:
                temp += 1
            # Update maximum and corresponding line index
            if temp >= max:
                max = temp
                num = i
            i += 1
        # If no non-decisive move found, return None
        if num == None:
            return None
        # Find an empty position in the line and return it
        for p in board.lines[num]:
            if board.spaces[p] == '-':
                return (max, p)
