# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connect4.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: apickett <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/22 13:06:06 by apickett          #+#    #+#              #
#    Updated: 2018/10/22 14:23:57 by apickett         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

boardW = 7
boardH = 6
x = 0
y = 0

def main():
    while True:
        P1ece, P2ece = PickPiece()
        turn = First()
        print('%s will go first.' % (turn))
        mainboard = Newboard()

        while True:
            if turn == 'Player 1':
                drawBoard(mainboard)
                move = Playerinput(mainboard)
                moveset(mainboard, P1ece, move)
                if Wincond(mainboard, P1ece):
                    winner = 'Player 1'
                    break
                turn = 'Player 2'
            else:
                drawBoard(mainboard)
                move = Playerinput(mainboard)
                moveset(mainboard, P2ece, move)
                if Wincond(mainboard, P2ece):
                    winner = 'Player 2'
                    break
                turn = 'Player 1'

        drawBoard(mainboard)
        print("The winner is: %s" % winner)
        if not Ragequit():
            break

def moveset(board, player, x):
    for y in range(boardH-1, -1, -1):
        if board[x][y] == ' ':
            board[x][y] = player
            return

def Ragequit():
    quit = input()
    print("Rejouer? (y or quit)")
    if quit.lower().startswith('q'):
        sys.exit
    else:
        return input().lower().startswith('y')

def Playerinput(board):
    while True:
        print('Which column do you want to move on? (1-%s)' % (boardW))
        move = input()
        if not move.isdigit():
            continue
        move = int(move) - 1
        if isvalid(board, move):
            return move

def First():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def isvalid(board, move):
    if move < 0 or move >= boardW:
        return False
    
    if board[move][0] != ' ':
        return False

    return True

def drawBoard(board):
    print()
    for x in range(1, boardW + 1):
        print(' %s  ' % x, end='')
    print()

    print('+---+' + ('---+' * (boardW - 1)))

    for y in range(boardH):
        print('|   |' + ('   |' * (boardW - 1)))

        print('|', end='')
        for x in range(boardW):
            print(' %s |' % board[x][y], end='')
        print()

        print('|   |' + ('   |' * (boardW - 1)))

        print('+---+' + ('---+' * (boardW - 1)))

def Newboard():
    board = []
    for x in range(boardW):
        board.append([' '] * boardH)
    return board


def PickPiece():
    piece = ''
    while not (piece == 'X' or piece == '0'):
        print("Player 1, pick X or 0")
        piece = input().upper()
    
    if piece == 'X':
        return ['X', '0']
    else:
        return ['0', 'X']

def Wincond(board, piece):  
    for y in range(boardH):
        for x in range(boardW - 3):
            if board[x][y] == piece and board[x+1][y] == piece and board[x+2][y] == piece and board[x+3][y] == piece:
                return True
    for x in range(boardW):
        for y in range(boardH - 3):
            if board[x][y] == piece and board[x][y+1] == piece and board[x][y+2] == piece and board[x][y+3] == piece:
                return True
    for x in range(boardW - 3):
        for y in range(3, boardH):
            if board[x][y] == piece and board[x+1][y-1] == piece and board[x+2][y-2] == piece and board[x+3][y-3] == piece:
                return True
    for x in range(boardW - 3):
        for y in range(boardH - 3):
            if board[x][y] == piece and board[x+1][y+1] == piece and board[x+2][y+2] == piece and board[x+3][y+3] == piece:
                return True
    return False

    return False

if __name__ == '__main__':
    main()
