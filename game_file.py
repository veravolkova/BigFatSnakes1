def display_board(board):   
   
    s = ' -' *10
    for item in range(1,8,3):        
        print(s + '\n |  ' + board[item] +'  |  ' + board[item+1] + '  |  ' + board[item+2] + '  |')       
    print(s)

#test
#test_board = ['0','1','2','3','4','5','6','7','8','9']
#display_board(test_board)
