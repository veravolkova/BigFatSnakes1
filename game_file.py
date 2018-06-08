# I do not know why this code does not work. 
#It prints out the input question, but even user input is X the loop continues running. This in Jupyter.
#Step 2:
def player_input():
    a = 'd'

    while a != "O"or a != "X":
        a = input("What are you:")
    if a == "O"or a== "X":
        print("You have selected:" + a)