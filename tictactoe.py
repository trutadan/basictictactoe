# global variables
game_active = True
winner = None
current_player = None
steps = 1

# game's structure
def play_game():
    """Initialize the game, and create game resources."""

    # displays the initial board..
    display_board()

    # lets the player decide between X and O
    global current_player
    current_player = input("Choose: X or O ?")

    while current_player not in ["X", "O"]:
        current_player = input("Invalid input. Choose: X or O ?")

    # runs as long as the game is active
    while game_active:
        global steps

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # checks if the game had ended
        check_game_over()

        # flips the turn to the other player
        flip_player()

        # helps the game decide when it's a tie
        steps = steps + 1

    # the end of the game
    if winner == "X" or winner == "O":
        print(f"{winner} won. Congratulations!")
    elif winner == None:
        print("Tie.")

def handle_turn(player):
    """Handle a single turn of an arbitrary player."""

    print(f"{current_player}'s turn.")
    position = input("Choose a position from 1 to 9: ")

    auxiliar = False
    while not auxiliar:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1 to 9: ")

        position = int(position) - 1

        if board_positions[position] == "X" or board_positions[position] == "O":
            print(f"The position {position+1} is already occupied. ")
        else:
            auxiliar = True


    board_positions[position] = current_player

    display_board()

def check_game_over():
    """Checks if the game is over."""
    check_win()
    check_tie()

def check_win():
    """Checks for a winner."""
    global winner

    # checks rows
    row_winner = check_rows()

    # checks columns
    column_winner = check_columns()

    # checks diagonals
    diagonal_winner = check_diagonals()

    # searches for a winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    # sets the global variable
    global game_active

    # checks if any of the rows have all the same value
    row_1 = board_positions[0] == board_positions[1] == board_positions[2]
    row_2 = board_positions[3] == board_positions[4] == board_positions[5]
    row_3 = board_positions[6] == board_positions[7] == board_positions[8]

    # stops the game if someone wins and returns the winner
    if row_1:
        game_active = False
        return board_positions[0]
    elif row_2:
        game_active = False
        return board_positions[3]
    elif row_3:
        game_active = False
        return board_positions[6]

def check_columns():
    # sets the global variable
    global game_active

    # checks if any of the columns have all the same value
    column_1 = board_positions[0] == board_positions[3] == board_positions[6]
    column_2 = board_positions[1] == board_positions[4] == board_positions[7]
    column_3 = board_positions[2] == board_positions[5] == board_positions[8]

    # stops the game if someone wins and returns the winner
    if column_1:
        game_active = False
        return board_positions[0]
    elif column_2:
        game_active = False
        return board_positions[1]
    elif column_3:
        game_active = False
        return board_positions[2]

def check_diagonals():
    # sets the global variable
    global game_active

    # checks if any of the diagonals have all the same value
    diagonal_1 = board_positions[0] == board_positions[4] == board_positions[8]
    diagonal_2 = board_positions[2] == board_positions[4] == board_positions[6]

    # stops the game if someone wins and returns the winner
    if diagonal_1:
        game_active = False
        return board_positions[0]
    elif diagonal_2:
        game_active = False
        return board_positions[2]

def check_tie():
    """Checks if the game ended in a draw."""
    global game_active
    if steps == 9:
        game_active = False

def flip_player():
    # global variable
    global current_player

    # flips the turn to the other player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

# game's board
board_positions = ["1", "2", "3",
                   "4", "5", "6",
                   "7", "8", "9"]

def display_board():
    """Draws the board on the screen."""
    print(f" {board_positions[0]} | {board_positions[1]} | {board_positions[2]}")
    print("- - - - - -")
    print(f" {board_positions[3]} | {board_positions[4]} | {board_positions[5]}")
    print("- - - - - -")
    print(f" {board_positions[6]} | {board_positions[7]} | {board_positions[8]}")

# starts the game
play_game()