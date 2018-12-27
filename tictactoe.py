# TODO Prevent overwriting moves
# TODO Show available moves
# TODO Check if won
# TODO Announce winner
# TODO Get computer to play against user

theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}


# def check_spot(board):



def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-----')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-----')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = raw_input().lower()
    if move in theBoard:
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        print 'ERROR. Please enter a valid move.'
printBoard(theBoard)
