# Exercise 11-5-2017 - Tic Tac Toe Play
# draw Tic Tac Toe gameboard -
# the game board will be getting input from Player 1
# and then make the computer make a move
# Last updated: 11/05/2017
#
# Inputs - gets input from two players (including one computer) in form of row , col
# checks the input for correctness: i,e ensures that the current spot is free
# - exits if board is full or there is a winner
def createBoard_TicTacToe():
    board = [['-', '-', '-'],['-', '-', '-'], ['-', '-', '-']]
    return board

def drawboard(board):
    print(board[0])
    print(board[1])
    print(board[2])

def userInput1():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    # in a later stage, ask which player wants to go first (user or computer)
    letter = ''     #set letter to blank
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    print (letter)

def checkIfFree(board, playerInput1, playerInput2):
    # check if the value entered by the usesr is free or in use
    cv = True
    print('here -1' , board)
    print(playerInput1)
    print(playerInput2)
    currentValue = board[playerInput1][playerInput2]
    print('here-2', currentValue)
    if currentValue == 'X' or currentValue == 'O':
        cv = False
        print ('invalid value  = this place is already taken')
    return cv

def userInputPlayGame(board):
    #asks user for input in terms of row and column
    #print ('please enter your choice of entery')
    playerInput1 = input('please enter your choice of column ')
    playerInput2 = input('please enter your choice of row ')
    playerInput1 = int(playerInput1)
    playerInput2 = int(playerInput2)

    print('user entered value for place (', playerInput1, ' , ',  playerInput2,  ')')
    abc = checkIfFree(board, playerInput1, playerInput2)
    print('here-3 ', abc)
    #if (abc != True):
     #   print ('invalid value - this place is already taken. Please re-enter the selection')



b1 = createBoard_TicTacToe()
drawboard(b1)
L1 = userInput1()
userInputPlayGame(b1)