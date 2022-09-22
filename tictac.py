"""
File: tictac.py
Author: Matt Rushton

Purpose: Two players play a game of Tic-Tac-Toe.
Input: Users chooses a spot on a grid to place either and X or an O.
Output: Show users placement on grid and inform when a victory is attained.

"""

print(f"\nWelcome to Tic-Tac-Toe!\nPlayer One will be X's and Player Two will be O's.\nReady Player One?")

# This function will print the grid
def print_grid():
    print(f"\n{squares[0]}|{squares[1]}|{squares[2]}\n-+-+-\n{squares[3]}|{squares[4]}|{squares[5]}\n-+-+-\n{squares[6]}|{squares[7]}|{squares[8]}\n")
    #for i, square in enumerate(squares): #
    #    #print(f"{[0]}|{[1]}|{[3]}\n-+-+-")
    #    print(f"index {i} is {square}")


squares = [1, 2, 3, 4, 5, 6, 7, 8, 9] # This is our number array for the grid using integers. If you want strings it would be '1', '2', etc

print_grid()

number_input = int(input("X's turn to choose a square (1-9): ")) # We use 'int()' to specify that input will be an integer, not a string.

# for loop looks at each index position in the length of the squares array using range()
# It then compares what's in each index position with the number_input and if it matches, replaces it with an X.
for i in range(len(squares)):
    if squares[i] == number_input:
        squares[i] = 'X'

print_grid()

number_input = int(input("O's turn to choose a square (1-9): ")) # We use 'int()' to specify that input will be an integer, not a string.

# for loop looks at each index position in the length of the squares array using range()
# It then compares what's in each index position with the number_input and if it matches, replaces it with an O.
for i in range(len(squares)):
    if squares[i] == number_input:
        squares[i] = 'O'

print_grid()

