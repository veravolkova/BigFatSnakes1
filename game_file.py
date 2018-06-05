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
  
  
  #5 Still thinking...
