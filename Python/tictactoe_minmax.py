"""
Algorithm to generate all possible board states of a tic-tac-toe game using a Min-Max approach.

Completeness: Always finds an answer, the answer can be a draw or a winnable condition for either player
Optimization: Finds the lowest cost possible for a win, if possible, else, goes for a tie.
Time Complexity: O(N) where N is the number of moves necessary for a win
Space Complexity O(N + M) where is the number of moves necessary for a win and M is how far ahead it looks before reaching a dead-end

Author: Giovanni Rebouças
Date: 19/05/2021
"""
import random


class TicTacToe:
    """
    Class that simulates a match of TicTacToe
    """

    def __init__(self):
        """
        Constructor of class. Calls function to set the game to it's initial state and to store amount of turns.

        Params: None

        Returns: None
        """
        # Set the game to it's initial state on object creation
        self.boardState = [[".", ".", "."],
                           [".", ".", "."],
                           [".", ".", "."]]

        # Make a list of possible players to be choosen at "random" to start
        players = ["X", "O"]

        # Choose "randomly" from possible players
        self.player_turn = random.choice(players)

        # Store which turn we are currently at
        self.turn = 0

    def drawBoard(self):
        """
        Draw the game board's current state.

        Params: None

        Returns: None
        """
        # Since we have a list of 3 lists acting as a matrix, each first element is a row, and each second element is a cell in that row (or a column)
        for row in range(0, 3):
            for column in range(0, 3):
                print(str(self.boardState[row][column]) + "|", end=" ")
            print()  # Make sure we skip to next line, this would be the same as priting \n
        print()  # Make sure we skip to next line, this would be the same as priting \n

    def isEndState(self):
        """
        Checks if the game has ended and returns the winner in each case

        Params: None

        Returns: string | Character representing which player won.
        """
        # Check if it's any of the three possible horizontal win states
        for row in range(0, 3):
            if self.boardState[row] == ["X", "X", "X"] or self.boardState[row] == ["O", "O", "O"]:
                return self.boardState[row][0]

        # Check if it's any of the three possible vertical win states
        for column in range(0, 3):
            if self.boardState[0][column] != "." and self.boardState[0][column] == self.boardState[1][column] == self.boardState[2][column]:
                return self.boardState[0][column]

        # Check if it's a Main diagonal win state
        if self.boardState[0][0] != "." and self.boardState[0][0] == self.boardState[1][1] == self.boardState[2][2]:
            return self.boardState[0][0]

        # Check if it's a Opposite diagonal win state
        if self.boardState[0][2] != "." and self.boardState[0][2] == self.boardState[1][1] == self.boardState[2][0]:
            return self.boardState[0][2]

        # Check if the board is full
        for column in range(0, 3):
            for row in range(0, 3):
                # If we find a single empty field, and the game hasn't ended (obviously), continue playing
                if self.boardState[column][row] == ".":
                    return None

        # If we haven't met any victory conditions, and the board is FULL, then it's a tie.
        return "."

    def max(self):
        """
        Evaluates what move will garner the max points for the O player.

        Params: None

        Returns:
        maxvalue | Represents the value that a particular move will gather. Possible values are -1 (loss), 0 (tie), 1 (win)
        pos_x | Optimal position in the X axis that the player should choose
        pox_y | Optimal position in the Y axis that the player should choose
        """

        # Initialize variables that will store optimal position to play a piece
        pos_x = None
        pos_y = None

        # Set maxvalue to -2 which is the WORST possible outcome (something that isn't even possible by our definition - nothing worse than losing)
        maxvalue = -2

        # Check if we have reached and end state (ties, wins or losses)
        result = self.isEndState()

        # If we have reached an end state, return the function with maxvalue set to the appropriate number and the positions don't really matter, so just set 1,1 (center of the board)
        if result == "X":
            return -1, 1, 1
        elif result == "O":
            return 1, 1, 1
        elif result == ".":
            return 0, 1, 1

        # If we have not reached the end stage, iterate over all empty cells in the board, and calculate it's values in search of the move that will render the biggest maxvalue
        for row in range(0, 3):
            for column in range(0, 3):
                # If it's an empty cell, calculate the value of a possible move in this spot
                if self.boardState[row][column] == ".":
                    # Simulate playing a O to this cell
                    self.boardState[row][column] = "O"

                    # Call min function recursively and let it calculate min values for the entire branch of, the coordinates of other optimal cells aren't going to be used, replace with anonymous variable
                    nextMValue, _, _ = self.min()

                    # If the nextMValue is bigger than the currently stored value in maxvalue, replace it and store the optimal position's coordinates
                    if nextMValue > maxvalue:
                        maxvalue = nextMValue
                        pos_x = row
                        pos_y = column

                    # Reset the previously simulated move to an empty cell
                    self.boardState[row][column] = "."

        # Return value for this particular play and the optimal positions to play your piece
        return maxvalue, pos_x, pos_y

    def min(self):
        """
        Evaluates what move will garner the min points for the X player.

        Params: None

        Returns:
        minvalue | Represents the value that a particular move will gather. Possible values are -1 (win), 0 (tie), 1 (loss)
        pos_x | Optimal position in the X axis that the player should choose
        pox_y | Optimal position in the Y axis that the player should choose
        """

        # Initialize variables that will store optimal position to play a piece
        pos_x = None
        pos_y = None

        # We're initially setting it to 2 as worse than the worst case:
        minvalue = 2

        # Check if we have reached and end state (ties, wins or losses)
        result = self.isEndState()

        # If we have reached an end state, return the function with maxvalue set to the appropriate number and the positions don't really matter, so just set 1,1 (center of the board)
        if result == "X":
            return -1, 1, 1
        elif result == "O":
            return 1, 1, 1
        elif result == ".":
            return 0, 1, 1

        # If we have not reached the end stage, iterate over all empty cells in the board, and calculate it's values in search of the move that will render the biggest maxvalue
        for row in range(0, 3):
            for column in range(0, 3):
                # If it's an empty cell, calculate the value of a possible move in this spot
                if self.boardState[row][column] == ".":
                    # Simulate playing a X to this cell
                    self.boardState[row][column] = "X"

                    # Call max function recursively and let it calculate max values for the entire branch of, the coordinates of other optimal cells aren't going to be used, replace with anonymous variable
                    nextMValue, _, _ = self.max()

                    # If the nextMValue is smaller than the currently stored value in minvalue, replace it and store the optimal position's coordinates
                    if nextMValue < minvalue:
                        minvalue = nextMValue
                        pos_x = row
                        pos_y = column

                    # Reset the previously simulated move to an empty cell
                    self.boardState[row][column] = "."

        # Return value for this particular play and the optimal positions to play your piece
        return minvalue, pos_x, pos_y

    def start(self):
        """
        Starts the match.

        Params: None

        Returns: None
        """

        # Game loop. Go on forever until otherwise specified via return or break statements.
        while True:
            # Draw the current board state
            self.drawBoard()
            # Check if we have reached and end state (ties, wins or losses)
            self.result = self.isEndState()

            # If it has ended (not None), check the winner and print appropriate message
            if self.result is not None:
                if self.result == "X":
                    print('The winner is X!')
                elif self.result == "O":
                    print('The winner is O!')
                elif self.result == ".":
                    print("It's a tie!")

                # Break from the game loop and finish program execution
                return

            # Check whose turn it is, calculate optimal (or randomize) and simulate move
            if self.player_turn == "X":
                # If it's anything past the first turn for this player, try and play the best possible move
                if self.turn > 0:
                    # Get best possible move and the coordinates to play
                    _, px, py = self.min()
                else:  # If it is the first move, randomize a position and increment turn to try and win
                    px = random.randint(0, 2)
                    py = random.randint(0, 2)
                    self.turn += 1

                # Simulate move
                self.boardState[px][py] = "X"

                # Pass turn to opponent
                self.player_turn = "O"

            elif self.player_turn == "O":  # O player always goes for wins from the very first turn
                # Get best possible move and the coordinates to play
                _, px, py = self.max()

                # Simulate move
                self.boardState[px][py] = "O"

                # Pass turn to opponent
                self.player_turn = "X"


if __name__ == "__main__":
    # Generate a pseudo-random seed from system time (implicitly through os.systime)
    random.seed()

    # Instantiate a TicTacToe match
    match = TicTacToe()

    # Start the match
    match.start()
