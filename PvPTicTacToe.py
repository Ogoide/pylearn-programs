from random import randint
from copy import copy

def loosing_check(board):
    if ' ' not in board.values():
        print('The board is full - better luck next time!')
        loose = True
        return loose

def board_printer(board_struct):
    val = list(board_struct.values())
    for i in range(0,9):
        if (i+1)/3 in range(4):
            print(val[i], )
        else:
            print(val[i], ' ', end='')

def victory(board):
    # Check victory conditions
    global victoryX; global victoryO
    if board['TL'] == 'X' and board['TM'] == 'X' and board['TR'] == 'X':
        victoryX = True
    elif board['ML'] == 'X' and board['MM'] == 'X' and board['MR'] == 'X':
        victoryX = True
    elif board['BL'] == 'X' and board['BM'] == 'X' and board['BR'] == 'X':
        victoryX = True
    elif board['TL'] == 'X' and board['ML'] == 'X' and board['BL'] == 'X':
        victoryX = True
    elif board['TM'] == 'X' and board['MM'] == 'X' and board['BM'] == 'X':
        victoryX = True
    elif board['TR'] == 'X' and board['MR'] == 'X' and board['BR'] == 'X':
        victoryX = True
    elif board['TL'] == 'X' and board['MM'] == 'X' and board['BR'] == 'X':
        victoryX = True
    elif board['BL'] == 'X' and board['MM'] == 'X' and board['TR'] == 'X':
        victoryX = True

    if board['TL'] == 'O' and board['TM'] == 'O' and board['TR'] == 'O':
        victoryO = True
    elif board['ML'] == 'O' and board['MM'] == 'O' and board['MR'] == 'O':
        victoryO = True
    elif board['BL'] == 'O' and board['BM'] == 'O' and board['BR'] == 'O':
        victoryO = True
    elif board['TL'] == 'O' and board['ML'] == 'O' and board['BL'] == 'O':
        victoryO = True
    elif board['TM'] == 'O' and board['MM'] == 'O' and board['BM'] == 'O':
        victoryO = True
    elif board['TR'] == 'O' and board['MR'] == 'O' and board['BR'] == 'O':
        victoryO = True
    elif board['TL'] == 'O' and board['MM'] == 'O' and board['BR'] == 'O':
        victoryO = True
    elif board['BL'] == 'O' and board['MM'] == 'O' and board['TR'] == 'O':
        victoryO = True
    if victoryX:
        board_printer(board)
        print('X Player Wins! Congratulations!')
        return True
    elif victoryO:
        board_printer(board)
        print('O Player Wins! Congratulations!')
        return True


rng = randint(0,1)
if rng == 0:
    rpp = 'X'
else:
    rpp = 'O'

print('Choose a cell to enter \'X\' or \'O\' in it.')
print('TL TM TR\n'
      'ML MM MR\n'
      'BL BM BR')

while True:
    board = {'TL':' ', 'TM':' ', 'TR':' ',
             'ML':' ', 'MM':' ', 'MR':' ',
             'BL':' ', 'BM':' ', 'BR':' '}

    victoryX = False; victoryO = False
    while True:
        e1 = 0; e2 = 0
        temp_board = board.copy()
        error = False

        if rpp == 'X':
            player1 = input('Choose a cell to insert \'X\':\n')
            for k in temp_board.keys():
                if player1 == k:
                    if temp_board[k] != ' ':
                        print('That cell is already occupied. Please try again.')
                        error = True
                    else:
                        temp_board[k] = 'X'
                else:
                    e1 += 1
            if e1 == len(temp_board.keys()):
                print('Sorry, I couldn\'t understand your choice. Please try again.')
                error = True
            if not error:
                board_printer(temp_board)
                victory(temp_board)
                if victory(temp_board):
                   break
                if loosing_check(temp_board):
                   break

            if not error:
                player2 = input('Choose a cell to insert \'O\':\n')
                for k in temp_board.keys():
                    if player2 == k:
                        if temp_board[k] != ' ':
                            print('That cell is already occupied. Please try again.')
                            error = True
                        else:
                            temp_board[k] = 'O'
                    else:
                        e2 += 1
                if e2 == len(temp_board.keys()):
                    print('Sorry, I couldn\'t understand your choice. Please try again.')
                    error = True
            if not error:
                board_printer(temp_board)
                victory(temp_board)
                if victory(temp_board):
                    break
                if loosing_check(temp_board):
                    break

        else:
            player1 = input('Choose a cell to insert \'O\':\n')
            for k in temp_board.keys():
                if player1 == k:
                    if temp_board[k] != ' ':
                        print('That cell is already occupied. Please try again.')
                        error = True
                    else:
                        temp_board[k] = 'O'
                else:
                    e1 += 1
            if e1 == len(temp_board.keys()):
                print('Sorry, I couldn\'t understand your choice. Please try again.')
                error = True
            if not error:
                board_printer(temp_board)
                victory(temp_board)
                if victory(temp_board):
                    break
                if loosing_check(temp_board):
                    break

            if error == False:
                player2 = input('Choose a cell to insert \'X\':\n')
                for k in temp_board.keys():
                    if player2 == k:
                        if temp_board[k] != ' ':
                            print('That cell is already occupied. Please try again.')
                            error = True
                        else:
                            temp_board[k] = 'X'
                    else:
                        e2 += 1
                if e2 == len(temp_board.keys()):
                    print('Sorry, I couldn\'t understand your choice. Please try again.')
                    error = True
                if not error:
                    board_printer(temp_board)
                    victory(temp_board)
                    if victory(temp_board):
                        break
                    if loosing_check(temp_board):
                        break
        if error == False:
            board = temp_board.copy()
    nxt = input('Want to go for another round? (Y to confirm/anything else to exit)\n')
    if nxt == 'Y':
        continue
    else:
        break

