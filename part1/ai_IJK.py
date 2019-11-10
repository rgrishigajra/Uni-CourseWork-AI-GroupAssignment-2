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

<<<<<<< HEAD
transformplus = {'a': 2, 'b': 4, 'c': 8, 'd': 16, 'e': 32, 'f': 64, 'g': 128, 'h': 256, 'i': 512, 'j': 1024, 'k': 2048,
             'A': 2, 'B': 4, 'C': 8, 'D': 16, 'E': 32, 'F': 64, 'G': 128, 'H': 256, 'I': 512, 'J': 1024, 'K': 2048}
transformminus= {'a': 2, 'b': 4, 'c': 8, 'd': 16, 'e': 32, 'f': 64, 'g': 128, 'h': 256, 'i': 512, 'j': 1024, 'k': 2048,
             'A': -2, 'B': -4, 'C': -8, 'D': -16, 'E': -32, 'F': -64, 'G': -128, 'H': -256, 'I': -512, 'J': -1024, 'K': -2048}

# p=Game_IJK.getCurrentPlayer()
# if p=='-':
#     for key in transform:
#         transform[key] = -1 * transform[key]
#

def convert(boardi,game):
    #print(game.getCurrentPlayer())
=======
#dictionary to transform letters into corresponding numbers for '+' player
transformplus = {'a': -2, 'b': -4, 'c': -8, 'd': -16, 'e': -32, 'f': -64, 'g': -128, 'h': -256, 'i': -512, 'j': -1024, 'k': -2048,
             'A': 2, 'B': 4, 'C': 8, 'D': 16, 'E': 32, 'F': 64, 'G': 128, 'H': 256, 'I': 512, 'J': 1024, 'K': 2048}

#dictionary to transform letters into corresponding numbers for -' player
transformminus= {'a': 2, 'b': 4, 'c': 8, 'd': 16, 'e': 32, 'f': 64, 'g': 128, 'h': 256, 'i': 512, 'j': 1024, 'k': 2048,
             'A': -2, 'B': -4, 'C': -8, 'D': -16, 'E': -32, 'F': -64, 'G': -128, 'H': -256, 'I': -512, 'J': -1024, 'K': -2048}

#heuristic (weight) matrix used for calculating utility value
heuristic=[
    [2048, 1024, 512, 256, 128, 64],
    [1024, 512, 256, 128, 64, 32],
    [512, 256, 128, 64, 32, 16],
    [256, 128, 64, 32, 16, 8],
    [128, 64, 32, 16, 8, 4],
    [64, 32, 16, 8, 4, 2],
]

#function to convert current board with letters  to numbers
def convert(boardi,game):
>>>>>>> 0f41c5cb4fa411578ce43963dd5451ddca685122
    for i in range(0, 6):
        for j in range(0, 6):
            if boardi[i][j] != ' ' and game.getCurrentPlayer()=='+':
                boardi[i][j] = transformplus[boardi[i][j]]
            if boardi[i][j] != ' ' and game.getCurrentPlayer()=='-':
<<<<<<< HEAD
                boardi[i][j] = transformplus[boardi[i][j]]
    #game.printGame()
    return boardi

# h=[
#     [2048, 512, 64, 16, 4, 0],
#     [512, 64, 16, 4, 0, -1],
#     [64, 16, 4, 0, -1, -2],
#     [16, 4, 0, -1, -2, -3],
#     [4, 0, -1, -2, -3, -4],
#     [0, -1, -2, -3, -4, -5],
# ]
h=[[1024,512,256,128,64,32],
   [512,256,128,64,32,16],
   [256,128,64,32,16,8],
   [128,64,32,16,8,4],
   [64,32,16,8,4,2],
   [32,16,8,4,2,1]]
ht=[[17179869184, 16777216, 8388608, 4096, 2048, 1],
        [8589934592, 33554432, 4194304, 8192, 1024, 2],
        [4294967296, 67108864, 2097152, 16384, 512, 4],
        [2147483648, 536870912, 1048576, 32768, 256, 8],
        [1073741824, 134217728, 524288, 65536, 128, 16],
        [536870912, 268435456, 262144, 131072, 64, 32]]

# d=[[1,2,3,4,5,6],
#    [2,3,4,5,6,7],
#    [3,4,5,6,7,8],
#    [4,5,6,7,8,9],
#    [5,6,7,8,9,10],
#    [6,7,8,9,10,11]]
#
# def emptytiles(s):
#     c=0
#     for i in range(0, 6):
#         for j in range(0, 6):
#             if s[i][j] == ' ':
#                 c+=1
#     return c
#
# def penalty(s):
#     pd = 0
#     pr = 0
#     for i in range(0, 5):
#         for j in range(0, 5):
#             if s[i][j] != ' ' and s[i + 1][j] != ' ':
#                 pd = pd + abs(abs(s[i][j]) - abs(s[i + 1][j]))
#     for i in range(0, 5):
#         for j in range(0, 5):
#             if s[i][j] != ' ' and s[i][j + 1] != ' ':
#                 pr = pr + abs(abs(s[i][j]) - abs(s[i][j + 1]))
#     return pr+pd

def weight(s):
    sum1=0
    sum2=0
    sum3=0
    # for i in range(0, 6):
    #     for j in range(0, 6):
    #         if s[i][j] != ' ':
    #             sum1 = sum1 + s[i][j] * h[i][j]
    for i in range(0, 6):
      for j in range(0, 6):
          if s[i][j] != ' ':
              sum1 = sum1 + s[i][j] * h[i][j]
            #sum2 = sum2 + s[i][j] * ht[i][j]
          else:
              sum3+=2048
    #monotonic
    return (sum1+sum2+sum3)

def utility(s,game):
    s=convert(s,game)
    # e=emptytiles(s)
    # p=penalty(s)
    w=weight(s)
    # u=e-p+w
    return w
=======
                boardi[i][j] = transformminus[boardi[i][j]]
    return boardi


#function to calculate penalty based on neighboring elements(right and down)
def penalty(currentState):
    penaltyDown = 0
    penaltyRight = 0
    #calculate penalties with right neighbour
    for i in range(0, 5):
        for j in range(0, 5):
            if currentState[i][j] != ' ' and currentState[i + 1][j] != ' ':
                penaltyDown = penaltyDown + abs(abs(currentState[i][j]) - abs(currentState[i + 1][j]))
    #calculate penalties with bottom element
    for i in range(0, 5):
        for j in range(0, 5):
            if currentState[i][j] != ' ' and currentState[i][j + 1] != ' ':
                penaltyRight = penaltyRight + abs(abs(currentState[i][j]) - abs(currentState[i][j + 1]))
    return (penaltyRight+penaltyDown)


#function to calculate weight values and empty tiles
def weight(currentState):
    weightValue=0
    emptyTiles=0
    for i in range(0, 6):
      for j in range(0, 6):
          if currentState[i][j] != ' ':
            weightValue+=currentState[i][j] * heuristic[i][j]
          else:
              emptyTiles+=1
    return (weightValue+emptyTiles)


#function to calculate utility value
def utility(currentState,game):
    currentState=convert(currentState,game)
    utilityValue=penalty(currentState)+weight(currentState)
    return utilityValue
>>>>>>> 0f41c5cb4fa411578ce43963dd5451ddca685122

#function to generate successor
def successor(game,i):
    game.makeMove(i)
    return game

<<<<<<< HEAD
=======
#minimax algorithm used for game with alpha-beta pruning
>>>>>>> 0f41c5cb4fa411578ce43963dd5451ddca685122
def minimax(game, depth, maxPlayer,alpha,beta):

    #terminal condition
    if depth == 0 or game.isGameFull():
        return utility(game.getGame(),game)

<<<<<<< HEAD
=======
    #when max player is playing
>>>>>>> 0f41c5cb4fa411578ce43963dd5451ddca685122
    elif maxPlayer == True:
        value = float('-inf')
        for i in ['U','L','R','D']:
            child=successor(copy.deepcopy(game),i)
            value = max(value, minimax(child, depth-1, False,alpha,beta))
            alpha = max(alpha, value)

            if alpha >= beta:
                break
        return value

    #when min player is playing
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

    # You'll want to put in your fancy AI code here. For right now this just
    # returns a random move.

    moves=['U', 'L', 'R', 'D']
    value=[]
    #start with minimax algorithm with current game state
    for i in ['U', 'L', 'R', 'D']:
        child = successor(copy.deepcopy(game), i)
        value.append(minimax(child, 3, False,float('-inf'),float('inf')))
<<<<<<< HEAD
=======
    #get index number with highest value
>>>>>>> 0f41c5cb4fa411578ce43963dd5451ddca685122
    k = np.argmax(value)
    #choose a move with highest minimax utility value
    yield moves[k]

    # You'll want to put in your fancy AI code here. For right now this just
    # returns a random move.

<<<<<<< HEAD
    yield moves[k]

    # yield moves[k]
=======
>>>>>>> 0f41c5cb4fa411578ce43963dd5451ddca685122
