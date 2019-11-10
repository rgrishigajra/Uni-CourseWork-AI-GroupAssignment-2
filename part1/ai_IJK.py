#!/usr/local/bin/python3

"""
This is where you should write your AI code!

Authors: [Milan Chheta(michheta), Rishabh Gajra(rgajra), Jay Madhu(jaymadhu)]

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

#dictionary to transform letters into corresponding numbers for '+' player
transformplus = {'a': -2, 'b': -4, 'c': -8, 'd': -16, 'e': -32, 'f': -64, 'g': -128, 'h': -256, 'i': -512, 'j': -1024, 'k': -2048,
             'A': 2, 'B': 4, 'C': 8, 'D': 16, 'E': 32, 'F': 64, 'G': 128, 'H': 256, 'I': 512, 'J': 1024, 'K': 2048}

#dictionary to transform letters into corresponding numbers for -' player
transformminus= {'a': 2, 'b': 4, 'c': 8, 'd': 16, 'e': 32, 'f': 64, 'g': 128, 'h': 256, 'i': 512, 'j': 1024, 'k': 2048,
             'A': -2, 'B': -4, 'C': -8, 'D': -16, 'E': -32, 'F': -64, 'G': -128, 'H': -256, 'I': -512, 'J': -1024, 'K': -2048}

#weight matrix used for calculating utility value
weightMatrix=[
    [2048, 1024, 512, 256, 128, 64],
    [1024, 512, 256, 128, 64, 32],
    [512, 256, 128, 64, 32, 16],
    [256, 128, 64, 32, 16, 8],
    [128, 64, 32, 16, 8, 4],
    [64, 32, 16, 8, 4, 2],
]

#function to convert current board with letters  to numbers
def convert(boardi,game):
    for i in range(0, 6):
        for j in range(0, 6):
            if boardi[i][j] != ' ' and game.getCurrentPlayer()=='+':
                boardi[i][j] = transformplus[boardi[i][j]]
            if boardi[i][j] != ' ' and game.getCurrentPlayer()=='-':
                boardi[i][j] = transformminus[boardi[i][j]]
    return boardi


# #function to calculate penalty based on neighboring elements(right and down)
# def penalty(currentState):
#     penaltyDown = 0
#     penaltyRight = 0
#     #calculate penalties with right neighbour
#     for i in range(0, 5):
#         for j in range(0, 5):
#             if currentState[i][j] != ' ' and currentState[i + 1][j] != ' ':
#                 penaltyDown = penaltyDown + abs(abs(currentState[i][j]) - abs(currentState[i + 1][j]))
#     #calculate penalties with bottom element
#     for i in range(0, 5):
#         for j in range(0, 5):
#             if currentState[i][j] != ' ' and currentState[i][j + 1] != ' ':
#                 penaltyRight = penaltyRight + abs(abs(currentState[i][j]) - abs(currentState[i][j + 1]))
#     return (penaltyRight+penaltyDown)
#

#function to calculate weight values and empty tiles
def weight(currentState):
    weightValue=0
    emptyTiles=0
    for i in range(0, 6):
      for j in range(0, 6):
          if currentState[i][j] != ' ':
            weightValue+=currentState[i][j] * weightMatrix[i][j]
          else:
              emptyTiles+=2048**4
    return (weightValue+emptyTiles)



#function to calculate utility value
def utility(currentState,game):
    currentState=convert(currentState,game)
    utilityValue=weight(currentState)
    return utilityValue

#function to generate successor
def successor(game,i):
    game.makeMove(i)
    return game

#minimax algorithm used for game with alpha-beta pruning
def minimax(game, depth, maxPlayer,alpha,beta):

    #terminal condition
    if depth == 0 or game.isGameFull():
        return utility(game.getGame(),game)

    #when max player is playing
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
    #get index number with highest value
    k = np.argmax(value)

    # You'll want to put in your fancy AI code here. For right now this just
    # returns a random move.

    #choose a move with highest minimax utility value
    yield moves[k]

        # yield moves[k]