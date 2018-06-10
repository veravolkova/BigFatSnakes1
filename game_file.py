#8
def player_choice(board):

    #Use While Loop: the next position is repeatedly tested until the condition is met. 
   
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Your next position is (from 1-9): '))
        
    return position
    
    pass
  
 #9
 def replay():
    return input('Try again? Y or N: ').startswith('y')
    pass
