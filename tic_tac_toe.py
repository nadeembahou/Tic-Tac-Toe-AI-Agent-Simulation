
# Import libraries
from game import Game
from human_player import HumanPlayer
from random_player import RandomPlayer
from utility_player import UtilityPlayer
from goal_player import GoalPlayer
from minimax_player import MinimaxPlayer
from alpha_beta_player import AlphaBetaPlayer

# Function to create the second player based on the selected skill level
def create_second_player(skill_level):
    if skill_level == 1:
        return RandomPlayer(2)
    elif skill_level == 2:
        choice = input("Choose skill level for the second player (1 for Utility, 2 for Goal): ")
        if choice == "1":
            return UtilityPlayer(2)
        elif choice == "2":
            return GoalPlayer(2)
        else:
            print("Invalid choice. Defaulting to Utility player.")
            return UtilityPlayer(2)
    elif skill_level == 3:
        choice = input("Choose skill level for the second player (1 for Minimax, 2 for Alpha-Beta): ")
        if choice == "1":
            return MinimaxPlayer(2)
        elif choice == "2":
            return AlphaBetaPlayer(2)
        else:
            print("Invalid choice. Defaulting to Minimax player.")
            return MinimaxPlayer(2)
    else:
        print("Invalid skill level selected.")
        return None

# Loop until the user chooses to exit the program
while True:
    # Ask the user to select the skill level
    print("Select skill level:")
    print("1. Easy (Random move)")
    print("2. Medium (Utility-based and Goal-based)")
    print("3. Hard (Minimax and Alpha-Beta algorithms)")
    skill_level = int(input("Enter the number corresponding to the desired skill level: "))

    # Create the first player as a HumanPlayer
    player1 = HumanPlayer(1)

    # Create the second player based on the selected skill level
    player2 = create_second_player(skill_level)
    if player2 is None:
        break

    # Create a new game using the two players
    game = Game(player1, player2)

    # Play the game to its conclusion
    game.play()

    # Ask the user if they want to continue
    choice = input("Play another game? Y/N: ")

    # Exit the program if the user doesn't want to play anymore
    if choice.upper() != "Y":
        print("Thanks for playing Tic Tac Toe!")
        break