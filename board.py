# Represents a tic-tac-toe board
class Board:

    # Initializes the board with either the specified or default state
    # Note: The board state is represented as nine character string
    # Note: composed of "X", "O", or "-" (for an empty space)
    def __init__(self, state="---------"):
        self.empty = "-"
        self.spaces = list(state)
        self.size = 3  # Size of the board (assuming it's a 3x3 board)

        # Lines represent each horizontal, vertical, or diagonal win line
        self.lines = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6))

    # Returns true if the board is empty, else false
    def is_empty(self) -> bool:
        for space in self.spaces:
            if space != self.empty:
                return False
        return True

    # Returns true if the board is full, else false
    def is_full(self) -> bool:
        for space in self.spaces:
            if space == self.empty:
                return False
        return True

    # Returns true if the specified space is open, else false
    def is_open_space(self, space: int) -> bool:
        return self.spaces[space] == "-"

    # Returns a list of all open spaces on the board
    def get_open_spaces(self) -> list:
        open_spaces = []
        for i in range(len(self.spaces)):
            if self.spaces[i] == "-":
                open_spaces.append(i)
        return open_spaces

    # Marks a space with the appropriate mark (i.e. "X" or "O")
    def mark_space(self, space: int, mark: str):
        if not self.is_open_space(space):
            raise Exception("Move is not valid.")

        self.spaces[space] = mark

    # Returns true if a win currently exists, else false
    def has_win(self, mark) -> bool:
        for line in self.lines:
            if self.spaces[line[0]] == mark \
                    and self.spaces[line[1]] == mark \
                    and self.spaces[line[2]] == mark:
                return True

        return False

    # Returns a deep copy of the board in its current state
    def copy(self):
        state = str().join(self.spaces)
        new_board = Board(state)
        return new_board

    # Returns a display-friendly grid of the numbered space indexes
    def get_space_indexes(self) -> str:
        return "0 1 2\n3 4 5\n6 7 8\n"

    # Returns a display-friendly grid of the current state of the board
    def __str__(self) -> str:
        return \
            f"{self.spaces[0]} {self.spaces[1]} {self.spaces[2]}\n" + \
            f"{self.spaces[3]} {self.spaces[4]} {self.spaces[5]}\n" + \
            f"{self.spaces[6]} {self.spaces[7]} {self.spaces[8]}\n"
    
    # Returns a list of legal moves available on the board
    def get_legal_moves(self) -> list:
        return self.get_open_spaces()
    
    # Marks a space with the appropriate mark (i.e. "X" or "O")
    def make_move(self, space: int, mark: str):
        if not self.is_open_space(space):
            raise Exception("Move is not valid.")

        self.spaces[space] = mark


    # Checks if the current state of the board is terminal
    def is_terminal(self):
        return self.is_full() or self.has_win("X") or self.has_win("O")
    
    # In your Board class
    def get_children(self, mark):
        children = []
        for i in range(len(self.spaces)):
            if self.spaces[i] == "-":
                child_board = self.copy()  # Create a copy of the board
                child_board.spaces[i] = mark  # Mark the space
                children.append(child_board)
        return children
    
    def utility(self, mark: str) -> int:
        if self.has_win(mark):
            return 1
        elif self.has_win('X' if mark == 'O' else 'O'):
            return -1
        else:
            return 0

    def undo_move(self, move: int):
        self.spaces[move] = '-'

    def check_winner(self) -> str:
        for line in self.lines:
            if self.spaces[line[0]] == self.spaces[line[1]] == self.spaces[line[2]] != self.empty:
                return self.spaces[line[0]]
        return None
    
    def get_state(self, index):
        return self.spaces[index]
    
    def index_to_position(self, index: int) -> tuple:
        return (index // self.size, index % self.size)  # Convert index to row and column positions

    def get_diagonal_indices(self, row: int, col: int) -> tuple:
        if row == col:
            diag1 = [(i, i) for i in range(self.size)]
        else:
            diag1 = None

        if row + col == self.size - 1:
            diag2 = [(i, self.size - 1 - i) for i in range(self.size)]
        else:
            diag2 = None

        return diag1, diag2

    def position_to_index(self, row: int, col: int) -> int:
        return row * self.size + col

    def get_opponent_mark(self, mark):
        return 'O' if mark == 'X' else 'X'