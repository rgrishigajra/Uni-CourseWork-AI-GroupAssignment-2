#!/usr/local/bin/python3

"""
This is where you should write your AI code!

Authors: PLEASE ENTER YOUR NAMES AND USER ID'S HERE

Based on skeleton code by Abhilash Kuhikar, October 2019
"""

from logic_IJK import Game_IJK
import random
import copy
import numpy as np
# Suggests next move to be played by the current player given the current game
#
# inputs:
#     game : Current state of the game 
#
# This function should analyze the current state of the game and determine the 
# best move for the current player. It should then call "yield" on that move.

transform = {'a': 2, 'b': 4, 'c': 8, 'd': 16, 'e': 32, 'f': 64, 'g': 128, 'h': 256, 'i': 512, 'j': 1024, 'k': 2048}

def convert(boardi):
    for i in range(0, 6):
        for j in range(0, 6):
            if boardi[i][j] != ' ':
                boardi[i][j] = transform[boardi[i][j].lower()]
    return boardi

h=[[5,4,3,2,1,0],[4,3,2,1,0,-1],[3,2,1,0,-1,-2],[2,1,0,-1,-2,-3],[1,0,-1,-2,-3,-4],[0,-1,-2,-3,-4,-5]]


def utility(s):
    sum=0
    s=convert(s)
    for i in range(0,5):
        for j in range(0,5):
            if s[i][j]!=' ':
                sum=sum+s[i][j]*h[i][j]
    return sum


def successor(game,i):
    game.makeMove(i)
    return game



def minimax(game, depth, maxPlayer,alpha,beta):
    if depth == 0 or game.isGameFull():
        return utility(game.getGame())
    elif maxPlayer == True:
        value = float('-inf')
        for i in ['U','L','R','D']:
            child=successor(copy.deepcopy(game),i)
            value = max(value, minimax(child, depth-1, False,alpha,beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in ['U','L','R','D']:
            child=successor(copy.deepcopy(game),i)
            value = min(value, minimax(child, depth-1, True,alpha,beta))
            beta = min(beta, value)
            if alpha >=beta:
                break
        return value






def next_move(game: Game_IJK)-> None:

    '''board: list of list of strings -> current state of the game
       current_player: int -> player who will make the next move either ('+') or -'-')
       deterministic: bool -> either True or False, indicating whether the game is deterministic or not
    '''

    board = game.getGame()
    player = game.getCurrentPlayer()
    deterministic = game.getDeterministic()

    moves=['U', 'L', 'R', 'D']
    value=[]
    for i in ['U', 'L', 'R', 'D']:
        child = successor(copy.deepcopy(game), i)
        value.append(minimax(child, 3, True,float('-inf'),float('inf')))
    k = np.argmax(value)



    # You'll want to put in your fancy AI code here. For right now this just 
    # returns a random move.
    if (player=='+'):
        yield moves[k]
    else:
        yield random.choice(['U', 'D', 'L', 'R'])
    # yield moves[k]