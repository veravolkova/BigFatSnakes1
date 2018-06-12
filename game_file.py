import random

'''
#################################################################################
############ FUNCTIONS ##########################################################
#################################################################################
'''

# FUNCTION 1: prints the board
def display_board(board):   
#    print('\n'*100)
   
    s = ' -' *10
    for item in range(1,8,3):        
        print(s + '\n |  ' + board[item] +'  |  ' + board[item+1] + '  |  ' + board[item+2] + '  |')       
    print(s)

# FUNCTION 2: a player chooses X or O mark
def player_input():
    
    player1 = "" 
    while player1 != "O" or player1 != "X":              
        player1 = input("What are you? Please enter X or O: ").upper()
        player2 = ""       

        if player1 == "O":
            player2 = "X"  
            return player1, player2                    
            break            
        elif player1 == "X":
            player2 = "O"
            return player1, player2
            break
        else:             
            print("Please enter a valid value")          

#FUNCTION 3: marking the player's choice on the board
def place_marker(board,marker,position):
    board[position] = marker

# FUNCTION 4: checking out if there is a winner
def check_win(board, mark):

    return (
    (board[1] == mark and  board[2] == mark and board[3] == mark) or    #horizontal rows    
    (board[4] == mark and  board[5] == mark and  board[6] == mark) or
    (board[7] == mark and  board[8] == mark and  board[9] == mark) or    
    (board[1] == mark and  board[4] == mark and  board[7] == mark) or   #vertical rows
    (board[2] == mark and  board[5] == mark and  board[8] == mark) or  
    (board[3] == mark and  board[6] == mark and  board[9] == mark) or      
    (board[1] == mark and  board[5] == mark and  board[9] == mark) or   #diagonal
    (board[3] == mark and  board[5] == mark and  board[7] == mark)) 

# FUNCTION 5: for choosing who goes first
def who_first():
    if random.randint(0,1) == 0:
        return 'player1'       
    else:
        return 'player2'       

# FUNCTION 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def is_space_check(board, position): 
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False   

# FUNCTION 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for cell in board:        
        if (cell != "X" and cell!= "O" and cell != "0"):
            return False
    return True

# FUNCTION 8: Placing markers on the board
def player_choice(board):
    
    position = 0    
    
    while True:       
        position = int(input('Your next position is (from 1-9): '))
        
        if (position in [1,2,3,4,5,6,7,8,9] and is_space_check(board, position)):      
            return position
            break        
        else: 
            print('Either the cell is already marked or the value is not valid')
        
# FUNCTION 9: checks if the user wants to play again
def replay():
    return input('Try again? Y or N: ').lower().startswith('y')

# EXTRA FUNCTION 10 for creating putting X and O in chain
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
    

