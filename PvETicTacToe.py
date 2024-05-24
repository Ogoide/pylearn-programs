from random import randint, choice
from time import sleep
from datetime import datetime
import os, pickle

def loosing_check(board):
    if ' ' not in board.values():
        print('The board is full - better luck next time!')
        loose = True
        return loose


def board_printer(board_struct):
    s = ''
    board_keys_correspondence = {}
    board_keys = list(board_struct.keys())
    for i in range(1, 10):  # 1-9
        board_keys_correspondence.setdefault(i, board_keys[i - 1])
    for i in range(1, 10):
        if board_struct[board_keys_correspondence[i]] == 'X':
            s += '\033[34m' + 'X' + '\033[0m' + ' '
        elif board_struct[board_keys_correspondence[i]] == 'O':
            s += '\033[31m' + 'O' + '\033[0m' + ' '
        else:
            s += board_struct[board_keys_correspondence[i]] + ' '
        if i % 3 == 0:
            if i != 9:
                s += '\n'
    print('-' * 37)

    for row in s.split('\n'):
        print(' ' * 12, '| ', row, '|', sep='')

    print('-' * 37)


def board_printer_logger(board_struct):
    s = ''
    board_keys_correspondence = {}
    board_keys = list(board_struct.keys())
    for i in range(1, 10):  # 1-9
        board_keys_correspondence.setdefault(i, board_keys[i - 1])
    for i in range(1, 10):
        s += board_struct[board_keys_correspondence[i]] + ' '
        if i % 3 == 0:
            s += '\n'
    return s


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
        print('Player Wins! Congratulations!')
        return True
    elif victoryO:
        print('Computer Wins! Better luck next time!')
        return True

def add_letter(temp_board, play):
    e1 = 0
    for k in tempboard.keys():
        if play.upper().strip() == k:
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
    elif oc == 4:
        corners_used = True
        return corners_used

def setup_time():
    date_format = '%H%M-%d%m%Y'
    now = datetime.now()
    global time_string
    time_string = f'Log_{now:{date_format}}'
    return time_string

def log(board, action):
    board_struct = {}
    for k, v in board.items():
        if v == ' ':
            board_struct[k] = '_'
        else:
            board_struct[k] = v
    file_path = os.path.join(config('Read'),f'{time_string}.txt')
    if action == 'Start':
        with open(file_path, 'w') as file:
            file.write('Game started.\n')
            for row in board_printer_logger(board_struct).split('\n'):
                quote_row = ''.join(f'"{i}" ' for i in row.split())
                file.write(quote_row + '\n')
            file.write('-' * 20 + '\n')
    else:
        with open(file_path, 'a') as file:
            file.write(action + '\n')
            for row in board_printer_logger(board_struct).split('\n'):
                quote_row = ''.join(f'"{i}" ' for i in row.split())
                file.write(quote_row + '\n')
            file.write('-' * 20 + '\n')


def config(mode):
    if mode == 'Change':
        # Opening and closing truncates the file, clearing its contents
        with open('config.txt'):
            pass
        while True:
            new_log_path = input('Enter the new path for log files.\n')
            if os.path.exists(new_log_path):
                config_file = open('config.txt', 'wb')
                pickle.dump(new_log_path, config_file)
                config_file.close()
                break
            else:
                print('This path doesn\'t exist or is inaccessible.')
                sleep(1)
    else:
        try:
            config_file = open('config.txt', 'rb')
            log_path = pickle.load(config_file)
            config_file.close()
            return log_path
        except:
            while True:
                log_path = input('This game registers all moves in the form of a log file, which is created everytime the game starts.\n'
                                 'As such, please provide a path to the directory where this file should be created.\n').strip()
                if os.path.exists(log_path):
                    config_file = open('config.txt', 'wb')
                    pickle.dump(log_path, config_file)
                    config_file.close()
                    break
                else:
                    print('This path doesn\'t exist or is inaccessible.')
                    sleep(1)

def start_menu():
    setup_time()
    global play_start
    print('\033[36m' + '-'* 50)
    print('''\t\tWELCOME TO THE TIC-TAC-TOE!
    To change the configuration, enter [1]
    To play, enter [2]
    To exit, enter [3]''')
    print('-' * 50 + '\033[0m')
    for i in [1,2,3]:
        print('.', sep='', end='')
        sleep(1)
    print()
    while True:
        opc = input('Choose your option:\n')
        if opc.strip() == '1':
            config('Change')
            opc = input('Do you want to play now? [Y/N]\n')
            if opc.upper().strip() == 'Y':
                play_start = True
                break
            elif opc.upper().strip() == 'N':
                print('Goodbye!')
                sleep(1)
                exit()
        elif opc.strip() == '2':
            play_start = True
            break
        elif opc.strip() == '3':
            print('Goodbye!')
            sleep(1)
            exit()
        else:
            print('I\'m sorry, I couldn\'t understand your choice.')
            sleep(1)

play_start = False
config('start')
start_menu()

if play_start:
    print('-' * 10 + ' ', '\033[36m' + '\033[1m' + '\033[4m' + 'PVE TIC-TAC-TOE', '\033[0m' + ' ' + '-' * 10,'\n', sep='')

    print('Choose a cell to enter \'X\' in it.')
    print('TL TM TR\n'
          'ML MM MR\n'
          'BL BM BR')

    while True:
        board = {'TL':' ', 'TM':' ', 'TR':' ',
                 'ML':' ', 'MM':' ', 'MR':' ',
                 'BL':' ', 'BM':' ', 'BR':' '}
        # Initial victory conditions set to false
        victoryX = False; victoryO = False
        log(board, 'Game Started.')

        while True:
            # First play from the player
            error = False
            # Index of the dict that is ran through
            e1 = 0
            tempboard = board.copy()
            print('-' * 37)
            play = input('Enter your choice:\n')
            try:
                add_letter(tempboard, play)
                log(tempboard, 'Player\'s firt move.')
            except:
                error = True
                continue

            while True:
                if not error:
                    # Computer game-logic and player counterplay

                    if tempboard['MM'] == ' ':
                        tempboard['MM'] = 'O'
                        # Player didn't play to the middle
                        mm = False
                    elif tempboard['MM'] == 'X':
                        # Player played to the middle
                        mm = True
                        corners_play()

                    print('The computer has chosen it\'s move!')
                    log(tempboard, 'Computer\' first move.')
                    board_printer(tempboard)
                    board = tempboard.copy()

                    player_move = 2
                    # Player's next move
                    while True:
                        pcmove = 1
                        corners = ['TL', 'TR', 'BL', 'BR']
                        corners_val = []
                        for c in corners:
                            corners_val.append(tempboard[c])
                        error = False
                        O_win = ' '
                        X_block = ' '
                        sleep(1)
                        play = input('Enter your choice:\n')
                        try:
                            add_letter(tempboard, play)
                            print('You made a move.')
                            board_printer(tempboard)
                            log(tempboard, 'Player\'s next move.')
                            board = tempboard.copy()
                            sleep(1)
                        except:
                            error = True

                        victory(board)
                        if victory(board):
                            exit()
                        if loosing_check(board):
                            exit()

                        if ((not victory(board)) or (not loosing_check(board))) and (not error):

                            # Top row check logic
                            top = ['TL', 'TM', 'TR']
                            top_equal_letters_X = 0;
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
                            middle_equal_letters_X = 0;
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
                            elif (not mm) and player_move == 2 and (tempboard['TM'] == ' ') and (tempboard['BM'] == ' ') \
                                    and (tempboard['ML'] == ' ') and (tempboard['MR'] == ' '):
                                # If player didn´t start in the middle
                                for k in tempboard.keys():
                                    if tempboard[k] == 'X':
                                        if k == 'TL':
                                            l1 = ['TM', 'ML']
                                            rc1 = randint(0,1)
                                            if rc1 == 0 and tempboard[l1[rc1]] == ' ' and pcmove == 1:
                                                tempboard[l1[rc1]] = 'O'
                                                pcmove -= 1
                                            elif rc1 == 1 and tempboard[l1[rc1]] == ' ' and pcmove == 1:
                                                tempboard[l1[rc1]] = 'O'
                                                pcmove -= 1
                                        elif k == 'TR':
                                            l2 = ['TM', 'MR']
                                            rc2 = randint(0, 1)
                                            if rc2 == 0 and tempboard[l2[rc2]] == ' ' and pcmove == 1:
                                                tempboard[l2[rc2]] = 'O'
                                                pcmove -= 1
                                            elif rc2 == 1 and tempboard[l2[rc2]] == ' ' and pcmove == 1:
                                                tempboard[l2[rc2]] = 'O'
                                                pcmove -= 1
                                        elif k == 'BR':
                                            l3 = ['BM', 'MR']
                                            rc3 = randint(0, 1)
                                            if rc3 == 0 and tempboard[l3[rc3]] == ' ' and pcmove == 1:
                                                tempboard[l3[rc3]] = 'O'
                                                pcmove -= 1
                                            elif rc3 == 1 and tempboard[l3[rc3]] == ' ' and pcmove == 1:
                                                tempboard[l3[rc3]] = 'O'
                                                pcmove -= 1
                                        elif k == 'BL':
                                            l4 = ['BM', 'ML']
                                            rc4 = randint(0, 1)
                                            if rc4 == 0 and tempboard[l4[rc4]] == ' ' and pcmove == 1:
                                                tempboard[l4[rc4]] = 'O'
                                                pcmove -= 1
                                            elif rc4 == 1 and tempboard[l4[rc4]] == ' ' and pcmove == 1:
                                                tempboard[l4[rc4]] = 'O'
                                                pcmove -= 1

                            elif pcmove == 1 and (' ' in corners_val):
                                corners_play()


                            elif pcmove == 1:
                                empty_vals = []
                                for k, v in tempboard.items():
                                    if v == ' ':
                                        empty_vals.append(k)
                                rch = choice(empty_vals)
                                tempboard[rch] = 'O'
                            player_move += 1


                            print('The computer has made its move!')
                            board_printer(tempboard)
                            log(tempboard, 'Computer\'s next move.')
                            board = tempboard.copy()

                        else:
                            continue

                        victory(tempboard)
                        if victoryX or victoryO:

                            if victoryX:
                                log(tempboard, 'Player wins.')
                            if victoryO:
                                log(tempboard, 'Computer wins.')

                            exit()
                        if loosing_check(tempboard):
                            exit()
                    else:
                        break