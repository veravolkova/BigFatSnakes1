Maris_section
#write your code here
#create board

#4 Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.:

def check_win(board,mark):

if ((board[0] == mark and board[1] == mark and board[2]== mark)
or (board[3] == mark and board[4] == mark and board[5]== mark)
or (board[6] == mark and board[7] == mark and board[8]== mark)
or (board[0] == mark and board[3] == mark and board[6]== mark)
or (board[1] == mark and board[4] == mark and board[7]== mark)
or (board[2] == mark and board[5] == mark and board[8]== mark)
or (board[0] == mark and board[4] == mark and board[8] == mark)
or (board[2] == mark and board[4] == mark and board[6]== mark))

    print('You won!')
  
  #5 

def who_first():
    
    if randint(0,1) == 0:
        
        return 'Player 1 goes first!'
    else:
        return 'Player 2 goes first!'

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
test
