"""
Algorithm to generate all possible board states of a tic-tac-toe game using a Depth-first approach.

Completeness: Always finds an answer, the answer can be a draw or a winnable condition for either player
Optimization: Doesn't always find the lowest cost/best way
Time Complexity: O(M+N) where M is the number of all states and N is the number of moves for all states
Space Complexity O(M+N) where M is the number of states (including the initial empty state) necessary to get to the end of a branch, into a win/draw situation and N is the number of moves to get to that end state

Author: Giovanni Rebouças
Date: 18/05/2021
"""

# Constants for board symbols
X_SYMBOL = "X"
O_SYMBOL = "O"
EMPTY_SYMBOL = "."

# Generate the default board format which is ALL empty spaces
DEFAULT_BOARD = EMPTY_SYMBOL * 9

# Templates for all possible winning conditions:
WINNING_CONDITION_TEMPLATES = [
    (0, 1, 2),  # First row, all X's or O's
    (3, 4, 5),  # Second row, all X's or O's
    (6, 7, 8),  # Third row, all X's or O's
    (0, 3, 6),  # First column, all X's or O's
    (1, 4, 7),  # Second column, all X's or O's
    (2, 5, 8),  # Third column, all X's or O's
    (0, 4, 8),  # Main diagonal, all X's or O's
    (2, 4, 6)   # Opposite diagonal, all X's or O's
]


def isWinnableState(board):
    """
    Returns True if the board first ANY of the winnable conditions indicated by a triple X or triple O sequence in all possible states in WINNING_CONDITION_TEMPLATES

    Params:
    board | string/List(char) - current board state

    Returns:
    boolean | True if the board fits to a pre-defined winnable condition, false otherwise
    """
    return any("".join(board[pos] for pos in condition) in ["XXX", "OOO"] for condition in WINNING_CONDITION_TEMPLATES)


def simulateMove(board, playerSymbol, position):
    """
    Simulates a move by splitting the board list along the requested position and then, through list slicing, replacing the EMPTY_SYMBOL with playerSymbol.

    Params:
    board | string/List(char) - current board state
    playerSymbol | char - what symbol is the player (X or O)
    position | int - what board position should be replaced with playerSymbol

    Returns:
    string/List(char) | New board state with simulated move
    """
    # By calling board[:position] we get everything up until, but not including the position we are at.
    # By calling board[position + 1:] we get everything from the next position over from our position.
    # By using the '+' operator we can concatenate the 2 split strings with our playerSymbol, therefore simulating a replace option
    newBoard = board[:position] + playerSymbol + board[position + 1:]

    return newBoard


def generateBoardStates(board=DEFAULT_BOARD, player=None):
    """
    Generate all possible, VALID board combinations using a DEPTH-first approach.

    Params:
    board | string/List(char) - current board state | Defaults to an all empty board
    player | char - what symbol is the player (X or O) | Defaults to None, player hasn't "chosen" his symbol yet

    No returns, but yields many values that can later be piped into a list.
    """
    # This step makes sure that the ROOT board state is an all empty board and the we will generate all possible moves if X or if O goes first
    if player is None:
        # This is the empty board and it IS a valid board state
        yield board

        # Generate all boards states when X goes first
        for boardstate in generateBoardStates(board, player=X_SYMBOL):
            yield boardstate

        # Generate all boards states when O goes first
        for boardstate in generateBoardStates(board, player=O_SYMBOL):
            yield boardstate

        return

    # Define the opponent type by the player type. If player is X, opponent is O. If player is O or None, opponent is X
    if player is X_SYMBOL:
        opponent = O_SYMBOL
    else:
        opponent = X_SYMBOL

    # For each cell in the board, get it's position and "value"
    for pos, cell in enumerate(board):
        # Make sure this cell is an empty symbol and therefore, we can simulate a move
        if cell is not EMPTY_SYMBOL:
            continue

        # Simulate a move and return the new board state
        playedBoard = simulateMove(board, player, pos)
        yield playedBoard

        # Check if the new board meets winning conditions, if so, stop game
        if isWinnableState(playedBoard):
            continue

        # Recursively call the function to return board states for subsequent moves in a Depth-first manner
        for nextBoard in generateBoardStates(playedBoard, opponent):
            yield nextBoard


if __name__ == "__main__":
    # Call function to generate all board states in a depth-first approach
    generateBoardStates()
