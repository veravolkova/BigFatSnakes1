#imports go first
#from IPython.display import clear_output
import random

'''
#################################################################################
############ FUNCTIONS ##########################################################
#################################################################################
'''


# FUNCTION 1: prints the board. clear_output does not work in my environment. 
# Vera's
# Feel free to test it in your own
def display_board(board):   

# Andrei's comment: to clear the board
    print('\n'*100)

    s = ' -' *10
    for item in range(1,8,3):        
        print(s + '\n |  ' + board[item] +'  |  ' + board[item+1] + '  |  ' + board[item+2] + '  |')       
    print(s)

#test
#test_board = ['0','1','2','3','4','5','6','7','8','9']
#display_board(test_board)


# FUNCTION 2: a player chooses X or O mark
# Tiina's
# try to use meaningful variable names (not a , but marker, for ex.) in your code, otherwise 
# it will be difficult for others to understand your code
def player_input():
    
    player1 = "" 
    while player1 != "O" or player1 != "X":
        #.upper() gives a player more freedom, to use lower case as well
        # we will need both players        
        player1 = input("What are you? Please enter X or O: ").upper()
        player2 = ""       
    #you will need a couple of if statements as well. let's separate an initial one
    #into two parts to have more flexibility
    #and let's include the second player
    #we will need to return the values as we need them in our code later
        if player1 == "O":
            player2 = "X"  
            return player1, player2                    
            break            
        elif player1 == "X":
            player2 = "O"
            return player1, player2
            break
        else: 
            #what if a user has entered an int?
            print("Please enter a valid value")          
#function 2 test   
#player_input()         
        
#FUNCTION 3: marking the player's choice on the board
#It looks ok. You just needed to pass a parameter into display board functions for it to show up
#Like this display_board(the place for your parameter), i.e. display_board(board)

def place_marker(board,marker,position):
    board[position] = marker
    
#function 3 test
#place_marker(test_board,'$',8)
#display_board(test_board)   

# FUNCTION 4: checking out if there is a winner
# Mari's
def check_win(board, mark):

#corrected numbers a bit as we do not use board[0]
#added return instead of print in order to use it later in the code
    return (
    (board[1] == mark and  board[2] == mark and board[3] == mark) or    #horizontal rows    
    (board[4] == mark and  board[5] == mark and  board[6] == mark) or
    (board[7] == mark and  board[8] == mark and  board[9] == mark) or    
    (board[1] == mark and  board[4] == mark and  board[7] == mark) or   #vertical rows
    (board[2] == mark and  board[5] == mark and  board[8] == mark) or  
    (board[3] == mark and  board[6] == mark and  board[9] == mark) or      
    (board[1] == mark and  board[5] == mark and  board[9] == mark) or   #diagonal
    (board[3] == mark and  board[5] == mark and  board[7] == mark)) 

#function 4 test:
#win_check(test_board,'X')    
  

# FUNCTION 5: for choosing who goes first
# Mari
def who_first():
    if random.randint(0,1) == 0:
        #shortened a bit a return statement
        return 'player1'       
    else:
        return 'player2'       

#function 5: testing
#choose_first()


# FUNCTION 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
# Andrey's

# if board[position] == ' ':
# here we will never have ' ' as our board contains numbers from 1-9 
# our_board = ['0','1','2','3','4','5','6','7','8','9'] 
# that is why we can do smth like this
def is_space_check(board, position): 
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False
    #you can write it in one line aso
    #return board[position] != 'X' and board[position] != 'O'

# FUNCTION 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
# Andrey's

def full_board_check(board):
    for cell in board:  
        #the same as in the previous functions
        #as our initial board is board = ['0','1','2','3','4','5','6','7','8','9'] 
        #make sure that it is not zero as well. I added the third condition
        #or you can do smth like this   if is_space_check(board, item)
        if (cell != "X" and cell!= "O" and cell != "0"):
            return False
    return True

# FUNCTION 8: Placing markers on the board
# Jolene's

def player_choice(board):
    
    position = 0    
    
    while True:
        #and is very important here
        position = int(input('Your next position is (from 1-9): '))
        #it is very important to use and here, not or
        if (position in [1,2,3,4,5,6,7,8,9] and is_space_check(board, position)):      
            return position
            break
        #what if the value is not valid or a user chooses the same cell and
        #the system rewrites it? That is why I added the second condition
        else: 
            print('Either the cell is already marked or the value is not valid')
        
# FUNCTION 9: checks if the user wants to play again
# Jolene's
# think about the situation when a user input is an int or anu other leter
# you may also want to say "Goodbye" to a user once he or she chooses 'n'
# added lower() in order to give a user more freedom  
def replay():
    return input('Try again? Y or N: ').lower().startswith('y')

#function 9 test:
#replay()


# EXTRA FUNCTION 10 for creating putting X and O in chain
# Vera's

def marker_turn(mylist, mystring, x, y):
            
    if mystring == 'player1':
        mylist.append(x)
        mylist.append(y)
   
    else:
        mylist.append(y)
        mylist.append(x) 
        
    return mylist 


'''
####################################################################################
############ THE GAME ITSELF #######################################################  
####################################################################################
'''

while True: 

    print('Welcome to Tic Tac Toe!')   
    
# STEP1 this will help us later in the code  
    board = ['0','1','2','3','4','5','6','7','8','9'] 
    turn = []
    marker = ''    
    player1 = ''
    player2 = ''
    item = 0

# STEP2 asking a user if she/he wants to be X or O
    print('')
    player1, player2 = player_input() 
    print('')
    
    print(f'You have selected {player1}\nPlayer two is {player2}')    
    
# STEP3 showing the numbered board
    print('')
    display_board(board)
    print('')
    
# STEP4 determining who goes first    
    if who_first() == 'player1':
        print('Player 1 goes first')
        marker_turn(turn, 'player1', player1, player2) #it will put the markers X and O in turn
    else:
        print('Player 2 goes first')
        marker_turn(turn, 'player2', player1, player2)

#let's define the sequence of the markers
    turn = turn * 5
    print('') 
#    print(turn)     #this line is for testing
     
# STEP5 placing the markers on the board until someone/no one wins
    
    while True:
   
        place_marker(board, turn[item], player_choice(board))
        display_board(board)
                
        if check_win(board,turn[item]):
            print(turn[item] + ' has won! Congrats!') 
            break      

        elif full_board_check(board) == True:
            print('No one has won. Please try again')
            break         
        else: 
            item +=1
            continue
        
    if not replay():
        break
    else: 
        pass #here we can clear the output if the code is in jupyter 

