import random


def display_board(board):  

    s = ' -' *10
    for item in range(1,8,3):        
        print(s + '\n |  ' + board[item] +'  |  ' + board[item+1] + '  |  ' + board[item+2] + '  |')       
    print(s)


def player_input():    
   
    while True:              
        player1 = input("What are you? Please enter X or O: ").upper()
        player2 = ""       

        if player1 == "O":
            player2 = "X"  
            return player1, player2                 
        elif player1 == "X":
            player2 = "O"
            return player1, player2            
        else:             
            print("Please enter a valid value")         


def place_marker(board,marker,position):
    board[position] = marker


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


def who_first():
    if random.randint(0,1) == 0:
        return 'player1'       
     

def is_space_check(board, position): 
    return board[position] != 'X' and board[position] != 'O'
       

def full_board_check(board):
    for cell in board:        
        if (cell != "X" and cell!= "O" and cell != "0"):
            return False
    return True


def player_choice(board):      
    
    while True:
        try:       
            position = int(input('Your next position is (from 1-9): '))
            if (position in range(1,10) and is_space_check(board, position)):      
                return position
            else: 
                print('Either the cell is already marked or the value is not valid')
        except:
            print("Please enter an integer")        
        

def replay():   
    
    while True:
        decision = input('Try again? Y or N: ').lower()
        if decision == 'y':
            return True
        elif decision == 'n':
            print('Thank you and goodbye!')
            return False
        else:
            print('Enter valid value')


def marker_turn(mylist, mystring, x, y):
            
    if mystring == 'player1':
        mylist.append(x)
        mylist.append(y)   
    else:
        mylist.append(y)
        mylist.append(x)         
    return mylist 


while True: 

    print('Welcome to Tic Tac Toe!')      
 
    board = ['0','1','2','3','4','5','6','7','8','9'] 
    turn = []       
    item = 0

    print('')
    player1, player2 = player_input() 
    print('')    
    print(f'You have selected {player1}\nPlayer two is {player2}')        

    print('')
    display_board(board)
    print('')    
  
    if who_first() == 'player1':
        print('Player 1 goes first')
        marker_turn(turn, 'player1', player1, player2) #it will put the markers X and O in turn
    else:
        print('Player 2 goes first')
        marker_turn(turn, 'player2', player1, player2)


    turn = turn * 5
    print('') 
    
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
    

