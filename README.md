A Simple Tic-Tac-Toe Game.
 implementation of the classic Tic Tac Toe game for two players. Players take turns entering row and 
 column numbers to place their “X” or “O” on the board. T
 he game continues until one player wins or the board is full.

How to Play
  Run the tic_tac_toe.py script in your terminal or command prompt.
  Players take turns entering their moves by specifying the row and column (e.g., “1 2” for the top row, middle column).
  The game will display the current state of the board after each move.
  The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins!
  If no winner is found, the game ends in a draw.

Code Explanation:
`print_board(board)`
def print_board(board):
    for i, row in enumerate(board):
        if i > 0:
            print("_" * 9)
        print(" | ".join(row))
This function prints the current state of the board.
It iterates through each row of the board and prints it.
A separator line is printed between rows to enhance readability.

`check_winner(board, player)`
def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
    
This function checks if the given player has won.
It checks all rows, columns, and diagonals to see if any of them contain three of the player's marks.
Returns True if the player has won, otherwise False.

`play_game()`
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row and column (i.e., 1 2): ").split())
        if board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Try again.")
This function manages the game loop.
It initializes an empty 3x3 board and sets the starting player to "X".
The game runs in a loop, printing the board and asking the current player for their move.
It updates the board with the player's move and checks for a winner.
If a cell is already taken, it prompts the player to choose another cell.
The game ends when a player wins, and the final board state is printed.
