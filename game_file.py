#section8
def player_choice(board):

    #Use While Loop: the next position is repeatedly tested until the condition is met. 
   
    position = 0
    
    while position not space_check(board, position):
        position = int(input('Your next position is (from 1-9): '))
        
    return position

    else: 
        return ('please choose another number')
  
    #return instead of print because it is invisible in the output. 
    
    pass
  
 #section9
 def replay():
    return input('Try again? Y or N: ').startswith('y')
    pass
