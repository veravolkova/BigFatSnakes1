## Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
## new
def is_space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

##Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def player_choice(board):
    for cell in board:
        if cell == ' ':
            return False
    return True
