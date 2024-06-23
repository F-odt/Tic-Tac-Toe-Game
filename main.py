def print_board(board):
    # Iterate through each row in the board with its index
    for i, row in enumerate(board):
        # Print a separator line after the first row
        if i > 0:
            print("_" * 9)
        # Print the row, joining each cell with a separator " | "
        print(" | ".join(row))


def check_winner(board, player):
    # Check rows, columns, and diagonals for a winning line
    for i in range(3):
        # Check if all cells in the row are the player's symbol
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    # Check the two diagonals for a winning line
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    # Return False if no winning line is found
    return False


def play_game():
    # Initialize a 3x3 board with empty spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Set the current player to "X"
    current_player = "X"

    while True:
        # Print the current state of the board
        print_board(board)
        # Get the player's input for row and column
        row, col = map(int, input(f"Player {current_player}, enter row and column (i.e., 1 2): ").split())
        # Check if the chosen cell is empty
        if board[row - 1][col - 1] == " ":
            # Place the player's symbol in the chosen cell
            board[row - 1][col - 1] = current_player
            # Check if the current player has won
            if check_winner(board, current_player):
                # Print the board and announce the winner
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"
        else:
            # Inform the player that the chosen cell is already taken
            print("Cell already taken. Try again.")


# Start the game
play_game()
