TiinaBranch
# I do not know why this code does not work. Does someone have any ideas?
#It prints out the input question, but even user input is X the loop continues running. This in Jupyter.
#Step 2:
def player_input():
    a = 'd'

    while a != "O"or a != "X":
        a = input("What are you:")
    if a == "O"or a== "X":
        print("You have selected:" + a)      
#Step 3:
#I could not make this work either. I am not sure how to define the board that is made by the display_board function. Otherwise I think 
#marker needs to be same as the position. After the marker is in right position updated display board would be printed out.

def place_marker(board,marker,position):
    board[position] = marker
    display_board()

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
test

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
TiinaBranch


test
test
