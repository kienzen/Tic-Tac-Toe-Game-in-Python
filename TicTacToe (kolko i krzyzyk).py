# -*- coding: utf-8 -*-
# %%
import random

board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}


def display_board():
    print('   ', board[1], '|', board[2], '|', board[3])
    print('_________________')
    print('   ', board[4], '|', board[5], '|', board[6])
    print('_________________')
    print('   ', board[7], '|', board[8], '|', board[9])


def has_won(board):
    blank = " "
    if board[1] == board[2] == board[3] != blank or board[4] == board[5] == board[6] != blank or board[7] == board[8] == \
            board[9] != blank:
        return True
    elif board[1] == board[4] == board[7] != blank or board[2] == board[5] == board[8] != blank or board[3] == board[
        6] == board[9] != blank:
        return True
    elif board[1] == board[5] == board[9] != blank or board[3] == board[5] == board[7] != blank:
        return True
    else:
        return False


def if_draw(board):
    lista_pol = []
    for k, v in board.items():
        lista_pol.append(v)
    if " " in lista_pol:
        return False
    else:
        return True


def makes_move(active_player, player1):
    if active_player == player1:
        mark = "X"
    else:
        mark = "O"

    while True:
        print(active_player, ',where would you like to put your mark?')
        n = int(input())
        if board[n] == " ":
            board[n] = mark
            break
        else:
            print("Please pick a free field")


def next_turn(active_player, player1, player2):
    if active_player == player1:
        return player2
    else:
        return player1


def tictactoe():
    print("Welcome to Tic Tac Toe written by Adam")
    print("Player1 plays with X, while Player2 uses O")
    player1 = input("Please write your name Player1:")
    player2 = input("Please write your name Player2:")
    active_player = ""
    if random.randint(1, 2) == 1:
        active_player = player1
    else:
        active_player = player2

    while True:
        display_board()
        makes_move(active_player, player1)
        display_board()
        print('\n' * 100)
        if has_won(board):
            print("Congratulations", active_player, "! You have won!")
            break
        if if_draw(board):
            print("Draw!")
            break
        active_player = next_turn(active_player, player1, player2)


tictactoe()

