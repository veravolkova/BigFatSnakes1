## Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

##Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def player_choice(board):
    space = 0
    for cell in range(1,10):
        if space_check(board, cell):
            return False
        else:
            return True
