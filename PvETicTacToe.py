from random import choice
from time import sleep

mm = True
def loosing_check(board):
    if ' ' not in board.values():
        print('The board is full - better luck next time!')
        loose = True
        return loose


def board_printer(board_struct):
    val = list(board_struct.values())
    for i in range(0, 9):
        if (i + 1) / 3 in range(4):
            print(val[i], )
        else:
            print(val[i], ' ', end='')


def victory(board):
    # Check victory conditions
    global victoryX
    global victoryO
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
        print('Computer Wins! Better luck next time!')
        return True


def add_letter(tempboard, play):
    e1 = 0
    for k in tempboard.keys():
        if play == k:
            if tempboard[k] != ' ':
                print('That cell is already occupied. Please try again.')
                sleep(1)
                raise Exception
            else:
                tempboard[k] = 'X'
        else:
            e1 += 1
    if e1 == len(tempboard.keys()):
        print('Sorry, I couldn\'t understand your choice. Please try again.')
        sleep(1)
        raise Exception


def corners_play():
    global pcmove
    pcmove = 1
    corners = ['TL', 'TR', 'BL', 'BR']
    c = choice(corners)
    oc = 0
    for cc in corners:
        if tempboard[cc] != ' ':
            oc += 1
    if oc != 4:
        while True:
            if tempboard[c] == ' ':
                tempboard[c] = 'O'
                pcmove -= 1
                break
            else:
                c = choice(corners)


print('Choose a cell to enter \'X\' or \'O\' in it.')
print('TL TM TR\n'
      'ML MM MR\n'
      'BL BM BR')

while True:
    board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
             'ML': ' ', 'MM': ' ', 'MR': ' ',
             'BL': ' ', 'BM': ' ', 'BR': ' '}
    # Initial victory conditions set to false
    victoryX = False
    victoryO = False

    while True:
        # First play from the player
        error = False
        # Index of the dict that is ran through
        e1 = 0
        tempboard = board.copy()
        play = input('Enter your choice:\n')
        try:
            add_letter(tempboard, play)
        except:
            error = True

        while True:
            if not error:
                # Computer game-logic and player counterplay
                if tempboard['MM'] == ' ':
                    tempboard['MM'] = 'O'
                    mm = False
                elif tempboard['MM'] == 'X':
                    corners_play()

                print('The computer has chosen it\'s move!')
                board_printer(tempboard)
                board = tempboard.copy()

                # Player's next move
                while True:
                    pcmove = 1
                    error = False
                    O_win = ' '
                    X_block = ' '
                    play = input('Enter your choice:\n')
                    try:
                        add_letter(tempboard, play)
                        print('You made a move.')
                        board_printer(tempboard)
                        board = tempboard.copy()
                        sleep(1)
                    except:
                        error = True

                    victory(board)
                    if victory(board):
                        exit()
                    if loosing_check(board):
                        exit()
                    teste = 1
                    if (not victory(board) or not loosing_check(board)) and not error:

                        # Top row check logic
                        top = ['TL', 'TM', 'TR']
                        top_equal_letters_X = 0
                        top_equal_letters_O = 0
                        for l in top:
                            if tempboard[l] == 'X':
                                top_equal_letters_X += 1
                            elif tempboard[l] == 'O':
                                top_equal_letters_O += 1
                        if top_equal_letters_O == 2 and top_equal_letters_O + top_equal_letters_X != 3 and pcmove == 1:
                            for l in top:
                                if tempboard[l] == ' ':
                                    O_win = l
                        elif top_equal_letters_X == 2 and top_equal_letters_O + top_equal_letters_X != 3 and pcmove == 1:
                            for l in top:
                                if tempboard[l] == ' ':
                                    X_block = l

                        # Middle row check logic
                        middle = ['ML', 'MM', 'MR']
                        middle_equal_letters_X = 0
                        middle_equal_letters_O = 0
                        for l in middle:
                            if tempboard[l] == 'X':
                                middle_equal_letters_X += 1
                            elif tempboard[l] == 'O':
                                middle_equal_letters_O += 1
                        if middle_equal_letters_O == 2 and middle_equal_letters_O + middle_equal_letters_X != 3 and pcmove == 1:
                            for l in middle:
                                if tempboard[l] == ' ':
                                    O_win = l
                        elif middle_equal_letters_X == 2 and middle_equal_letters_O + middle_equal_letters_X != 3 and pcmove == 1:
                            for l in middle:
                                if tempboard[l] == ' ':
                                    X_block = l

                        # Bottom row check logic
                        bottom = ['BL', 'BM', 'BR']
                        bottom_equal_letters_X = 0
                        bottom_equal_letters_O = 0
                        for l in bottom:
                            if tempboard[l] == 'X':
                                bottom_equal_letters_X += 1
                            elif tempboard[l] == 'O':
                                bottom_equal_letters_O += 1
                        if bottom_equal_letters_O == 2 and bottom_equal_letters_O + bottom_equal_letters_X != 3 and pcmove == 1:
                            for l in bottom:
                                if tempboard[l] == ' ':
                                    O_win = l
                        elif bottom_equal_letters_X == 2 and bottom_equal_letters_O + bottom_equal_letters_X != 3 and pcmove == 1:
                            for l in bottom:
                                if tempboard[l] == ' ':
                                    X_block = l

                        # Left column check logic
                        left = ['TL', 'ML', 'BL']
                        left_equal_letters_X = 0
                        left_equal_letters_O = 0
                        for l in left:
                            if tempboard[l] == 'X':
                                left_equal_letters_X += 1
                            elif tempboard[l] == 'O':
                                left_equal_letters_O += 1
                        if left_equal_letters_O == 2 and left_equal_letters_O + left_equal_letters_X != 3 and pcmove == 1:
                            for l in left:
                                if tempboard[l] == ' ':
                                    O_win = l
                        elif left_equal_letters_X == 2 and left_equal_letters_O + left_equal_letters_X != 3 and pcmove == 1:
                            for l in left:
                                if tempboard[l] == ' ':
                                    X_block = l

                        # Middle column check logic
                        middlec = ['TM', 'MM', 'BM']
                        middlec_equal_letters_X = 0
                        middlec_equal_letters_O = 0
                        for l in middlec:
                            if tempboard[l] == 'X':
                                middlec_equal_letters_X += 1
                            elif tempboard[l] == 'O':
                                middlec_equal_letters_O += 1
                        if middlec_equal_letters_O == 2 and middlec_equal_letters_X + middlec_equal_letters_O != 3 and pcmove == 1:
                            for l in middlec:
                                if tempboard[l] == ' ':
                                    O_win = l
                        elif middlec_equal_letters_X == 2 and middlec_equal_letters_X + middlec_equal_letters_O != 3 and pcmove == 1:
                            for l in middlec:
                                if tempboard[l] == ' ':
                                    X_block = l

                        # Right column check logic
                        right = ['TR', 'MR', 'BR']
                        right_equal_letters_X = 0
                        right_equal_letters_O = 0
                        for l in right:
                            if tempboard[l] == 'X':
                                right_equal_letters_X += 1
                            elif tempboard[l] == 'O':
                                right_equal_letters_O += 1
                        if right_equal_letters_O == 2 and right_equal_letters_X + right_equal_letters_O != 3 and pcmove == 1:
                            for l in right:
                                if tempboard[l] == ' ':
                                    O_win = l
                        elif right_equal_letters_X == 2 and right_equal_letters_X + right_equal_letters_O != 3 and pcmove == 1:
                            for l in right:
                                if tempboard[l] == ' ':
                                    X_block = l

                        # Left diagonal check logic
                        ldiag = ['TL', 'MM', 'BR']
                        ldiag_equal_letters_X = 0
                        ldiag_equal_letters_O = 0
                        for l in ldiag:
                            if tempboard[l] == 'X':
                                ldiag_equal_letters_X += 1
                            elif tempboard[l] == 'O':
                                ldiag_equal_letters_O += 1
                        if ldiag_equal_letters_O == 2 and ldiag_equal_letters_X + ldiag_equal_letters_O != 3 and pcmove == 1:
                            for l in ldiag:
                                if tempboard[l] == ' ':
                                    O_win = l
                        elif ldiag_equal_letters_X == 2 and ldiag_equal_letters_X + ldiag_equal_letters_O != 3 and pcmove == 1:
                            for l in ldiag:
                                if tempboard[l] == ' ':
                                    X_block = l

                        # Right diagonal check logic
                        rdiag = ['TR', 'MM', 'BL']
                        rdiag_equal_letters_X = 0
                        rdiag_equal_letters_O = 0
                        for l in rdiag:
                            if tempboard[l] == 'X':
                                rdiag_equal_letters_X += 1
                            elif tempboard[l] == 'O':
                                rdiag_equal_letters_O += 1
                        if rdiag_equal_letters_O == 2 and rdiag_equal_letters_X + rdiag_equal_letters_O != 3 and pcmove == 1:
                            for l in rdiag:
                                if tempboard[l] == ' ':
                                    O_win = l
                        elif rdiag_equal_letters_X == 2 and rdiag_equal_letters_X + rdiag_equal_letters_O != 3 and pcmove == 1:
                            for l in rdiag:
                                if tempboard[l] == ' ':
                                    X_block = l

                        # Placing the computer's letter, prioritizing win conditions
                        if O_win != ' ':
                            tempboard[O_win] = 'O'
                        elif X_block != ' ':
                            tempboard[X_block] = 'O'
                        elif pcmove == 1 and ' ' in tempboard.values() and mm == False:
                            for k in tempboard.keys():
                                if tempboard[k] == 'X':
                                    if k == 'TL' and teste==1:
                                        l1 = ['TM', 'ML']
                                        tempboard[choice(l1)] = 'O'
                                        teste -= 1
                                    elif k == 'TR' and teste==1:
                                        l1 = ['TM', 'MR']
                                        tempboard[choice(l1)] = 'O'
                                        teste -= 1
                                    elif k == 'BR' and teste==1:
                                        l1 = ['BM', 'MR']
                                        tempboard[choice(l1)] = 'O'
                                        teste -= 1
                                    elif k == 'BL' and teste==1:
                                        l1 = ['BM', 'ML']
                                        tempboard[choice(l1)] = 'O'
                                        teste -= 1

                        elif pcmove == 1 and ' ' in tempboard.values():
                            corners_play()
                        elif pcmove == 1 and ' ' in tempboard.values():
                            empty = []
                            for k in tempboard.keys():
                                if tempboard[k] == ' ':
                                    empty.append(k)
                            while True:
                                tch = choice(empty)
                                if tch == ' ':
                                    tempboard[tch] = 'O'
                                    pcmove -= 1

                        print('The computer has made it\'s move!')
                        board_printer(tempboard)
                        board = tempboard.copy()

                        victory(tempboard)
                        if victory(tempboard):
                            exit()
                        if loosing_check(tempboard):
                            exit()
            else:
                break
