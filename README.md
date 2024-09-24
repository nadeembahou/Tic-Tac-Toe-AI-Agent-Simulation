# Tic-Tac-Toe-AI-Agent-Simulation
Developed a Python-based Tic-Tac-Toe game framework featuring multiple agent types (random, conditional logic, and utility-based) and an automated experiment system for testing agent strategies. Implemented conditional logic and utility functions for AI decision-making. Designed experiments to evaluate agent performance.


Overview:

Files:
 - tic_tac_toe.py - the main program to play a game of tic tac toe against an agent
 - experiment.py - a program to run a specified number of games with automated players for analysis
 - game.py - represents a game of tic tac toe played by two players
 - board.py - represents a tic tac toe board
 - player.py - represents an abstract player to be implemented by the following subclasses <below>
   - human_player.py - represents an human player who is prompted for input via the console
   - random_player.py - represents an automated player that choses moves at random
   - conditional_player.py - represents an automated agent who uses conditional logic on decisive moves
   - utility_player.py - represents an automated agent who uses a utility function to evaluate moves

Output for tic-tac-toe.py and experiment found as text files. 
 
